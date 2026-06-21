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
                        call chex_unknown_oi from _call_chex_unknown_oi
                    "chex_unknown_baile_lefthanded":
                        call chex_unknown_baile_lefthanded from _call_chex_unknown_baile_lefthanded
                    "返回":
                        pass
            "查看[yoosee]的建议":
                call chplotadvice_yoosee from _call_chplotadvice_yoosee
            "查看[yangsy]的建议":
                call chplotadvice_yangsy from _call_chplotadvice_yangsy
            # "查看测试（chtest）":
            #     call chtest
            "返回主菜单":
                return

image splash = "splash.png"
image attention = "attention.png"
label splashscreen: 
    call request_manage_storage from _call_request_manage_storage
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

    def CopyToAnyway(filename, dest_filename):

        if not renpy.loadable(filename):
            renpy.notify("❌ 错误：未找到文件 '{}'，请检查路径。".format(filename))
            return

        # 只取文件名，防止路径里有奇怪的斜杠
        base_name = os.path.basename(filename)
        target_path = os.path.join(dest_filename)

        try:
            # 3. 核心步骤：从 Ren'Py 虚拟文件系统（含 RPA）读取文件字节流
            # 分块读取（防止大文件内存溢出）
            with renpy.file(filename) as f:
                with open(target_path, "wb") as out_file:
                    while True:
                        chunk = f.read(8192)  # 每次读 8KB
                        if not chunk:
                            break
                        out_file.write(chunk)
            
            renpy.show_screen("copy_tip", "已将文件保存至 \""+target_path+"\"")

        except Exception as e:
            renpy.show_screen("copy_tip", "保存失败：{}".format(str(e)))

init python:
    if renpy.android:
        import jnius
        mActivity = jnius.autoclass("org.renpy.android.PythonSDLActivity").mActivity
    else:
        mActivity = None

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