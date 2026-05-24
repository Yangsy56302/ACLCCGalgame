# The game starts here.
label start:
    stop music

    default has_phone = False


    # jump chtest

    call guide_naming_start from _call_guide_naming_start
    $ renpy.block_rollback()
    call ch0 from _call_ch0

    return


label chtest:
    
    show yangsy zorder 2 at t41
    show gra zorder 2 at t11
    show mwam angry zorder 2 at t43
    show morin zorder 2 at t44
    show baile zorder 3 at t42
    ""

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
