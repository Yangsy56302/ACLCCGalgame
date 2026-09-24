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