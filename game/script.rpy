# The game starts here.
label start:
    $ is_ingame = True
    stop music

    default has_phone = False

    call setup_naming_start from _call_setup_naming_start
    $ renpy.block_rollback()
    call ch0 from _call_ch0

    return

label to_be_continued(chp):
    
    stop music fadeout 1.0
    scene black with dissolve
    
    while True:
        menu:
            "查看第一章剧情" if chp == "ch0":
                jump ch1
            "查看已被废弃的AI剧情":
                jump vibe_ch2
            "查看游离的支线章节":
                menu:
                    "chex_unknown_oi":
                        call chex_unknown_oi
                    "chex_unknown_baile_lefthanded":
                        call chex_unknown_baile_lefthanded
                    "返回":
                        pass
            "查看[yoosee]的建议":
                call chplotadvice_yoosee
            "查看[yangsy]的建议":
                call chplotadvice_yangsy
            # "查看测试（chtest）":
            #     call chtest
            "返回主菜单":
                return

image splash = "splash.png"
image attention = "attention.png"
label splashscreen: 
    
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

init 999 python:
    if not is_debug_installed:
        persistent.debug_mode = False

init -999 python:
    class Continue(Action):
        def __call__(self):
            newest_page, newest_name = self.get_newest_slot()
            FileLoad(newest_name, confirm = False, page = newest_page)()

        def get_sensitive(self):
            if not renpy.newest_slot():
                return False

            newest_page, newest_name = self.get_newest_slot()

            if newest_page == '_reload':
                return False

            return FileLoadable(newest_name, page=newest_page)

        def get_newest_slot(self):
            newest = renpy.newest_slot()

            if newest:
                page, name = newest.split("-")
                return page, name
    is_debug_installed = False
    names = ["祐荽","Yangsy56302","小绿君","飞雨凌云","莫邪Morin","ms_win_and_mc",
            "是动听D温呐","晴柚-Grafrustix","TheHale","终究是摆了","阿希尔Ashell",
            "myworldzycpc","李星眠","晴安柚子","凌云","莫邪","李婉清","杨曦","小绿草",
            "MaoYuNa133","怃","Pumi","UNI","Happylamb029"]

init python:
    import os
    import shutil
    import sys

    def get_desktop_path():
        """获取当前用户的真实桌面路径（支持Windows重定向）"""
        if renpy.windows:
            # 优先读取注册表
            try:
                import winreg
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                    r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
                desktop, _ = winreg.QueryValueEx(key, "Desktop")
                winreg.CloseKey(key)
                # 如果路径包含 %USERPROFILE% 环境变量，需要展开
                desktop = os.path.expandvars(desktop)
                if os.path.isdir(desktop):
                    return desktop
            except Exception:
                pass
            # 备用：通过环境变量
            profile = os.environ.get("USERPROFILE")
            if profile:
                candidate = os.path.join(profile, "Desktop")
                if os.path.isdir(candidate):
                    return candidate
        # 非Windows或上述都失败：用默认方法
        return os.path.expanduser("~/Desktop")

    def CopyToAnyway(source_rel_path, dest_filename):

        src = os.path.join(source_rel_path)
        dst = os.path.join(dest_filename)

        if not os.path.exists(src):
            renpy.notify(f"源文件不存在: {source_rel_path}")
            return

        try:
            shutil.copy2(src, dst)
            renpy.notify(f"已保存到: {dst}")
        except Exception as e:
            renpy.notify(f"保存失败: {e}")