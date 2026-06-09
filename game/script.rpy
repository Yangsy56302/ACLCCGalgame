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
    
    names = ["祐荽", "Yangsy56302", "小绿君", "飞雨凌云", "莫邪Morin", "ms_win_and_mc", "是动听D温呐", "晴柚-Grafrustix", "TheHale", "终究是摆了", "阿希尔Ashell", "myworldzycpc"]
