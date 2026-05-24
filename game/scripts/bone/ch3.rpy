label bone_ch3:
    scene black with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    $ renpy.notify("某个周末")
    pause 1.0

    scene bg group_photo with fade

    yangsy.comment "……所以[mc]到底是在什么时候进群的？"

    stop music fadeout 2.0

    $ renpy.notify("几周后")
    pause 1.0

    play music "audio/mus_setup.ogg" fadein 2.0

    "ACLC 逐渐步入正轨。\n[gra.nvl] 想给 ACLC 做个网站，于是委托会做这件事的 [baile.nvl] 和 [lv.nvl] 去建设。"

    "你时不时在群里看到他们讨论技术问题——\n什么框架、什么部署、什么域名解析——\n你听不太懂，但觉得他们很厉害。"

    yangsy.comment "这里可以选择跟建设网站的成员交谈，提高进线可能"

    "几天后，网站做好了。"

    "你点进去看了看。\n网站设计得很简洁——首页是成员作品展示，\n有教程区，有资源下载区。\n虽然简单，但看得出花了很多心思。"

    mc.nvl "好厉害"

    nvl clear

    "网站上线后，ACLC 的氛围更火热了。\n越来越多的人开始分享自己的魔改作品，讨论技术，交流心得。"
    "你看着群里一天比一天热闹，心里有一种说不出的满足感。"

    scene black with fade

    $ renpy.notify("ACLC 第一次群内魔改比赛")
    pause 1.0

    scene bg group_photo with fade

    "Gra 在群里宣布了一件大事："

    gra "我们搞个{s}魔改比赛{/s}吧"

    yangsy.comment "等会咱们也没搞过魔改比赛什么的啊\n按理来说不是应该让[mc]试做魔改吗"

    menu:
        "尝试":
            $ joined_contest = True
            

        "等待":
            $ joined_contest = False
            pass
            
    yangsy.comment "这里可以存个变量用于决定后续分支；\n首次尝试会导致游戏倾向于进入作者线"
    yangsy.comment "最终进什么线应该是多个选项变量综合而来的结果，且最好不是随机的"

    if joined_contest:
        "你开始构思自己的第一个魔改作品。\n虽然你还什么都不会，但你知道——\n这个群里会有人帮你。"
        yangsy "这也会提高进入帮助[mc]的人的线路的可能"

        $ renpy.notify("比赛当天")
        pause 1.0

        scene bg group_photo with fade

        "提交截止前的最后一小时，你终于完成了你的作品。\n虽然只是一个很简单的关卡修改，\n但在做出来的那一刻，你盯着屏幕看了很久。"

        mc "我做出来了……"

        "你把它发到了群里。"
        
        "虽然你的作品在那些大佬眼里可能还很稚嫩，\n但群友们的鼓励让你觉得——\n这就是你想要的感觉。"

    else:
        scene bg group_photo with fade

        "比赛当天，你看着大家一个个提交作品，\n默默地把它们一个个下载下来试玩。"
        "你心里想着：\n下一次，我也要参加。"

    stop music fadeout 3.0

    scene black with fade

    "比赛结束后，Gra 在群里说了一句话："

    gra "ACLC 才刚起步，以后还会有更多活动\n大家一起把这个社区做大吧"

    "那时你还不知道，这句话背后的分量有多重。"

    jump bone_ch4
