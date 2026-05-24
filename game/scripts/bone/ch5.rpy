label bone_ch5:
    scene black with fade

    $ renpy.notify("几个月后")
    pause 2.0

    scene bg group_photo with fade
    play music "audio/mus_astral_calm.mp3" fadein 3.0
    $ renpy.notify("♪ ms_win_and_mc - Astral Calm")
    "ACLC 在几个月里成长了很多。\n新成员源源不断地加入，\n群里的消息记录一天比一天长。"

    "baile 的网站访问量也在稳步上升。\n偶尔会有陌生人来群里说\n\"我是从 aclc.top 找到你们的\"。"

    "据传，甚至还有几个国外的魔改作者联系交流。"

    "这个消息在群里引起了不小的震动。\n以前魔改只是一个小圈子的自娱自乐，\n现在，它开始走向更广阔的视野了。"

    yangsy.nvl "那我们也该有个英文名了叭 (´･ω･`)"

    gra.nvl "早就有了——ACLC 本身就是英文名"

    yangsy.nvl "不！我说的是国际版！像 ACLGlobal 之类的！"

    lv.nvl "……以后再说吧"

    scene black with fade
    stop music fadeout 2.0

    $ renpy.notify("几天后，Yangsy 的直播间")
    pause 1.0

    play music "audio/mus_setup.ogg" fadein 2.0

    "Yangsy 在群里发了一个直播间链接。"

    yangsy "？"
    yangsy "不是哥们 Yangsy怎么不记得Yangsy直播过"

    "她语气里有那么一丝不甘。"
    
    yangsy "差不多得了嗷（"

    nvl clear

    stop music fadeout 3.0

    scene black with fade

    jump bone_ch6
