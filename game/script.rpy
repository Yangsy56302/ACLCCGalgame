# The game starts here.
label start:
    $ is_ingame = True
    stop music

    call setup_naming_start from _call_setup_naming_start
    $ renpy.block_rollback()
    call ch0 from _call_ch0

    return


label to_be_continued(chp):
    while True:
        stop music fadeout 1.0
        scene black with dissolve

        menu:
            "查看已被废弃的AI剧情":
                jump vibe_ch2
            "查看游离的支线章节":
                menu:
                    "chex_unknown_oi":
                        call chex_unknown_oi from _call_chex_unknown_oi
                    "chex_unknown_baile_lefthanded":
                        call chex_unknown_baile_lefthanded from _call_chex_unknown_baile_lefthanded
                    "chex_myworld":
                        call chex_myworld from _call_chex_myworld
                    "返回":
                        pass
            "查看剧情建议":
                menu:
                    "查看[yoosee]的建议":
                        call chplotadvice_yoosee from _call_chplotadvice_yoosee
                    "查看[yangsy]的建议":
                        call chplotadvice_yangsy from _call_chplotadvice_yangsy
                    "返回":
                        pass
            "输入以指定一个label来执行":
                call chany from _call_chany
            "返回主菜单":
                return


image splash = "splash.png"
image attention = "attention.png"
label splashscreen: 
    $ migrate_persistent_variables()
    call request_manage_storage from _call_request_manage_storage

    if not renpy.windows and not renpy.variant("android"):
        mwam.comment "唔……这个系统既不是Windows也不是Android呢。"
        mwam.comment "其他平台的话，我们可没怎么正经测过……"
        mwam.comment "要是碰到什么奇怪的问题，就当是这片平台特有的彩蛋吧（"

    scene black 
    with Pause(1) 

    show attention with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)
    
    show splash with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)

    return


label request_manage_storage:
    if renpy.variant("android"):
        python:
            if is_external_storage_manager():
                print("所有文件访问权限已授予")
            else:
                print("正在请求所有文件访问权限...")
                request_all_files_access()
            
            renpy.pause(3.0)

        # 再次检查授权状态
            if is_external_storage_manager():
                print("权限已授予")
            else:
                print("权限未被授予")


init -999 python:
    is_debug_installed = False

init 999 python:
    if not is_debug_installed:
        persistent.debug_mode = False


init python:
    if renpy.android:
        import jnius
        mActivity = jnius.autoclass("org.renpy.android.PythonSDLActivity").mActivity
    else:
        mActivity = None


init python:
    if renpy.variant("android"):
        import os
        import shutil
        from jnius import autoclass

        PythonSDLActivity = autoclass('org.renpy.android.PythonSDLActivity')
        Intent = autoclass('android.content.Intent')
        Settings = autoclass('android.provider.Settings')
        Uri = autoclass('android.net.Uri')
        Environment = autoclass('android.os.Environment')

        def request_all_files_access():
            """跳转到系统设置页面，请求 '所有文件访问权限'"""
            intent = Intent()
            intent.setAction(Settings.ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION)
            current_activity = PythonSDLActivity.mActivity
            current_activity.startActivity(intent)

        def is_external_storage_manager():
            """检查是否已获得 MANAGE_EXTERNAL_STORAGE 权限"""
            return Environment.isExternalStorageManager()

        def release_file_quietly(source_file, target_subdir, target_filename):
            """在持有 MANAGE_EXTERNAL_STORAGE 权限的前提下，静默写入文件。"""
            if not renpy.android:
                print("非安卓环境")
                return

            # 1. 检查并请求权限
            if not is_external_storage_manager():
                request_all_files_access()
                renpy.notify("请在新页面中授权“所有文件访问权限”")
                return
            
            # 2. 获取公共目录根路径并构建目标目录
            ext_root = Environment.getExternalStorageDirectory().getAbsolutePath()
            target_dir = os.path.join(ext_root, target_subdir)
            os.makedirs(target_dir, exist_ok=True)
            target_path = os.path.join(target_dir, target_filename)

            # 3. 写入文件
            try:
                with renpy.file(source_file) as src:
                    with open(target_path, "wb") as dst:
                        shutil.copyfileobj(src, dst)
                print(f"文件释放成功: {target_path}")
                renpy.show_screen("copy_tip","已将文件保存至 \""+target_path+"\"")
            except Exception as e:
                print(f"释放失败: {e}")


label after_load:
    python:
        current_vars = getattr(renpy.store, "variables", None)

        if not isinstance(current_vars, dict):
            current_vars = {}
            renpy.store.variables = current_vars

        if "another_view" not in current_vars:
            current_vars["another_view"] = bool(getattr(renpy.store, "another_view", False))

        if hasattr(renpy.store, "another_view"):
            del renpy.store.another_view
    return


init python:
    if renpy.windows:
        _active_cmd_consoles = []

        # 控制台窗口里运行的客户端程序（写入临时目录，由 python.exe 在新控制台中执行）
        # 输出：tail 队列文件；输入：把用户敲的行追加到 <队列文件>.in，交给 Ren'Py 主线程处理
        _CMD_CLIENT_CODE = r'''
import sys, os, time

os.system('chcp 65001 >nul')

q_file = sys.argv[1]
interactive = len(sys.argv) > 2 and sys.argv[2] == '1'
in_file = sys.argv[3] if len(sys.argv) > 3 else q_file + '.in'


def _set_title(text):
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(text)
    except Exception:
        pass


def _enable_vt():
    """Enable ANSI escapes so the input line can be erased with ESC[2K."""
    try:
        import ctypes
        k32 = ctypes.windll.kernel32
        handle = k32.GetStdHandle(-11)
        mode = ctypes.c_uint32()
        if not k32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        return bool(k32.SetConsoleMode(handle, mode.value | 0x0004))
    except Exception:
        return False


def _raw_ctrl_c():
    """Deliver Ctrl+C as a character instead of a signal."""
    try:
        import ctypes
        k32 = ctypes.windll.kernel32
        handle = k32.GetStdHandle(-10)
        mode = ctypes.c_uint32()
        if k32.GetConsoleMode(handle, ctypes.byref(mode)):
            k32.SetConsoleMode(handle, (mode.value & ~0x0001) | 0x0080)
    except Exception:
        pass


VT = _enable_vt() if interactive else False

try:
    import unicodedata
except ImportError:
    unicodedata = None


def _char_width(ch):
    if unicodedata is None:
        return 1
    return 2 if unicodedata.east_asian_width(ch) in ('W', 'F') else 1


def _text_width(text):
    return sum(_char_width(c) for c in text)


class LineEditor(object):
    """Hand-drawn input line, so game output can pre-empt it cleanly."""

    def __init__(self, out=None):
        self.out = out if out is not None else sys.stdout
        self.prompt = ''
        self.buf = []
        self.pos = 0
        self.history = []
        self.hist = None
        self.drawn = 0

    def text(self):
        return ''.join(self.buf)

    def active(self):
        return self.prompt != ''

    def clear(self):
        if not self.drawn:
            return
        if VT:
            self.out.write('\r\x1b[2K')
        else:
            self.out.write('\r' + ' ' * self.drawn + '\r')
        self.out.flush()
        self.drawn = 0

    def draw(self):
        self.clear()
        if not self.active():
            return
        line = self.prompt + self.text()
        self.out.write(line)
        self.out.flush()
        self.drawn = _text_width(line)

    def redraw(self):
        self.clear()
        self.draw()

    def insert(self, ch):
        self.buf.insert(self.pos, ch)
        self.pos += 1
        self.redraw()

    def backspace(self):
        if self.pos > 0:
            del self.buf[self.pos - 1]
            self.pos -= 1
            self.redraw()

    def delete(self):
        if self.pos < len(self.buf):
            del self.buf[self.pos]
            self.redraw()

    def left(self):
        if self.pos > 0:
            self.pos -= 1
            self.redraw()

    def right(self):
        if self.pos < len(self.buf):
            self.pos += 1
            self.redraw()

    def home(self):
        self.pos = 0
        self.redraw()

    def end(self):
        self.pos = len(self.buf)
        self.redraw()

    def reset(self):
        self.buf = []
        self.pos = 0
        self.hist = None
        self.redraw()

    def history_prev(self):
        if not self.history:
            return
        if self.hist is None:
            self.hist = len(self.history)
        if self.hist > 0:
            self.hist -= 1
            self.buf = list(self.history[self.hist])
            self.pos = len(self.buf)
            self.redraw()

    def history_next(self):
        if self.hist is None:
            return
        self.hist += 1
        if self.hist >= len(self.history):
            self.hist = None
            self.buf = []
        else:
            self.buf = list(self.history[self.hist])
        self.pos = len(self.buf)
        self.redraw()

    def submit(self):
        """Send the line to the game and go back to a plain idle console."""
        text = self.text()
        self.clear()
        self.out.write('\n')
        self.out.flush()
        if text.strip():
            self.history.append(text)
            try:
                with open(in_file, 'a', encoding='utf-8') as f:
                    f.write(text.replace('\r', ' ').replace('\n', ' ') + '\n')
            except Exception:
                pass
        self.prompt = ''
        self.buf = []
        self.pos = 0
        self.hist = None

    def handle(self, ch):
        """Feed one character (or an extended-key prefix) to the editor."""
        if not self.active():
            return
        if ch in ('\x00', '\xe0'):
            code = msvcrt.getwch()
            if code == 'H':
                self.history_prev()
            elif code == 'P':
                self.history_next()
            elif code == 'K':
                self.left()
            elif code == 'M':
                self.right()
            elif code == 'S':
                self.delete()
            elif code == 'G':
                self.home()
            elif code == 'O':
                self.end()
            return
        if ch in ('\r', '\n'):
            self.submit()
        elif ch == '\x08':
            self.backspace()
        elif ch in ('\x03', '\x15', '\x1b'):
            self.reset()
        elif ch >= ' ':
            self.insert(ch)


def main():
    import msvcrt

    if interactive:
        _raw_ctrl_c()

    editor = LineEditor()
    pos = 0

    def pump_output():
        """Print what the game queued; False means the queue file is gone."""
        nonlocal pos
        if not os.path.exists(q_file):
            return False
        try:
            with open(q_file, 'r', encoding='utf-8') as f:
                f.seek(pos)
                lines = f.readlines()
                pos = f.tell()
        except Exception:
            return True
        if not lines:
            return True

        editor.clear()
        for raw in lines:
            line = raw.rstrip('\n')
            if line == '__EXIT__':
                editor.clear()
                sys.stdout.flush()
                os._exit(0)
            elif line == '__CLS__':
                os.system('cls')
                editor.drawn = 0
            elif line.startswith('__COLOR__ '):
                os.system('color ' + line[10:])
            elif line.startswith('__TITLE__ '):
                _set_title(line[10:])
            elif line.startswith('__PROMPT__ '):
                editor.prompt = line[11:]
            elif line.startswith('__ECHO__ '):
                print(line[9:], flush=True)
        editor.draw()
        return True

    while True:
        try:
            if not pump_output():
                break
            if interactive:
                while msvcrt.kbhit():
                    editor.handle(msvcrt.getwch())
            time.sleep(0.03)
        except KeyboardInterrupt:
            continue
        except Exception:
            time.sleep(0.05)


if __name__ == '__main__':
    main()
'''

        class CmdWindow(object):
            """
            命令提示符控制台窗口控制器
            通过独立 IPC 命令队列常驻运行，彻底杜绝管道关闭闪退

            输出：Ren'Py 往队列文件追加 __ECHO__/__COLOR__ 等指令，窗口里的客户端进程负责显示。
            输入：拉取式——剧本里调用 `a = console.Input(">>> ")`，窗口显示提示符并等用户回车，
            函数把这行返回给剧本，由剧本自己决定显示还是执行（console.Python(a)）。
            只有 interactive=True 的窗口才读键盘；纯输出窗口敲什么都无效。
            客户端自己画提示符和输入行，游戏输出插进来时会擦掉重画，不会糊掉。
            """
            MAX_OUTPUT = 2000

            def __init__(self, title="Console", interactive=False):
                self.title = title
                self.interactive = bool(interactive)
                self.process = None
                self.queue_file = None
                self.input_file = None
                self.client_py = None
                self.input_pos = 0
                self.input_buf = b""

            def __getstate__(self):
                return {
                    "title": self.title,
                    "interactive": self.interactive,
                    "queue_file": self.queue_file,
                    "input_file": self.input_file,
                    "client_py": self.client_py
                }

            def __setstate__(self, state):
                self.title = state.get("title", "Console")
                self.interactive = state.get("interactive", False)
                self.queue_file = state.get("queue_file", None)
                self.input_file = state.get("input_file", None)
                self.client_py = state.get("client_py", None)
                self.process = None
                self.input_pos = 0
                self.input_buf = b""

            def Create(self):
                """创建并弹出新的命令提示符窗口"""
                import os
                import sys
                import tempfile
                import subprocess

                if self.process is not None and self.process.poll() is None:
                    return

                # 创建临时命令队列文件、输入回传文件与客户端执行脚本
                temp_dir = tempfile.gettempdir()
                self.queue_file = os.path.join(temp_dir, f"renpy_cmd_q_{id(self)}.txt")
                self.input_file = os.path.join(temp_dir, f"renpy_cmd_i_{id(self)}.txt")
                self.client_py = os.path.join(temp_dir, f"renpy_cmd_c_{id(self)}.py")
                self.input_pos = 0
                self.input_buf = b""

                temp_paths = [self.queue_file]
                if self.interactive:
                    temp_paths.append(self.input_file)
                for temp_path in temp_paths:
                    with open(temp_path, "w", encoding="utf-8"):
                        pass

                with open(self.client_py, "w", encoding="utf-8") as f:
                    f.write(_CMD_CLIENT_CODE)

                # 寻找同级目录的 python.exe 作为控制台程序载体
                py_dir = os.path.dirname(sys.executable)
                py_exe = os.path.join(py_dir, "python.exe")
                if not os.path.exists(py_exe):
                    py_exe = "python.exe"

                CREATE_NEW_CONSOLE = getattr(subprocess, "CREATE_NEW_CONSOLE", 0x00000010)

                si = subprocess.STARTUPINFO()
                STARTF_USESHOWWINDOW = getattr(subprocess, "STARTF_USESHOWWINDOW", 0x00000001)
                si.dwFlags |= STARTF_USESHOWWINDOW
                si.wShowWindow = 1 # SW_SHOWNORMAL

                try:
                    if self not in _active_cmd_consoles:
                        _active_cmd_consoles.append(self)
                    self.process = subprocess.Popen(
                        [py_exe, self.client_py, self.queue_file,
                        "1" if self.interactive else "0", self.input_file],
                        creationflags=CREATE_NEW_CONSOLE,
                        startupinfo=si
                    )
                except Exception as e:
                    print(f"启动控制台窗口失败: {e}")
                    return

                self._send_queue(f"__TITLE__ {self.title}")

            def _send_queue(self, msg):
                if self.queue_file and os.path.exists(self.queue_file):
                    try:
                        with open(self.queue_file, "a", encoding="utf-8") as f:
                            f.write(msg + "\n")
                    except Exception:
                        pass

            def CreateIfNeeded(func):
                """装饰器，在被装饰的方法运行前先确保窗口是否存在"""
                def wrapper(self, *args, **kwds):
                    if self.process is None or self.process.poll() is not None:
                        self.Create()
                    ret = func(self, *args, **kwds)
                    return ret
                return wrapper

            @CreateIfNeeded
            def ShowText(self, text=""):
                """在窗口中展示文本内容"""
                for line in str(text).splitlines():
                    self._send_queue(f"__ECHO__ {line}")

            @CreateIfNeeded
            def Clear(self):
                """清空控制台窗口中的文本"""
                self._send_queue("__CLS__")

            @CreateIfNeeded
            def Color(self, color_code="0A"):
                """修改窗口的背景与文字颜色 (cmd color 规范)"""
                self._send_queue(f"__COLOR__ {color_code}")

            @CreateIfNeeded
            def Title(self, title_text=""):
                """修改控制台窗口的标题"""
                self.title = str(title_text)
                self._send_queue(f"__TITLE__ {self.title}")

            # ---- 输入侧：由剧本主动拉取 ----

            def _send_prompt(self, prompt="> "):
                """让窗口显示一个等待输入的提示符"""
                if not self.interactive:
                    return
                self._send_queue("__PROMPT__ " + str(prompt))

            def _ensure_interactive(self):
                """确保窗口里跑的是可接收键盘的客户端，不是就重建一个"""
                alive = self.process is not None and self.process.poll() is None
                if self.interactive and alive:
                    return
                if alive:
                    self.Close()
                self.interactive = True
                self.Create()

            def _drop_pending_input(self):
                """丢掉窗口里还没被读走的旧输入，从文件末尾开始读"""
                self.input_buf = b""
                self.input_pos = 0
                try:
                    if self.input_file and os.path.exists(self.input_file):
                        self.input_pos = os.path.getsize(self.input_file)
                except Exception:
                    self.input_pos = 0

            def _take_line(self):
                """取一行已经敲完的输入；还没有就返回 None"""
                if not self.input_file or not os.path.exists(self.input_file):
                    return None

                try:
                    with open(self.input_file, "rb") as f:
                        f.seek(self.input_pos)
                        data = f.read()
                        self.input_pos = f.tell()
                except Exception:
                    return None

                if not data:
                    return None

                # 只处理完整的行，剩下的半行留到下一次（避免读到写了一半的内容）
                buf = self.input_buf + data
                if b"\n" not in buf:
                    self.input_buf = buf
                    return None

                head, _, rest = buf.partition(b"\n")
                self.input_buf = rest
                return head.decode("utf-8", "replace").rstrip("\r")

            def Input(self, prompt="> "):
                """阻塞等待用户在控制台窗口敲一行，返回这一行（不含换行）。

                用法：a = console.Input(">>> ")
                窗口先显示提示符，用户回车后返回；窗口被关掉时返回空字符串。
                只能在剧本里（python 块）调用，因为它会插入一段 renpy.pause 等待。
                """
                self._ensure_interactive()
                self._drop_pending_input()
                self._send_prompt(prompt)

                while True:
                    line = self._take_line()
                    if line is not None:
                        return line
                    if self.process is None or self.process.poll() is not None:
                        return ""
                    renpy.pause(0.05, hard=True, checkpoint=False)

            def Python(self, source):
                """在当前 store 里执行一段 Python，把返回值或报错写回窗口"""
                source = str(source).strip()
                if not source:
                    return

                try:
                    value = renpy.python.py_eval(source)
                except SyntaxError:
                    # 不是表达式，按语句执行
                    try:
                        renpy.python.py_exec(source)
                    except renpy.game.CONTROL_EXCEPTIONS:
                        self.ShowText("控制台不支持跳转 / 调用，请用内置控制台（Shift+O）。")
                    except Exception:
                        self._report()
                    return
                except renpy.game.CONTROL_EXCEPTIONS:
                    self.ShowText("控制台不支持跳转 / 调用，请用内置控制台（Shift+O）。")
                    return
                except Exception:
                    self._report()
                    return

                if value is not None:
                    text = repr(value)
                    if len(text) > self.MAX_OUTPUT:
                        text = text[:self.MAX_OUTPUT] + " ..."
                    self.ShowText(text)

            def _report(self):
                """把刚才的异常精简后写进窗口"""
                import traceback
                for line in traceback.format_exc().rstrip().splitlines()[-8:]:
                    self.ShowText(line)

            def Close(self):
                """关闭该命令提示符窗口"""
                self._send_queue("__EXIT__")
                if self.process is not None and self.process.poll() is None:
                    try:
                        self.process.terminate()
                    except Exception:
                        pass
                    self.process = None
                if self in _active_cmd_consoles:
                    _active_cmd_consoles.remove(self)
                self.input_pos = 0
                self.input_buf = b""
                # 清理临时文件
                try:
                    import os
                    if self.queue_file and os.path.exists(self.queue_file):
                        os.remove(self.queue_file)
                    if self.input_file and os.path.exists(self.input_file):
                        os.remove(self.input_file)
                    if self.client_py and os.path.exists(self.client_py):
                        os.remove(self.client_py)
                except Exception:
                    pass
