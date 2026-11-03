# The game starts here.
label start:
    $ is_ingame = True
    stop music

    call setup_naming_start from _call_setup_naming_start
    call nocutscene
    call ch0 from _call_ch0
    call cutscene("ch0")
    call ch1 from _call_ch1
    call cutscene("ch1")
    call ch2 from _call_ch2
    call cutscene("ch2")
    call ch3 from _call_ch3
    call cutscene("ch3")
    call to_be_continued("ch3")
    return


label cutscene(chp):

    stop music fadeout 1.0
    play sound "snd_screen_wipe_out.wav"
    scene black with wipeadofai

    with Pause(1.0)

    play sound "snd_screen_wipe_in.wav"
    scene expression "images/cutscene/[chp].png" with wipeadofai

    with Pause(3.0)
    
    play sound "snd_screen_wipe_out.wav"
    scene black with wipeadofai

    with Pause(1.0)

    return


label nocutscene:

    stop music fadeout 1.0
    play sound "snd_screen_wipe_out.wav"
    scene black with wipeadofai
    
    with Pause(1.0)

    return


label to_be_continued(chp):
    while True:
        stop music fadeout 1.0
        play sound "snd_screen_wipe_out.wav"
        scene black with wipeadofai

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

    play sound "snd_screen_wipe_out.wav"
    show attention with wipeadofai
    with Pause(2)

    play sound "snd_screen_wipe_in.wav"
    scene black with wipeadofai
    with Pause(1)
    
    play sound "snd_screen_wipe_out.wav"
    show splash with wipeadofai
    with Pause(2)
    
    play sound "snd_screen_wipe_in.wav"
    scene black with wipeadofai
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

        class CmdWindow(object):
            """
            命令提示符控制台窗口控制器
            通过独立 IPC 命令队列常驻运行，彻底杜绝管道关闭闪退
            """
            def __init__(self, title="Console"):
                self.title = title
                self.process = None
                self.queue_file = None
                self.client_py = None

            def __getstate__(self):
                return {
                    "title": self.title,
                    "queue_file": self.queue_file,
                    "client_py": self.client_py
                }

            def __setstate__(self, state):
                self.title = state.get("title", "Console")
                self.queue_file = state.get("queue_file", None)
                self.client_py = state.get("client_py", None)
                self.process = None

            def Create(self):
                """创建并弹出新的命令提示符窗口"""
                import os
                import sys
                import tempfile
                import subprocess

                if self.process is not None and self.process.poll() is None:
                    return

                # 创建临时命令队列文件与客户端执行脚本
                temp_dir = tempfile.gettempdir()
                self.queue_file = os.path.join(temp_dir, f"renpy_cmd_q_{id(self)}.txt")
                self.client_py = os.path.join(temp_dir, f"renpy_cmd_c_{id(self)}.py")

                with open(self.queue_file, "w", encoding="utf-8") as f:
                    pass

                client_code = (
                    "import sys, os, time\n"
                    "os.system('chcp 65001 >nul')\n"
                    "q_file = sys.argv[1]\n"
                    "pos = 0\n"
                    "while True:\n"
                    "    if not os.path.exists(q_file):\n"
                    "        break\n"
                    "    try:\n"
                    "        with open(q_file, 'r', encoding='utf-8') as f:\n"
                    "            f.seek(pos)\n"
                    "            lines = f.readlines()\n"
                    "            pos = f.tell()\n"
                    "        for raw in lines:\n"
                    "            line = raw.strip()\n"
                    "            if line == '__EXIT__':\n"
                    "                sys.exit(0)\n"
                    "            elif line == '__CLS__':\n"
                    "                os.system('cls')\n"
                    "            elif line.startswith('__COLOR__ '):\n"
                    "                os.system('color ' + line[10:])\n"
                    "            elif line.startswith('__TITLE__ '):\n"
                    "                os.system('title ' + line[10:])\n"
                    "            elif line.startswith('__ECHO__ '):\n"
                    "                print(line[9:])\n"
                    "    except Exception:\n"
                    "        pass\n"
                    "    time.sleep(0.05)\n"
                )

                with open(self.client_py, "w", encoding="utf-8") as f:
                    f.write(client_code)

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
                        [py_exe, self.client_py, self.queue_file],
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
                # 清理临时文件
                try:
                    import os
                    if self.queue_file and os.path.exists(self.queue_file):
                        os.remove(self.queue_file)
                    if self.client_py and os.path.exists(self.client_py):
                        os.remove(self.client_py)
                except Exception:
                    pass
