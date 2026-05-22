# The game starts here.
label start:
    stop music

    # jump chtest

    call guide_naming_start from _call_guide_naming_start
    $ renpy.block_rollback()
    call ch0 from _call_ch0

    yoosee "不用照搬历史\n确定人物性格和故事走向就行"

    "事件：深圳电玩节\n事件：Manka Life"

    yoosee "漫展之后就从主线过渡到各个人物线上了\n所以主角是在这里要确定发展关系"
    yangsy "可不可以每一次都进一部分可攻略角色的线（\n别一次漫展世界线就全岔开了（"
    yoosee "看情况"
    yoosee "有的可能第一次就可以\n有的要第一次触发一些事件\n也可以比如第二次的时候没有触发条件就会断线这样"

    yoosee "总体可以分为普通线，作者线，攻略线三种"
    yoosee "普通线就是正常爱好者\n但是更偏向于普通玩家而不是深入魔改圈"
    yoosee "作者线就是成为魔改作者这样"
    yoosee "然后作者线也可以出发一些攻略角色"
    yoosee "攻略线更侧重感情"
    yoosee "魔改用于增添风味（）"

    scene black with dissolve
    return


label chtest:
    
    show yangsy flirt zorder 2 at t41
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

        def  get_newest_slot(self):
            newest = renpy.newest_slot()

            if newest:
                page, name = newest.split("-")
                return page, name
    
    names = ["祐荽", "Yangsy56302", "小绿君", "飞雨凌云", "莫邪Morin", "ms_win_and_mc", "是动听D温呐", "晴柚-Grafrustix", "TheHale", "终究是摆了", "阿希尔Ashell", "myworldzycpc"]