label ch0:
    stop music
    scene bg sky with fade

    "作为一个二线城市普通家庭的学生，\n{w=0.5}你比大多数人更容易接触到一些新潮的事物。"
    "同样的，{w=0.25}作为一个二线城市普通家庭的学生，\n{w=0.5}你的一些爱好往往并不能找到与你志同道合的伙伴。"
    "你不是一个外向的学生，{w=0.5}只是一个班里的小透明。\n有着普通的父母，{w=0.5}住着普通的房子，{w=0.5}上着普通的学校，{w=0.5}学习也普普通通。"
    "不是什么大家口里的坏孩子，\n{w=0.5}但也不是别人家长口中的“别人家的孩子”。"
    "日子就这么普普通通的过着{......}"


    scene bg home_noon with fade

    # "有一天，{w=0.25}你在网上冲浪的时候发现一个视频，{w=0.5}标题写着{w=0.25}“0基础编程教学”。{nw}"
    # $ _history_list.pop()
    # menu:
    #     "有一天，你在网上冲浪的时候发现一个视频，标题写着“0基础编程教学”。{fast}"
    #     "不点开这个视频":
    #         "你对这个视频不感兴趣，{w=0.5}也就没有点开那个视频。"
    #         "日子{w=0.25}还是普普通通的过着。"
    # 
    #         scene black with dissolve
    #         "{......}"
    #         scene bg sky with dissolve
    # 
    #         $ tutorial = "网上的教程"
    #         jump ch0_adofai
    # 
    #     "点开这个视频":
    #         "你对这个视频很感兴趣，{w=0.5}于是点了进去。"
    #         scene bg sky with fade
    #         "跟着视频学了一会，{w=0.5}你渐渐的开始对信息技术产生了浓厚的兴趣{...}"
    #         jump chex_unknown_oi
    $ renpy.notify("2020年某日")
    pause 3.0


    play music "mus_astral_calm.mp3" volume 0.3 fadein 1.0
    $ renpy.notify("♪ ms_win_and_mc - Astral Calm")

    "大概是2020年的某一天，{w=0.5}你偶然在某个视频网站上解接触到了一款游戏。"
    "作为一款音乐游戏，{w=0.5}它的玩法极其简单。"
    "在游戏官网详情页上是这么写的：\n
    {color=#ffffcc}{w=0.5}{i}“只需一个按键，{w=0.5}控制盘旋飞舞的双星，{w=0.5}踏着摇曳的舞步，\n{w=0.5}在一条跟随音乐节奏变化的蜿蜒道路上不断前进，{w=0.5}探索音乐的宇宙。”"
    "当然，{w=0.25}那时的你并没有看见这句话，{w=0.5}\n不过别人的游玩过程依然勾起了你的好奇心。"
    "在刷了几个下方的推荐视频后，{w=0.5}你萌生了尝试的想法，\n{w=0.5}不过那时的你并没有零花钱。"
    "尽管26元的游戏已经算是廉价，\n{w=0.5}但对于只在父母手机上玩过一些免费小游戏的你来说，{w=0.5}依然是一笔巨款。"
    "不得已，{w=0.25}你只能在搜索结果下的无数广告里下载了一个{w=0.25}{yellow}“渠道版”{/yellow}{w=0.25}将就着玩。"


    scene bg sbeam with dissolve

    # play music "mus_astral_calm.mp3"
    # python:
    #     renpy.notify("♪ ms_win_and_mc - Astral Calm")
    #     persistent.is_music1_unlock = True
    "在将游戏里的关卡翻来覆去的打了好几遍之后，{w=0.5}你开始觉得无聊了。"
    "作为一个社区内容占了极大比例的游戏，\n{w=0.5}“渠道版”不能联网的弊端越发明显。"
    "虽然游戏里也内置了编辑器，{w=0.5}但是那时的你对此一窍不通。"
    "在网站上看到的关卡，{w=0.5}简介里的链接也往往是创意工坊或是外网的云盘。"

    "最终，{w=0.25}在经历了几天的心理斗争之后，{w=0.5}你跟着网上的教程下载了Sbeam，\n{w=0.5}又偷偷用父母的信用卡笨拙地按照指示付了款。"

    stop music fadeout 2.0

    "然而，{w=0.25}在你购买游戏后没几天，{w=0.5}国外论坛在国内有了{green}镜像服务器{/green}，\n{w=0.5}可以方便的下载谱面。"
    "这让你的心理斗争与购买游戏的行为显得如此愚蠢。"

    play music "mus_astral_calm.mp3" volume 0.3 fadein 1.0

    "虽然你在知道这则消息之后气的跳脚，{w=0.5}但是你并没有抛弃这款游戏。"
    "一方面是，{w=0.5}你认为这是第一个属于自己的东西。"
    "那时候的家里，{w=0.5}电脑是父母的，{w=0.25}手机是父母的，{w=0.25}钱也是父母的。"
    "虽然买游戏的钱来自父母，{w=0.5}但是你觉得游戏是属于自己的，{w=0.25}有了感情。"
    "另外一方面是，{w=0.5}26元对你而言真的很贵。"
    "总之，{w=0.25}在购买了正版之后，{w=0.5}你接触到了更多你喜欢的谱面，{w=0.5}技术也在一天一天的提高。"
    "当然，{w=0.25}你父母最终知道了这件事。"
    "他们并没有斥责你，{w=0.5}只是用一种深邃的眼神看着你。"

    stop music fadeout 2.0
    scene sky with dissolve

    "对于经历着忽略式教育的你，{w=0.5}在你做错事的时候，\n{w=0.5}这种眼神已经见过无数次。"
    "像以前一样，{w=0.5}他们问了你钱的来源，{w=0.25}钱的数目，{w=0.25}买了什么东西，\n{w=0.5}以及做这一切的原因。"
    "在这期间，{w=0.5}他们一直在用这种眼神与你对视，{w=0.5}长达数分钟。"
    "最后，{w=0.25}随着一句{w=0.25}{color=#ff9999}“下不为例。”{/color}，{w=0.5}谈话结束。"
    "这样的谈话你已经经历了很多次。"
    "对你的父母来说，{w=0.5}他们并不觉得你会误入歧途，\n{w=0.5}但也没在你身上看见可能。"
    "父母都忙于生计，{w=0.25}并不关注你，{w=0.5}他们也认为你懂事，\n{w=0.5}因此家庭氛围还算融洽。"
    "而这样的家庭也养成了你内向的性格。"
    "你也没在学校里大肆宣传这个游戏，\n{w=0.5}即使偶尔和几个关系近的同学提起，{w=0.5}他们也不感兴趣。"
    "{cps=*0.5}日子依旧普普通通的过着{......}"


    scene bg that_video with fade

    $ renpy.notify("2022年某日，嘁哩嘁哩评论区")
    pause 1.0

    play music "mus_astral_calm.mp3" volume 0.3 fadein 1.0

    
    "就像之前的每一天一样，{w=0.5}你百无聊赖的刷着嘁站。"
    "作为一个已经断断续续玩过两年的玩家，\n{w=0.5}你早已掌握了这款名为《冰与火之舞》的游戏的玩法，\n{w=0.5}并取得了一些你自认为满意的记录。"
    "平时，{w=0.25}你也会在视频网站上消磨时间。"
    "有时看到一个高难谱面的通关或一张精美的特效作品，\n{w=0.5}你会毫不吝啬的在评论区表达你的赞美之情；"
    "有时看见一名新人入坑，\n{w=0.5}你也会在评论区鼓励一番。"
    "虽然仍不是什么著名人物，{w=0.5}但你在网络上也算是有了点名气。"
    mc "{......}{......}这啥玩意？"
    "随着又一次刷新，{w=0.25}主页上跳出一张封面简陋得如同小孩子简笔画的视频，\n{w=0.5}标题里的“冰与火之舞”五个字勾起了你的兴趣。"
    "这次的风格，{w=0.5}你从未见过。"
    "{cps=*0.75}怀着好奇心，{w=0.5}你点开了那个视频。{w=1.0}{nw}"

    scene black with dissolve
    stop music fadeout 1.0

    mc "{......}{......}"
    "{cps=*1.0}你感觉像是被人喂了一口屎。{/cps}"
    # yangsy.comment "诶不是咱就是说这话是不是有点太糙了啊喂（{nw}"

    scene bg that_video with dissolve
    play music "mus_astral_calm.mp3" volume 0.3 fadein 1.0
    
    "显然，{w=0.25}这是一个外网的转载视频。"
    "画面中，{w=0.25}你熟悉的一个个关卡被扭曲成了某种奇异而搞笑的风格，\n{w=0.5}加入了各种奇奇怪怪的机制。"
    "看着这一个个被“魔改”得面目全非的关卡，\n{w=0.5}你的心情从疑惑，{w=0.5}无语，{w=0.5}到愤怒，{w=0.5}再到平静。"
    "到了快结束的时候，{w=0.5}你甚至不受控制地笑了一下。"
    "显然，{w=0.5}你已经彻底理解了这种{cps=*0.5}“特立独行”{/cps}的艺术。"
    "按照惯例，{w=0.25}你发表了一条评论——"
    mc "{w=1.0}{nw}"
    $ _history_list.pop()
    "——其实你早就把那天评论的具体内容给忘了，\n{w=0.5}不过那条评论收获了许多的点赞与回复你倒是还记得很清楚。"
    stop music fadeout 1.0
    "而其中有一条回复，{w=0.5}你无论如何也不会忘记："

    scene black with dissolve

    nvl clear
    gra.nvl "觉得有兴趣的话可以来我们群里玩哦[[doge]"
    # mwam.comment "他自己说的，不要问我（{nw}"
    
    
    "{cps=*0.5}故事，{w=0.5}就从这{w=0.25}开始了。{/cps}"
    jump ch0_1


label ch0_1:
    scene bg home_night with dissolve
    # if has_phone:
    #     "你使用在视频简介里发现的群号找到了群。"
    # else:
    "你用父母的手机号注册了一个QQ，{w=0.5}使用在视频简介里发现的群号找到了群。"
    
    menu:
        "要加群吗？"
        "加群":
            pass
        "不加群":
            setup "骗你的，{w=0.5}你莫得选择。"

    "你发送了入群申请。"

    scene bg that_video with fade

    "在等待回复的途中，{w=0.5}你顺便看了这位UP的其他视频。"
    mc "这螃蟹有意思{...}"
    "你发现，{w=0.25}这些“被扭曲成某种奇异而搞笑的风格关卡”有一个统称：{w=0.5}{cps=*0.125}{rb}魔改关卡{/rb}{rt}Cursed Levels{/rt}{/cps}。"
    "没花多久时间，{w=0.5}你就把这些视频全都看了一遍。"
    "你还发现不同的螃蟹对应着不同的效果，{w=0.5}于是就将它们全部记了下来，{w=0.5}以便不时之需。"

    scene black with dissolve
    "{......}"
    scene bg home_midnight with dissolve

    "——突然响起的QQ提示音将你的意识拉回现实。"
    "等了将近一个小时的你{w=0.25}此时已经迫不及待了。"
    "你满怀期待地打开了QQ——{nw}"

    nvl clear
    system.nvl "{cps=*0.25}群主拒绝了你的入群申请{/cps}"

    mc "{......}{w=0.5}为什么会这样？"

    # menu:
    #     "再加一遍？"
    #     "是":
    #         pass
    #     "否":
    #         jump chex_unknown_not_join

    "不信邪的你又发了一遍入群申请——{w=0.5}这次的提示音倒是没过多久就出现了。"
    "QQ的群聊一栏多出了个名叫“Grafrustix的聊天群”的群。\n{w=1.0}你点进群内，{w=0.5}很快就看到了第一条消息："

    nvl clear
    gra.nvl "抱歉啊，{w=0.25}刚刚不小心点错了[[笑哭]"
    # if has_phone:
    #     "你很快就回复了："
    # else:
    "你笨拙地找着输入消息的地方，\n{w=0.5}笨拙地打着字，\n{w=0.5}最后{w=0.25}艰难的挤出一条消息："
    
    morin.nvl "何意味{fast}{nw}"
    mwam.nvl "这能点错也是没谁了{fast}{nw}"
    mc.nvl "没关系的"
    gra.nvl "总之欢迎新人入群[[doge]"
    morin.nvl "[[新人酱！新人酱！！.gif]{w=0.25}{nw}"
    mwam.nvl "欢迎新人{w=0.25}{nw}"
    lingyun.nvl "欢迎{w=0.25}{nw}"
    baile.nvl "欢迎"

    # if not has_phone:
    # "你又笨拙的发送了一条消息："
    # mc.nvl "那个，{w=0.25}您能介绍下自己吗，{w=0.5}我该怎么称呼您？"
    # gra.nvl "不用这么恭敬的啦{nw}"
    # pause 0.5

    gra.nvl "我是Grafrustix"
    gra.nvl "叫我晴柚也行"

    gra.nvl "群里的成员主要是对魔改感兴趣才加入这里讨论的"
    gra.nvl "不过也不完全是，{w=0.5}比如说有一部分成员其实是我同学"
    mwam.nvl "也可以说是线下粉丝"
    lingyun.nvl "神TM线下粉丝"

    gra.nvl "话说 {w=0.5}我该怎么叫你？"
    default gra_chemistry_name = False
    # yangsy.comment "Yangsy也不知道该在哪存剧情分支信息，目前就先这样吧（"

    if mc.nickname == "奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子":
        $ gra_chemistry_name = True
        menu(nvl=True):
            "[mc]":
                mc.nvl "[mc]"
                gra.nvl "你这名字很有个性嘛"
                gra.nvl "我感觉你很适合做魔改啊"
    else:
        menu(nvl=True):
            "[mc]":
                mc.nvl "[mc]"
            "奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子":
                $ gra_chemistry_name = True
                mc.nvl "奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子"
                gra.nvl "？"
                gra.nvl "你这名字很有个性嘛"
                gra.nvl "我感觉你很适合做魔改啊"
                gra.nvl "不过你应该不叫这个吧？{w=1.0}我到底该怎么叫你？"
                menu(nvl=True):
                    "[mc]":
                        mc.nvl "[mc]"

    gra.nvl "行，{w=0.25}就这么叫你了"

    mc.nvl "Grafrustix，{w=0.5}我还是不太理解这个魔改到底是什么"
    mc.nvl "可以详细讲一讲吗？"
    gra.nvl "可以的可以的"

    gra.nvl "首先{...}你应该知道冰与火之舞吧？"
    mc.nvl "知道"
    gra.nvl "那就好，{w=0.5}省的我把整个游戏机制给从头讲一遍了"

    nvl clear
    gra.nvl "魔改是一种对谱面进行修改的方式{nw}"
    gra.nvl "通常会先在关卡标题后面加上“但如何如何”的描述{nw}"
    gra.nvl "举个例子，Firestix有个魔改关卡，标题是\n“11-X 赫拉克勒斯但每一块地板上都有一个旋转”{nw}"
    gra.nvl "其中的描述部分就是“但每一块地板上都有一个旋转”{nw}"
    gra.nvl "然后对谱面进行修改，使谱面符合指定的描述{nw}"
    gra.nvl "这里就需要给每块地板上都添加旋转{nw}"
    gra.nvl "改完谱面之后还要修改音乐，确保与修改后的谱面所契合{nw}"
    gra.nvl "这点很重要，毕竟冰与火之舞是一款音乐游戏\n音乐与关卡不一致是很严重的问题{nw}"
    gra.nvl "魔改后的关卡会与原关卡产生一种强烈的反差感{nw}"
    gra.nvl "我们喜欢这种反差感，并因此聚集在这里{nw}"
    gra.nvl "其实我和另外几位成员也会自己制作魔改{nw}"
    if gra_chemistry_name:
        gra.nvl "哪天你也该去试一试"
    else:
        gra.nvl "或许你也可以试一试"
    
    mc.nvl "{......}谢谢Grafrustix，{w=0.5}我大概明白了"
    gra.nvl "那就好\n{w=1.0}我还担心这么多字会不会把你给看迷糊呢"
    yangsy.nvl "这年头持有长文本阅读能力的人确实不多了（"
    
    # if not has_phone:
    mc.nvl "哦对，{w=0.25}还有，{w=0.5}QQ应该怎么用？我不是很熟悉[[笑哭]"

    "{......}"
    "Grafrustix又开始耐心地跟你解释起了QQ的使用方法，{w=0.5}以及关于QQ群聊的一些信息。"
    "你本来还想继续询问“该怎么做魔改”之类的更多疑问——\n{w=0.5}但你母亲却已经在催你去睡觉了。"

    nvl clear
    mc.nvl "我先不聊了"
    gra.nvl "？{w=0.5}{nw}"
    gra.nvl "这么早就睡？{w=1.0}{nw}"
    baile.nvl "睡啥睡{w=0.5}{nw}"
    baile.nvl "起来嗨{w=1.0}{nw}"
    mwam.nvl "养生呢搁这"
    mc.nvl "不是，是{w=0.5}我['妈' if has_phone else '母亲']叫我睡觉了"
    gra.nvl "哦，{w=0.25}好吧"
    gra.nvl "那就祝你好梦{w=0.5}{nw}"
    mwam.nvl "明天见{w=0.25}{nw}"
    morin.nvl "晚安{w=0.25}{nw}"
    yangsy.nvl "🌙"
    
    scene black with dissolve
    "{......}"
    scene bg star with dissolve

    "你躺在床上回想今天发生的一切，{w=0.5}心中充满了干劲，{w=0.5}很快就进入了梦乡。"
    "窗外繁星点点，{w=0.5}或许{w=0.25}象征着无数个明天吧。"
    $ persistent.has_seen_ending = True


    while True:
        stop music fadeout 1.0
        scene black with dissolve
        menu:
            "未完待续{......}"
            "查看已被废弃的AI剧情":
                jump vibe_ch2
            "查看[yoosee]的建议":
                call chplotadvice_yoosee
            "查看[yangsy]的建议":
                call chplotadvice_yangsy
            "返回主菜单":
                return
        
    return



label chplotadvice_yoosee:

    scene black with dissolve
    
    # ch0 internally jumps to ch1 → ch2 → ... ch11 → route branches → epilogue → return
    
    yoosee.comment "不用照搬历史\n确定人物性格和故事走向就行"

    yoosee.comment "漫展之后就从主线过渡到各个人物线上了\n所以主角是在这里要确定发展关系"
    yangsy.comment "可不可以每一次都进一部分可攻略角色的线（\n别一次漫展世界线就全岔开了（"
    yoosee.comment "看情况"
    yoosee.comment "有的可能第一次就可以\n有的要第一次触发一些事件\n也可以比如第二次的时候没有触发条件就会断线这样"

    yoosee.comment "总体可以分为普通线，作者线，攻略线三种"
    yoosee.comment "普通线就是正常爱好者\n但是更偏向于普通玩家而不是深入魔改圈"
    yoosee.comment "作者线就是成为魔改作者这样"
    yoosee.comment "然后作者线也可以出发一些攻略角色"
    yoosee.comment "攻略线更侧重感情"
    yoosee.comment "魔改用于增添风味（）"

    return



label chplotadvice_yangsy:

    scene black with dissolve

    yangsy.comment "首先让大部分所有群员全都欢迎一句；可以顺便加点群员之间的互动"
    yangsy.comment "然后各种小事发生时需要搞些选项能跟涉事成员交谈，提高进线可能"
    yangsy.comment "自己的剧情自己写，写成啥样都没关系，后面会有人专门负责精修的"
    yangsy.comment "等主角熟悉群内环境之后就可以安排全体打算让主角做个魔改试试水"
    yangsy.comment "如果主角选择去尝试创作魔改，就让主角进创作者线，否则进普通线"
    yangsy.comment "前者攻略Gra，Yangsy等创作者，后者攻略Morin，ms_win等普通成员"
    yangsy.comment "也就是说要把攻略线拆成作者线和普通线的后续分支而不是平行时空"
    yangsy.comment "然后就再来点什么其他的小事，依旧，跟涉事成员交谈提高进线可能"
    yangsy.comment "不要直接让玩家直接选攻略谁，而是根据平时选了谁的选项自动决定"
    yangsy.comment "两次漫展主要用于提供选项以判断正在攻略的角色；决定不了就共通"
    yangsy.comment "螃蟹事件啊群聊解散啊这种刀子剧情虽说确实经历过但还是别写了（"
    yangsy.comment "最终结局和二周目meta线就到时候再说了，这都不是现在的首要事项"
    yangsy.comment "哦对如果你还没发现Yangsy每句长度都一样的话Yangsy会很失望的（"
    yangsy.comment "当然游戏内的字体并不是等宽字体所以这点很难看出来就是了（（（"

    return
