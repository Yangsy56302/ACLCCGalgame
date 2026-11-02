init python:
    is_debug_installed = True
    

style debug_menu_outer_frame is game_menu_outer_frame
style debug_menu_navigation_frame is game_menu_navigation_frame
style debug_menu_content_frame is game_menu_content_frame
style debug_menu_viewport is game_menu_viewport
style debug_menu_side is game_menu_side
style debug_menu_scrollbar is game_menu_scrollbar
style debug_menu_text is gui_text
style debug_menu_label is game_menu_label
style debug_menu_label_text is game_menu_label_text
style debug_menu_button is gui_button
style debug_menu_button_text is gui_button_text
style debug_menu_return_button is return_button
style debug_menu_return_button_text is return_button_text
style debug_menu_navigation_button is gui_button
style debug_menu_navigation_button_text is gui_button_text

style debug_text is gui_text
style debug_label is gui_label
style debug_label_text is gui_label_text
style debug_button is gui_button
style debug_button_text is gui_button_text
style debug_radio_button is radio_button
style debug_radio_button_text is radio_button_text
style debug_check_button is check_button
style debug_check_button_text is check_button_text

style debug_menu_text:
    font debug_gui_font
style debug_menu_label_text:
    font debug_gui_font
style debug_menu_button_text:
    font debug_gui_font
style debug_menu_return_button_text:
    font debug_gui_font
style debug_menu_navigation_button_text:
    font debug_gui_font
style debug_text:
    font debug_gui_font
style debug_label_text:
    font debug_gui_font
style debug_button_text:
    font debug_gui_font
style debug_radio_button_text:
    font debug_gui_font
style debug_check_button_text:
    font debug_gui_font


screen debug_screen():

    tag menu

    use game_menu(_("Debug Mode"), scroll="viewport"):

        vbox:
            style_prefix "debug"
        
            textbutton _("Disable Debug Mode") action Show("debug_confirm", None, _("Disable debug mode?"), yes_action=[SetVariable("persistent.debug_mode", False), Hide()], no_action=Hide())
            textbutton _("Unlock All Music") action Function(unlock_all_music)
            textbutton _("Unlock All CG") action Function(unlock_all_cg)
            textbutton _("Edit Variables...") action Show("per_variable")
            textbutton _("Clear Persistent Data") action Call("debug", "reset")
            if renpy.variant("pc"):
                textbutton _("Copy test file to Desktop") action Function(CopyToAnyway, "test/XS-X but delay event.zip", get_desktop_path() + "\\level file.zip")
                textbutton ("test debug console") action Call("test_console")
            elif renpy.variant("android"):
                textbutton _("Copy test file to Download") action Function(release_file_quietly, "test/XS-X but delay event.zip", "Download/ACLCCGame", "level file.zip")


screen debug_menu(title, scroll=None, yinitial=0.0):
    tag menu
    style_prefix "debug_menu"
    
    if main_menu:
        add gui.main_menu_background 
    else:
        add gui.game_menu_background 
    frame:
        style "debug_menu_outer_frame"
        hbox:
            frame:
                style "debug_menu_navigation_frame"

            frame:
                style "debug_menu_content_frame"
                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
    vbox:
        style_prefix "debug_menu_navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        if is_ingame:
            textbutton _("Variable") action ShowMenu("variable")

        textbutton _("Persistent Variable"):
            action ShowMenu("per_variable")

    textbutton _("Return"):
        style "return_button"
        action ShowMenu("debug_screen")
    
    label title


init python:
    def SetGameplayVariable(var, val):
        global variables
        variables[var] = val
    def SetPersistentVariable(var, val):
        global persistent
        persistent.variables[var] = val

    def unlock_all_music():
        for music_file in room_musics.values():
            renpy.mark_audio_seen(music_file)
        renpy.save_persistent()
        renpy.show_screen("debug_tip",("All music unlocked"))

    def unlock_all_cg():
        for group_images in gallery_images.values():
            for img in group_images:
                renpy.mark_image_seen(img)
        renpy.save_persistent()
        renpy.show_screen("debug_tip",("All CG unlocked"))

screen variable():
    tag menu
    use debug_menu("Variable"):
        vbox:
            style_prefix "debug"
            for var, val in variables.items():
                hbox:
                    label "[var]"
                    text ": [val]"
                hbox:
                    textbutton "None" action Function(SetGameplayVariable, var, None)
                    textbutton "True" action Function(SetGameplayVariable, var, True)
                    textbutton "False" action Function(SetGameplayVariable, var, False)

screen per_variable():
    tag menu
    use debug_menu("Persistent Variable"):
        vbox:
            style_prefix "debug"
            for var, val in persistent.variables.items():
                hbox:
                    label "[var]"
                    text ": [val]"
                hbox:
                    textbutton "None" action Function(SetPersistentVariable, var, None)
                    textbutton "True" action Function(SetPersistentVariable, var, True)
                    textbutton "False" action Function(SetPersistentVariable, var, False)


# label debug_unlock(Type):
#     nvl clear
#     debug "unlock: Now unlocking all [Type]{fast}{w=1.0}{nw}"
#     if Type == "CG":
#         scene bg home_midnight
#         scene bg home_night
#         scene bg home_noon
#         scene bg sbeam
#         scene bg sky
#         scene bg sky_night
#         scene bg star
#         scene bg that_video
#         scene black
#         debug "unlock: Success.{fast}{w=1.0}{nw}"
#     elif Type == "Music":
#         play music "mus_astral_calm.mp3"
#         play music "mus_aurora.mp3"
#         play music "mus_setup.ogg"
#         stop music
#         debug "unlock: Success.{fast}{w=1.0}{nw}"
#     else:
#         debug "unlock: Failed to find [Type]{fast}{w=1.0}{nw}"
#     if is_ingame:
#         return
#     else:
#         $ renpy.full_restart()


label debug(thing):
    if thing == "reset":
        nvl clear
        menu(nvl=True):
            debug "clean: Do you want to Clear All Persistent Data? (Y/N){fast}"
            "{font=MapleMono.otf}Yes{/font}":
                nvl clear
                debug "clean: Do you want to Clear All Persistent Data? (Y/N) Y{fast}{w=1.0}{nw}"
                debug "clean: Success.{fast}{w=1.0}{nw}"
                $ persistent._clear(progress=True)
            "{font=MapleMono.otf}No{/font}":
                nvl clear
                debug "clean: Do you want to Clear All Persistent Data? (Y/N) N{fast}{w=1.0}{nw}"
                pass
        $ persistent.debug_mode = True
    if is_ingame:
        return
    else:
        $ renpy.full_restart()


screen debug_confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5
                text_font debug_gui_font

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action text_font debug_gui_font
                textbutton _("No") action no_action text_font debug_gui_font


init python:
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

        def ShowText(self, text=""):
            """在窗口中展示文本内容"""
            if self.process is None or self.process.poll() is not None:
                self.Create()
            for line in str(text).splitlines():
                self._send_queue(f"__ECHO__ {line}")

        def Clear(self):
            """清空控制台窗口中的文本"""
            if self.process is None or self.process.poll() is not None:
                self.Create()
            self._send_queue("__CLS__")

        def Color(self, color_code="0A"):
            """修改窗口的背景与文字颜色 (cmd color 规范)"""
            if self.process is None or self.process.poll() is not None:
                self.Create()
            self._send_queue(f"__COLOR__ {color_code}")

        def Title(self, title_text=""):
            """修改控制台窗口的标题"""
            self.title = str(title_text)
            if self.process is None or self.process.poll() is not None:
                self.Create()
            self._send_queue(f"__TITLE__ {self.title}")

        def Break(self):
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



init -1 python:
    _active_cmd_consoles = []

label test_console:
    python:
        console = CmdWindow("DEBUG MODE")
        console.Create()
        console.Color("0A")
        console.Clear()
        console.ShowText("欢迎使用 RenPy 控制台！")
        console.ShowText("你可以在这里执行调试命令。")
    mwam.comment "控制台已弹出，点击继续以关闭控制台..."
    python:
        console.Break()
    return