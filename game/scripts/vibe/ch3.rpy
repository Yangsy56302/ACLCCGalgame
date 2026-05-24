label vibe_ch3:
    scene black with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    $ renpy.notify("某个周末")
    pause 1.0

    scene bg group_photo with fade

    "群里的消息突然比平时少了很多。\n你正觉得奇怪，就看到了 Gra 发的一条公告。"

    nvl clear

    gra.nvl "那个，我说个事[[严肃]"

    gra.nvl "这个群原本只是Yangsy随便建的聊天群\n但最近来的人越来越多了\n而且大家好像都是冲着魔改来的"

    gra.nvl "所以我打算分一个专门的群出来——\n关于 Adofai 魔改的讨论群"

    "消息发出去后，群里安静了几秒。\n然后炸了。"

    yangsy.nvl "哦哦哦！终于！ (≧▽≦)"

    morin.nvl "好耶！"

    lv.nvl "支持。是该有个专门的群了。"

    mc.nvl "我也支持\n不过新群叫什么？"

    gra.nvl "我想叫它——ACLC\n全称是 Adofai Cursed Level Community"

    nvl clear

    scene black with fade

    "{cps=*0.5}ACLC。{/cps}\n你默念着这个名字，心里有种莫名的兴奋感。\n这不再是一个普通的聊天群了——这是一个社区的开始。"

    pause 1.0

    scene bg group_photo with fade

    "很快，Gra 把新群建好了。\n大部分人都在第一时间加了过去。\n新群的界面干干净净的，群公告里只有一句话："

    gra "这里是 ACLC——Adofai Cursed Level Community\n欢迎所有热爱魔改的人"

    mc "简洁有力"

    yangsy "我能不能当管理员 (´･ω･`) "

    gra "不行 3"

    yangsy "好叭 ( ˘•ω•˘ ) "

    "你忍不住笑了。\n这个群和之前那个群最大的区别是——这里的每个人都是为了同一件事聚在一起的。"

    stop music fadeout 2.0

    $ renpy.notify("几周后")
    pause 1.0

    play music "audio/mus_setup.ogg" fadein 2.0

    "ACLC 逐渐步入正轨。\nbaile 主动提出要做一个网站。"

    baile "我可以搭一个 ACLC 的官网喵\n放一些教程和作品展示"

    gra "你还会做网站？"

    baile "稍微会一点喵……之前学过前端"

    lv "我可以帮忙后端"

    "于是 baile 和小绿君开始了网站的建设。\n你时不时在群里看到他们讨论技术问题——\n什么框架、什么部署、什么域名解析——\n你听不太懂，但觉得他们很厉害。"

    nvl clear

    mc.nvl "网站大概什么时候能好？"

    baile.nvl "快了喵……已经差不多了"

    lv.nvl "嗯，主要是域名解析等生效"

    "几天后，baile 在群里发了一个链接：aclc.top"

    baile.nvl "做好了喵~"

    "你点进去看了看。\n网站设计得很简洁——首页是成员作品展示，\n有教程区，有资源下载区。\n虽然简单，但看得出花了很多心思。"

    mc.nvl "好厉害"

    gra.nvl "辛苦了！"

    yangsy.nvl "我的作品要放首页！ (｀・ω・´)"

    baile.nvl "放了的喵~你自己去看"

    nvl clear

    "网站上线后，ACLC 的氛围更火热了。\n越来越多的人开始分享自己的魔改作品，\n讨论技术，交流心得。\n你看着群里一天比一天热闹，心里有一种说不出的满足感。"

    scene black with fade

    $ renpy.notify("ACLC 第一次群内魔改比赛")
    pause 1.0

    scene bg group_photo with fade

    "Gra 在群里宣布了一件大事："

    gra "我们搞个魔改比赛吧"

    morin "好！！我等这句话好久了！"

    yangsy "奖品是什么 (´▽｀)"

    gra "奖品是……荣誉 3\n还有 ACLC 网站首页推荐位"

    lv "这奖励很诱人了"

    mc "对我这种新人友好吗？"

    gra "分新手组和老手组\n所以你也可以参加"

    "你犹豫了一下。\n你确实想试试，但你又觉得自己什么都不懂。"

    menu:
        "参加比赛":
            $ joined_contest = True
            mc "行，我参加"

            gra "好！期待你的作品 3"

            yangsy "对手出现了！ (๑•̀ㅂ•́)و✧"

            morin "人家新人组，你激动啥"

            yangsy "新人也可能是黑马！"

        "先看看":
            $ joined_contest = False
            mc "我还是先看看吧……等下次"

            gra "没问题，先看看大家的作品也能学到很多东西"

    nvl clear

    "比赛的消息在群里掀起了一阵热潮。\n每个人都在讨论自己要做什么主题。\n你发现，当你真正身处一个充满创造力的环境中时，\n连空气都在微微发烫。"

    if joined_contest:
        "你开始构思自己的第一个魔改作品。\n虽然你还什么都不会，但你知道——\n这个群里会有人帮你。"

    $ renpy.notify("比赛当天")
    pause 1.0

    if joined_contest:
        scene bg group_photo with fade

        "提交截止前的最后一小时，你终于完成了你的作品。\n虽然只是一个很简单的关卡修改，\n但在做出来的那一刻，你盯着屏幕看了很久。"

        mc "我做出来了……"

        "你把它发到了群里。"

        gra "！ 新人交作品了！"

        morin "来鉴赏一下！"

        yangsy "我看看…… 嗯…… 卧槽 这个设计有点意思"

        "虽然你的作品在那些大佬眼里可能还很稚嫩，\n但群友们的鼓励让你觉得——\n这就是你想要的感觉。"

    else:
        scene bg group_photo with fade

        "比赛当天，你看着大家一个个提交作品。\nYangsy 做了一个让人瞠目结舌的扭曲关卡，\nlv 做了一个技术力极高的特效作品，\n就连 Morin 也交了一份让人眼前一亮的作品。\n你默默地把它们一个个下载下来试玩，\n心里想着：下一次，我也要参加。"

    stop music fadeout 3.0

    scene black with fade

    "比赛结束后，Gra 在群里说了一句话："

    gra "ACLC 才刚起步，以后还会有更多活动\n大家一起把这个社区做大吧"

    "那时你还不知道，这句话背后的分量有多重。"

    jump vibe_ch4
