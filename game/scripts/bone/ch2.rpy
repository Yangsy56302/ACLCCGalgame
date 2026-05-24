label bone_ch2:
    scene black with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    "加入群聊后的头几天，你像一只刚进新家的猫——小心翼翼地观察着周围的一切。"

    nvl clear

    comment.nvl "大概就是所有群员全都欢迎一句；可以顺便加点互动"

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

    comment "Gra 是（待补）"
    "除了 Gra，群里还有一个人的发言风格让你印象深刻——Yangsy。\n她（待补）"

    scene black with fade

    $ renpy.notify("又过了几天")
    pause 1.0

    play music "audio/mus_setup.ogg" fadein 2.0

    "日子一天天过去，你在群里也渐渐混了个脸熟。\n你发现这个群的氛围很特别——"

    "大家不只是聊魔改。\n他们会聊日常，聊音乐，聊游戏，偶尔也会聊聊各自的烦恼。"
    "有时深夜，群里的消息会从技术讨论慢慢变成人生相谈。\n那些时候，你会觉得这群人虽然天南海北，却意外地亲近。"

    nvl clear

    comment "mwam（待补）"

    nvl clear

    comment "Morin（待补）"

    nvl clear

    "此时的你还觉得，这样的日子可以一直持续下去。\n你所不知道的是，命运——或者说是群聊——很快就要迎来第一次转折。"

    stop music fadeout 3.0

    scene black with fade

    jump bone_ch3
