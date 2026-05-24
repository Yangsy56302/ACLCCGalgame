label bone_ch11:
    scene black with fade

    play music "audio/mus_astral_calm.mp3" fadein 3.0

    $ renpy.notify("深圳电玩节 / Manka Life")
    pause 1.0

    "消息是两个群里同时传开的。\n有人发现深圳电玩节和 Manka Life 有魔改相关的展位。\n更让人意外的是——ACLCC 有机会在线下展示作品。"

    "这个消息像一颗投入湖面的石子。\n线上聊了那么久的人——\n终于要在线下见面了。"

    "当然，不是所有人都有条件去。\n你在心里盘算了一下自己的时间和距离。"

    menu:
        "我要去":
            $ go_to_expo = True
            mc "我去。\n难得有机会，不能错过"

            lv "好，我记一下"

        "这次去不了":
            $ go_to_expo = False
            mc "我这次去不了……\n时间有点紧"

            lv "没事，以后还有机会"

    nvl clear

    scene black with fade

    "出发前的那段时间，群里充满了期待和紧张。"

    "mwam 在反复确认自己要展示的谱面，\nlv 在调试设备，\nMorin 在群里发了一百条消息问穿什么衣服。"

    "你发现，屏幕后面那些熟悉的名字，\n突然变得真实了起来。"

    if go_to_expo:
        scene bg group_photo with fade
        play music "audio/mus_setup.ogg" fadein 2.0

        "展会当天。"

        yangsy.nvl "直接重写得了（"

    else:
        scene bg group_photo with fade
        play music "audio/mus_setup.ogg" fadein 2.0

        "虽然没有去现场，但你一直守在手机前。\n群里的消息像直播一样不断刷屏。"

        "你看着那些消息，\n虽然不在现场，\n但你能想象出那个画面。"

    yangsy.nvl "或许这段剧情也可以用于[name_mc]向部分被攻略的角色表白？"

    nvl clear

    scene black with fade
    stop music fadeout 3.0

    "展会结束了。\n线上和线下的世界在这一天短暂地重叠，\n然后又分开。"

    "但有一些事情已经不一样了。"

    "在这段旅程中，你遇到了这群人。\n他们有的人还在你身边，有的人也还在你身边。"

    yangsy "而有的{s}人——{s}{nw}"
    yangsy "而有的缝合怪，在吐槽（"
    
    "但无论怎样，\n你已经不再是当初那个刚刚点进视频的旁观者了。"

    "故事走到了一个岔路口。\n你还想继续走下去——\n但往哪个方向走，你已不再迷茫。"

    yangsy "如果之前没有插入攻略线分支的话，在此插入攻略线分支（其实有些可以更早分支？"

    jump bone_epilogue