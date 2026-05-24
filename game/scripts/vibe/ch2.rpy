label vibe_ch2:
    scene black with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    "加入群聊后的头几天，你像一只刚进新家的猫——小心翼翼地观察着周围的一切。"

    nvl clear

    gra.nvl "欢迎新人[[鼓掌]"
    mc.nvl "大家好，我是新来的[mc]，请多关照"
    yangsy.nvl "哦哦！新人！( ´▽｀)"
    morin.nvl "欢迎欢迎！"
    lv.nvl "欢迎。"
    baile.nvl "欢迎喵~"
    mwam.nvl "欢迎。"
    ashell.nvl "欢迎。"
    dwen.nvl "欢迎来到 Gra 的群"
    lingyun.nvl "欢迎。"
    lamb.nvl "嗨~"

    "消息一条接一条地弹出来。\n你还没来得及回复，就已经被淹没了。"

    mc.nvl "谢谢大家……人好多啊"

    gra.nvl "哈哈，习惯就好\n我们群虽然不大，但都很活跃"

    nvl clear

    "这就是你和这群人最初的相遇。\n那时候你还不知道，这些ID背后是一群什么样的人——\n也不知道，他们会在你的人生中留下怎样的印记。"

    scene black with fade
    stop music fadeout 2.0

    $ renpy.notify("几天后")
    pause 1.0

    play music "audio/mus_setup.ogg" fadein 2.0

    "几天下来，你逐渐摸清了群里的生态。"
    "Gra 是群主，也是群里的核心——她说话的时候，大家都会认真听。"
    "但平时她并不端架子，反而像个大姐头一样照顾着每个人。"

    gra "今天有人要听新曲子吗？我刚扒了一份谱"

    mc "什么曲子？"

    gra "《Astral Calm》——最近很迷这首"

    "Gra 分享了一段自己弹的钢琴录音。\n你点开听了，虽然只是手机录的，音质不算好，但那份细腻的情感却透过杂音传了过来。"

    mc "真好听……你自己扒的？"

    gra "嗯，听了几遍就差不多了 3\n喜欢的话以后可以多弹给你们听"

    nvl clear

    "除了 Gra，群里还有一个人的发言风格让你印象深刻——Yangsy。\n她说话永远带着引号，仿佛每句话都是在引用什么神秘语录。"

    yangsy "今天又做出来一个逆天的玩意儿 (￣▽￣)ノ"

    mc "什么逆天的玩意儿？"

    yangsy "一个把 Adofai 变成音游的魔改 (不是)"

    lv "等等，Adofai 本来就是音游吧"

    yangsy "那就是把音游变成另一个音游！"

    morin "你搁这套娃呢"

    "Yangsy 发了一段视频。\n你点开一看——画面里的关卡已经完全看不出原样了：\n轨道扭曲成螺旋形，节拍点变成了奇怪的图标，背景还在不断闪烁变色。"

    mc "这……这也能玩？"

    yangsy "能！而且我已经录了全连视频！ [[链接]"

    "你点开链接，看了完整通关视频。\n虽然画面离谱，但节奏竟然意外地对得上。\n你忍不住笑出了声。"

    mc "你是怎么做出来的？"

    yangsy "勇气 + 咖啡 + 深夜 + 一点点的 (消音)"

    gra "别听她瞎说 3\n你要是感兴趣，我可以教你基础"

    stop music fadeout 2.0

    "Gra 的这句话在你心里埋下了一颗种子。\n你当时只是含糊地应了一声，没有立刻回答。"

    scene black with fade

    $ renpy.notify("又过了几天")
    pause 1.0

    play music "audio/mus_setup.ogg" fadein 2.0

    "日子一天天过去，你在群里也渐渐混了个脸熟。\n你发现这个群的氛围很特别——"

    "大家不只是聊魔改。\n他们会聊日常，聊音乐，聊游戏，偶尔也会聊聊各自的烦恼。"
    "有时深夜，群里的消息会从技术讨论慢慢变成人生相谈。\n那些时候，你会觉得这群人虽然天南海北，却意外地亲近。"

    nvl clear

    mwam.nvl "……所以我说，那个谱面设计得就很离谱\n明明没踩音却放了个蓝键"

    mc.nvl "哈哈，确实\n你平时都做什么谱？"

    mwam.nvl "最近在给一首自制曲写谱\n不过还没找到合适的风格"

    morin.nvl "发来发来！我帮你看看！"

    mwam.nvl "……下次吧\n还没弄好"

    "mwam 话不多，但每次聊到谱面和音乐，她就会多说几句。\n你注意到，她似乎只在熟悉的话题上才会放得开。"

    nvl clear

    "而另一个极端是 Morin。\n她好像永远有用不完的精力，群里的大小活动几乎都是她组织的。"

    morin.nvl "大家！周末有没有人要联机打 Adofai！"

    baile.nvl "我报名喵~"

    lv.nvl "虽然我觉得联机打 Adofai 没什么意义……但我也来"

    yangsy.nvl "联机什么模式？比谁先被魔改吓哭吗 (´▽｀)"

    morin.nvl "就比谁通关快！简单粗暴！"

    nvl clear

    "你默默在群里打了个\"+1\"。\n那时候你觉得，这样的日子可以一直持续下去。\n你还不知道，命运——或者说是群聊——很快就要迎来第一次转折。"

    stop music fadeout 3.0

    scene black with fade

    jump vibe_ch3
