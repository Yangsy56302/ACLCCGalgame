label vibe_ch4:
    scene black with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    "日子像流水一样过去。\nACLC 的日常渐渐有了固定的节奏——"

    "白天大家各自忙各自的事情，\n到了晚上群里的消息就开始热闹起来。\n有人发作品，有人求指导，有人纯粹在吹水。"

    "你也逐渐找到了自己在群里的位置。"

    nvl clear

    if joined_contest:
        "那次比赛之后，你对魔改的兴趣越来越浓。\n你开始在群里问一些基础问题，\nGra 和 Yangsy 都很热心地回答你。"

        mc.nvl "Gra，我想问你个问题……\n那个轨道扭曲的效果是怎么做的？"

        gra.nvl "那个啊，是改的配置文件里的曲线参数\n你把 spline 那一段的数值调一下就行"

        yangsy.nvl "\" 或者你也可以直接复制我的模板 (小声) \""

        gra.nvl "别教坏新人 3"

    else:
        "虽然没有参加比赛，但你也没闲着。\n你开始认真学习魔改制作的教程——\nbaile 的网站上就有不少入门资料。"

        mc.nvl "baile，你网站的教程是你自己写的吗？"

        baile.nvl "大部分是喵……\nlv 也帮了一些忙"

        mc.nvl "写得很好懂，谢谢你"

        baile.nvl "不客气喵~ 能帮到你就好"

    nvl clear

    scene bg group_photo with fade

    "这天晚上，群里像往常一样热闹。\n但有一件事让你的印象特别深——"

    "mwam 在群里分享了一首她新做的曲子。"

    mwam "我做了一首新的……你们听听看"

    "她发来一个音频文件。\n你戴上耳机，点下了播放键。"

    # TODO: 播放 mwam 的原创曲（需要实际音频文件）
    # play music "audio/mus_mwam_original.ogg" fadein 2.0

    "前奏响起的瞬间，你起了一身鸡皮疙瘩。\n那是一首节奏感很强的电子乐，\n旋律里带着一种说不出的空灵感。"

    mc "……这是你写的？"

    mwam "嗯……给一个魔改关卡配的"

    gra "太好听了吧！"

    yangsy "\" 大佬请收下我的膝盖 (´;ω;`) \""

    morin "放到你网站上啊！我要下载！"

    mwam "我再修一修……还没做完"

    "你注意到，mwam 虽然被夸了，但并没有表现出特别高兴的样子。\n她只是简单地道了谢，然后继续埋头修改她的作品。"

    nvl clear

    "后来你私下问她为什么看起来不太开心。\n她沉默了很久，才回复你——"

    mwam.nvl "我只是……不太习惯被夸"

    mc.nvl "为什么？你明明做得很好"

    mwam.nvl "嗯……可能因为我自己总觉得不够好吧\n每次做完一首曲子，隔一段时间再听\n就能听出一堆毛病"

    mc.nvl "那就改到满意为止"

    mwam.nvl "……嗯\n谢谢"

    nvl clear

    "那是你第一次觉得，这些每天在群里嘻嘻哈哈的人，\n其实每个人都有自己的故事。"
    "只是平时，他们把这些故事藏在了表情包和玩笑话背后。"

    scene black with fade

    $ renpy.notify("一个深夜")
    pause 2.0

    play music "audio/mus_aurora.mp3" fadein 2.0
    $ renpy.notify("♪ ms_win_and_mc - Aurora (Full Ver.)")
    "群里的消息渐渐安静了下来。\n你正准备关手机睡觉，却收到了 baile 的私聊。"

    baile "你睡了吗喵？"

    mc "还没，怎么了？"

    baile "要不要出来看星星喵\n今晚的星星特别好看"

    "你愣了一下。\n你和 baile 虽然已经在群里很熟了，\n但这是她第一次私聊你。"

    mc "你在哪？"

    baile "我家天台喵\n我给你拍张照"

    "她发来一张照片。\n深蓝色的夜空里，星星密密麻麻地铺展开来，\n像撒了一把碎钻石。"

    mc "好漂亮"

    baile "我最喜欢看星星喵\n每次心情不好的时候，就上来看看"

    mc "你今天心情不好？"

    baile "……有一点"

    "你没有追问为什么。\n你只是和她一起，隔着屏幕看着同一片星空。\n偶尔她会告诉你哪颗是北极星，哪颗是天狼星。"

    baile "你知道吗喵\nOI 的题目做不出来的时候\n我就看看星星\n然后就会觉得——宇宙这么大，做不出来一道题也没什么"

    mc "哈哈，这心态不错"

    baile "你要记住喵\n以后遇到困难的时候\n抬头看看星星就好"

    stop music fadeout 3.0

    scene black with fade

    "你关掉手机，躺在床上。\n窗外的夜空一片漆黑——\n城市的灯光太亮了，看不到星星。\n但你莫名觉得，今晚的夜空格外好看。"

    $ renpy.notify("第二天")
    pause 1.0

    scene bg group_photo with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    "第二天，群里又恢复了往日的热闹。\n你看着那些熟悉的 ID 在刷屏，\n心里有一种奇妙的充实感。"

    "ACLC 已经不再只是一个群了。\n对这里的很多人来说——\n包括你——它已经成了生活中不可或缺的一部分。"

    nvl clear

    "但与此同时，你也在思考一个问题：\n你在这个社区里，想成为什么样的人？"

    menu:
        "我想成为一个创作者——做出属于自己的魔改作品":
            $ vibe_route_creator = True
            $ vibe_route_normal = False
            mc "我想试着做魔改……不是随便玩玩的那种\n我想做出真正属于自己的作品"

            gra "这个想法不错 3\n如果你认真想学，我可以系统地教你"

            yangsy "\" 哦哦！新人要入坑了！ (ﾉ≧∀≦)ﾉ \""

            mc "那就拜托了"

            "从这一天起，你的 ACLC 生活有了新的方向。\n你不知道自己能走到哪一步，但你知道——\n至少你不会后悔这个决定。"

        "我想好好享受这个社区——和大家在一起就够了":
            $ vibe_route_creator = False
            $ vibe_route_normal = True
            mc "我觉得……我可能更适合做一个支持者\n看看大家的作品，帮忙宣传一下就好"

            gra "那也很好啊 3\n一个社区不只有创作者"

            morin "对！没有观众的话，作品也只是自嗨嘛"

            yangsy "\" 那你就是我们的头号粉丝了 (´▽｀) \""

            mc "哈哈，那就这么定了"

            "从这一天起，你找到了自己在 ACLC 的位置。\n也许你写不出一行魔改代码，\n但你可以在其他方面让这个社区变得更好。"

    nvl clear

    scene black with fade

    "你做出了选择。\n无论选了哪条路，你都知道——\n这只是个开始。"

    jump vibe_ch5
