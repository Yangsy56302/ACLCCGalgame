# The game starts here.
label start:
    call naming from _call_naming
    call ch0 from _call_ch0

    # yoosee '不用照搬历史\n确定人物性格和故事走向就行'

    # '事件：深圳电玩节\n事件：Manka Life'

    # yoosee '漫展之后就从主线过渡到各个人物线上了\n所以主角是在这里要确定发展关系'
    # yangsy '可不可以每一次都进一部分可攻略角色的线（\n别一次漫展世界线就全岔开了（'
    # yoosee '看情况'
    # yoosee '有的可能第一次就可以\n有的要第一次触发一些事件\n也可以比如第二次的时候没有触发条件就会断线这样'

    # yoosee '总体可以分为普通线，作者线，攻略线三种'
    # yoosee '普通线就是正常爱好者\n但是更偏向于普通玩家而不是深入魔改圈'
    # yoosee '作者线就是成为魔改作者这样'
    # yoosee '然后作者线也可以出发{sic}一些攻略角色'
    # yoosee '攻略线更侧重感情'
    # yoosee '魔改用于增添风味（）'

    return


label naming_loop:
    "Name the main character.{nw}"
    $ name_mc = renpy.input(_("Name the main character.{fast}"), length=56).strip()
    if not name_mc:
        "You must choose a name."
        jump naming_loop
    # elif any(name_mc.lower() in n for n in ["ashell", "阿希尔"]):
    #     character.ashell('大概是取名彩蛋对话啥的')
    #     jump naming_loop
    # elif name_mc.lower() == "你的名字":
    #     name_mc = "韦一敏"
    mc "Is this name correct?{nw}"
    menu:
        mc "Is this name correct?{fast}"
        "Yes":
            $ persistent.name_mc = name_mc
            return
        "No":
            jump naming_loop


label naming:
    scene black with fade

    if persistent.name_mc:
        $ name_mc = persistent.name_mc
        mc "A name has already been chosen."
    else:
        call naming_loop
    
    scene black with fade
    return


label chtest:
    menu:
        '?'
        '0':
            pass
        '1':
            pass
        '2':
            pass
        '3':
            pass
    return