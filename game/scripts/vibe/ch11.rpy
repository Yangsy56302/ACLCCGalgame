label vibe_ch11:
    scene black with fade

    play music "audio/mus_astral_calm.mp3"

    $ renpy.notify("深圳电玩节 / Manka Life")
    pause 1.0

    "消息是两个群里同时传开的。\n有人发现深圳电玩节和 Manka Life 有魔改相关的展位。\n更让人意外的是——ACLCC 有机会在线下展示作品。"

    nvl clear

    lv.nvl "我收到了主办方的邀请\n# 他们想找一些魔改作者做线下展示"

    morin.nvl "好耶！！线下聚会！"

    baile.nvl "真的吗喵！"

    lv.nvl "真的\n# 主办方说想展示 Adofai 的社区创作生态"

    nvl clear

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

        "你站在场馆门口，看着来来往往的人群。\n手里攥着手机，群里的消息一条一条跳出来："

        lv "我到了，在北门"

        morin "我也到了！！你们在哪！"

        baile "我在找一个很高的柱子喵……"

        "你穿过人群，寻找那些你只在屏幕上看过的脸。\n这种感觉很奇妙——"
        
        "你知道他们的名字，了解他们的性格，\n但你从未亲眼见过他们。"

        "然后你看到了一个白发的女孩。\n她站在柱子旁边，东张西望，\n白色的猫耳发饰在阳光下微微晃动。"

        "是 baile。"

        "她看到你的第一反应是愣住了。\n然后她歪了歪头——"

        baile "[mc]喵？"

        mc "……是我"

        baile "哇……你比我想象的要高喵"

        "说完，她不好意思地笑了笑。"

        $ baile.meet_irl = True

        nvl clear

        "接下来，你陆续见到了其他人。"

        "lv 比你想象中要沉稳得多，\n他戴着眼镜，话不多，但每句都在点子上。"

        "Morin 的能量在线下毫不衰减。\n她穿着一件亮色的卫衣，\n远远地就开始挥手。"

        "mwam 是最后到的。\n她低着头走进场馆，"
        
        "看到你们之后，犹豫了一下才走过来。"

        mwam "……大家好"

        "她的声音比线上要小得多。\n但你注意到，当你们开始聊起音乐和谱面时，"
        
        "她的话渐渐多了起来，\n声音也不再那么紧绷了。"

        $ mwam.meet_irl = True

        nvl clear

        "但有两个位置是空的。\nGra 没有来。Yangsy 也没有来。"
        "你知道她们的理由——\n也许是不想面对，也许是还没有准备好。\n你只是希望有一天她们也能在这里。"

        scene black with fade

        "展位上，ACLCC 的作品吸引了不少人驻足。\n有人第一次看到魔改，露出了惊讶的表情。\n有人试玩之后，竖起了大拇指。"

        lv "看吧……魔改不是只有争议\n# 更多人会喜欢的"

        "那一刻，你想起了一种可能性——\n也许那些偏见，真的可以一点一点被改变。"

    else:
        scene bg group_photo with fade
        play music "audio/mus_setup.ogg" fadein 2.0

        "虽然没有去现场，但你一直守在手机前。\n群里的消息像直播一样不断刷屏——"

        "baile 发了一张照片：lv 正在调试设备，\nMorin 在后面比了个 V 字手势。"

        "mwam 发了一段视频：展位前有人在试玩魔改，\n一边玩一边笑着说\"这是什么鬼哈哈哈哈哈\"。"
        "看到那句笑声，你也忍不住笑了。"

        "lv 偶尔发来一段文字播报："
        lv.nvl "来了好多人\n# 大家对魔改还挺感兴趣的"

        "你看着那些消息，\n虽然不在现场，\n但你能想象出那个画面。"

        "你想起 lv 的决定——\n在废墟上重建 ACLCC 的那个决定。\n当时你觉得，也许这只是徒劳。\n但现在你看到，\n那些废墟上真的开出了花。"

    nvl clear

    scene black with fade
    stop music fadeout 3.0

    "展会结束了。\n线上和线下的世界在这一天短暂地重叠，\n然后又分开。"

    "但有一些事情已经不一样了。"

    '魔改作品的展示获得了意想不到的正面反馈。\n有人说"我以前觉得魔改是在毁游戏，\n今天看到才发现，原来这么有创意"。'
    "偏见开始松动——\n虽然只是一点点，\n但至少有了裂缝。"

    "而更重要的，是你自己的心。"

    "在这段旅程中，你遇到了这群人。\n他们有的人还在你身边，有的人已经离开。"
    
    "但无论怎样，\n你已经不再是当初那个刚刚点进视频的旁观者了。"

    nvl clear

    "故事走到了一个岔路口。\n你还想继续走下去——\n但往哪个方向走，取决于你自己。"

    menu:
        "继续以爱好者的身份和大家在一起（普通线）":
            jump vibe_route_normal

        "成为一个创作者，用作品说话（作者线）":
            jump vibe_route_creator

        "走向那个特别的人（攻略线——请选择角色）":
            jump vibe_route_romance_select

    return

label vibe_route_romance_select:
    scene black with fade

    menu:
        "晴安柚子（Gra）":
            jump vibe_route_gra
        "杨曦（Yangsy）":
            jump vibe_route_yangsy
        "李婉清（mwam）":
            jump vibe_route_mwam
        "李星眠（baile）":
            jump vibe_route_baile
        "莫邪（Morin）":
            jump vibe_route_morin
        "再想想——回到主线选择":
            jump vibe_route_normal
