label bone_ch4:
    scene black with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    "日子像流水一样过去。\nACLC 的日常渐渐有了固定的节奏——"

    "白天大家各自忙各自的事情，\n到了晚上群里的消息就开始热闹起来。\n有人发作品，有人求指导，有人纯粹在吹水。"

    "你也逐渐找到了自己在群里的位置。"

    nvl clear

    yangsy "回答合适的答案，会提高进线可能"

    if joined_contest:
        "那次比赛之后，你对魔改的兴趣越来越浓。\n你开始在群里问一些基础问题，\n[gra.nvl] 和 [yangsy.nvl] 都很热心地回答你。"

    else:
        "虽然没有参加比赛，但你也没闲着。\n你开始认真学习魔改制作的教程——\[baile.nvl] 的网站上就有不少入门资料。"

    nvl clear

    scene bg group_photo with fade

    "这天晚上，群里像往常一样热闹。\n但有一件事让你的印象特别深——"

    "mwam 在群里分享了一首她新做的曲子。"

    yangsy "？"
    yangsy "设定里也没说[mwam.nvl]会作曲啊？"

    "mwam 在群里分享了一首她新做的谱子。"
    
    yangsy "这下好多了（"

    "你注意到，mwam 虽然被夸了，但并没有表现出特别高兴的样子。\n她只是简单地道了谢，然后继续埋头修改她的作品。"

    nvl clear

    yangsy "举个例子（不一定要实装），这里选择【关心一下】是进[mwam]线的必要条件："

    menu:
        "你决定："
        "关心一下":

            "后来你私下问她为什么看起来不太开心。\n她沉默了很久，才回复你——"

            mwam.nvl "我只是……不太习惯被夸"

            mc.nvl "为什么？你明明做得很好"

            mwam.nvl "嗯……可能因为我自己总觉得不够好吧\n每次做完一首曲子，隔一段时间再听\n就能听出一堆毛病"

            mc.nvl "那就改到满意为止"

            mwam.nvl "……嗯\n谢谢"

            nvl clear

            "那是你第一次觉得，这些每天在群里嘻嘻哈哈的人，\n其实每个人都有自己的故事。"
            "只是平时，他们把这些故事藏在了表情包和玩笑话背后。"

        "漠不关心":
            "你决定不再细想啥的（"

    scene black with fade

    $ renpy.notify("一个深夜")
    pause 2.0

    play music "audio/mus_aurora.mp3" fadein 2.0
    $ renpy.notify("♪ ms_win_and_mc - Aurora (Full Ver.)")
    "群里的消息渐渐安静了下来。\n你正准备关手机睡觉，却收到了 baile 的私聊。"

    baile "看星星"

    scene black with fade

    "你关掉手机，躺在床上。\n窗外的夜空一片漆黑——\n城市的灯光太亮了，看不到星星。\n但你莫名觉得，今晚的夜空格外好看。"

    stop music fadeout 3.0

    $ renpy.notify("第二天")
    pause 1.0

    scene bg group_photo with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    "第二天，群里又恢复了往日的热闹。\n你看着那些熟悉的 ID 在刷屏，\n心里有一种奇妙的充实感。"

    "ACLC 已经不再只是一个群了。\n对这里的很多人来说——\n包括你——它已经成了生活中不可或缺的一部分。"

    nvl clear

    "但与此同时，你也在思考一个问题：\n你在这个社区里，想成为什么样的人？"

    yangsy "这里就别让玩家手动选了（"
    yangsy "游戏应该根据之前的选择决定让[name_mc]进入作者线还是普通线"
    yangsy "两条线能攻略的人也不同——\n作者线能攻略的主要是魔改作者，\n普通线能攻略的主要是不是魔改作者的成员"
    yangsy "攻略线或许应该作为作者线和普通线的下游分支？()"
    yangsy "以及现在做选择可能有些早？\n有可能只是因为之前的剧情体量不够{...}"

    menu:

        "（如果之前主要跟魔改作者讨论）":
            $ current_route = "creator"
            mc "我想试着做魔改……不是随便玩玩的那种\n我想做出真正属于自己的作品"

            "从这一天起，你的 ACLC 生活有了新的方向。\n你不知道自己能走到哪一步，但你知道——\n至少你不会后悔这个决定。"

        "（如果之前主要跟其他成员讨论）":
            $ current_route = "normal"
            mc "我觉得……我可能更适合做一个支持者\n看看大家的作品，帮忙宣传一下就好"

            "从这一天起，你找到了自己在 ACLC 的位置。\n也许你写不出一行魔改代码，\n但你可以在其他方面让这个社区变得更好。"

    nvl clear

    scene black with fade

    "[name_mc]（不是玩家）做出了选择（不是点击选项）。\n无论选了哪条路，你都知道——\n这只是个开始。"

    jump bone_ch5
