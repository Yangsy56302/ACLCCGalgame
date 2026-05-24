label vibe_ch9:
    scene black with fade

    "ACLC 解散后的日子，像一潭死水。"

    '你每天还是会习惯性地打开 QQ，\n点开那个已经不复存在的群聊——\n只是为了看到那条"群聊已被解散"的提示。'

    "你也不知道自己为什么要这么做。\n也许是为了提醒自己，它真的存在过。"

    nvl clear

    "直到有一天，你收到了一条私聊。"

    lv.nvl "# ……在吗？"

    mc.nvl "在"

    lv.nvl "# 我想重建 ACLC"

    "你愣住了。"

    mc.nvl "你说真的？"

    lv.nvl "# 真的\n# 我不甘心就这么结束了"

    mc.nvl "但是……Gra 她……"

    lv.nvl "# Gra 那边我会去说\n# 但我觉得这个社区应该继续存在\n# 哪怕换一个名字，换一种方式"

    nvl clear

    '小绿君的话让你沉默了很久。\n你想起杨曦退群前的那句话——\n"也许我本来就不该做魔改"'

    "但你又想起更多——\n那些深夜里的笑声，第一次发表作品时的成就感"

    "听到 mwam 的曲子时的震撼，\n和 baile 一起看星星时的宁静……"

    menu:
        "我愿意帮你重建":
            mc "需要我做什么？"

            lv "# 先帮我联系一下大家吧\n# 看看还有多少人愿意回来"

            $ helped_rebuild = True

        "我需要想想……":
            mc "让我想想……"

            lv "# 嗯\n# 想好了告诉我"

            $ helped_rebuild = False

    nvl clear

    scene black with fade
    pause 1.0

    play music "audio/mus_aurora.mp3" fadein 3.0
    $ renpy.notify("♪ ms_win_and_mc - Aurora (Full Ver.)")
    "几天后，一个新的群聊出现在你的群列表里。"

    "群名：ACLC (CN)"
    "群号：和以前不一样了。\n但群成员列表里，那些熟悉的名字一个接一个地重新出现。"

    nvl clear

    "小绿君在空荡荡的新群里发了一条消息："

    lv.nvl "# 我回来啦"

    "然后——"

    morin.nvl "来啦！"

    baile.nvl "来了喵~"

    dwen.nvl "~ 我还在 ~"

    ashell.nvl "嗯。"

    lingyun.nvl "我也在。"

    lamb.nvl "嗨~"

    mwam.nvl "……我也回来了"

    nvl clear

    "你看着那些熟悉的名字一个一个出现。\n明明只是几行文字，\n却让你鼻子有点发酸。"

    if helped_rebuild:
        "你也在群里发了消息："
        mc.nvl "我也在"
        lv.nvl "# 欢迎回来"

    "但有两个人的名字一直没有出现。"

    "Gra。Yangsy。"

    "你知道，她们也许不会再回来了。"

    stop music fadeout 3.0

    scene black with fade

    "ACLC 死了。\n但 ACLC (CN)——简称 ACLCC——活了。"

    "虽然它还很小，很脆弱，\n像废墟上刚刚冒出来的嫩芽。\n但它在呼吸。"

    pause 1.0

    jump vibe_ch10
