label ch0:
    stop music
    scene bg sky with fade

    "作为一个二线城市普通家庭的学生，\n{w=0.5}你比大多数人更容易接触到一些新潮的事物。"
    "同样的，{w=0.25}作为一个二线城市普通家庭的学生，\n{w=0.5}你的一些爱好往往并不能找到与你志同道合的伙伴。"
    "你不是一个外向的学生，{w=0.5}只是一个班里的小透明。"
    "有着普通的父母，{w=0.5}住着普通的房子，{w=0.5}上着普通的学校，{w=0.5}学习也普普通通。"
    "不是什么大家口里的坏孩子，{w=0.5}但也不是别人家长口中的“别人家的孩子”。"
    "日子{w=0.25}就这么普普通通的过着。"
    "{......}"

    scene bg sky with fade
    "有一天"
    "你在网上冲浪的时候发现一个视频"
    "标题为：\"0基础编程教学\""
    menu:
        "不点开这个视频":
            "你对这个视频不感兴趣，于是你没有点开那个视频"
            scene bg sky with fade
            $ renpy.notify("2020年某日")
            pause 1.0
            "你偶然在某个视频网站上遇到了一款游戏。"
            $ tutorial = "网上的教程"
        "点开这个视频":
            "你对这个视频很感兴趣，于是点了进去"
            scene bg sky with fade
            "跟着视频学了一会，你渐渐的开始对信息技术产生了浓厚的兴趣"
            jump chex0_oi

label ch0_adofai:
    scene bg sbeam with dissolve
    "只需一个按键，{w=0.5}控制盘旋飞舞的双星，{w=0.5}踏着摇曳的舞步，\n{w=0.5}在一条跟随音乐节奏变化的蜿蜒道路上不断前进，{w=0.5}探索音乐的宇宙。"
    
    if has_phone:
        "你突然很想尝试一下。"
    else:
        "你突然很想尝试一下，{w=0.5}不过你身无分文。"
    
    play music "mus_astral_calm.mp3"
    $ renpy.notify("♪ ms_win_and_mc - Astral Calm")
    
    if has_phone:
        "最终，{w=0.25}你一点点跟着[tutorial]下载了Sbeam，\n{w=0.5}购买了这款游戏。"
    else:
        "最终，{w=0.25}你一点点跟着[tutorial]下载了Sbeam，\n{w=0.5}又偷偷用父母的信用卡笨拙地按照指示付了款。"
        "游戏并不贵，{w=0.5}26元人民币，\n{w=0.5}但对于只在父母手机上玩过一些免费小游戏的你来说，{w=0.5}依然是一笔巨款。"
        "当然，{w=0.25}你父母最终知道了这件事，\n{w=0.5}不过他们并没有斥责你，{w=0.5}经过一番简单的谈话后便原谅了你的行为。"
        "诚然，{w=0.25}对你的父母来说，{w=0.5}他们并不觉得你会误入歧途，\n{w=0.5}但也没在你身上看见光宗耀祖的可能。"
    
    "你也没在学校里大肆宣传这个游戏，\n{w=0.5}即使偶尔和几个关系近的同学提起，{w=0.5}他们也不感兴趣。"
    "日子{w=0.25}依旧普普通通的过着。"
    "{......}"
    # "{cps=*0.5}直到{w=0.25}有一天......{/cps}"

    scene bg that_video with fade

    $ renpy.notify("2022年某日，嘁哩嘁哩评论区")
    pause 1.0

    play music "mus_astral_calm.mp3" volume 0.3 fadein 1.0
    $ renpy.notify("♪ ms_win_and_mc - Astral Calm")
    
    "就像之前的每一天一样，{w=0.5}你百无聊赖的刷着嘁站。"
    mc "{......}{......}这啥玩意？"
    "随着又一次刷新，{w=0.25}主页上跳出一张封面简陋得如同小孩子简笔画的视频，\n{w=0.5}标题里的“冰与火之舞”五个字勾起了你的兴趣。"
    "作为一个已经断断续续玩过两年的玩家，\n{w=0.5}你早已掌握了这款游戏的玩法，\n{w=0.5}并取得了一些你自认为满意的记录。"
    "平时，{w=0.25}你也会在视频网站上消磨时间。"
    "有时看到一个高难谱面的通关或一张精美的特效作品，\n{w=0.5}你会毫不吝啬的在评论区表达你的赞美之情；"
    "有时看见一名新人入坑，\n{w=0.5}你也会在评论区鼓励一番。"
    "虽然仍不是什么著名人物，{w=0.5}但你在网络上也算是有了点名气。"
    "不过这次的风格，{w=0.25}你从未见过。"
    "{cps=*0.75}怀着好奇心，{w=0.5}你点开了那个视频。{w=1.0}{nw}"

    scene black
    stop music

    mc "{......}{......}"
    "{cps=32}你感觉像是被人喂了一口屎。"

    scene bg that_video
    play music "mus_astral_calm.mp3" volume 0.3 fadein 1.0
    
    # yangsy "诶不是咱就是说这话是不是有点太糙了啊喂（{nw}"
    "显然，{w=0.25}这是一个外网的转载视频。"
    "画面中，{w=0.25}你熟悉的一个个关卡被扭曲成了某种奇异而搞笑的风格，\n{w=0.5}加入了各种奇奇怪怪的机制。"
    "看着这一个个被“魔改”得面目全非的关卡，\n{w=0.5}你的心情从疑惑，{w=0.5}无语，{w=0.5}到愤怒，{w=0.5}再到平静。"
    "到了快结束的时候，{w=0.5}你甚至不受控制地笑了一下。"
    "显然，{w=0.5}你已经彻底理解了这种{cps=*0.5}“特立独行”{/cps}的艺术。"
    "按照惯例，{w=0.25}你发表了一条评论："
    # mc "{cps=*0.5}做出这个东西的人{w=0.5}{b}一定{/b}{w=0.25}是个天才。{/cps}"
    mc "{w=1.0}{nw}"
    "其实你早就忘了那天的评论究竟是什么，{w=0.5}不过那条评论收获了许多的赞。"
    stop music fadeout 2.0
    "不过，那条评论的一个回复，你记得很清楚。"
    # yoosee "这一句我觉得不满意，后面要改"

    scene black

    # $ renpy.notify("几天之后")
    # pause 1.0

    # "几天之后，{w=0.5}你的评论{w=0.5}收到了一条回复。"
    gra "喜欢的话可以来我们群里[[doge]"
    # mwam "他自己说的，不要问我（{nw}"
    scene black
    # stop music
    $ persistent.has_seen_ending = True
    "{cps=*0.5}故事，{w=0.5}就从这{w=0.25}开始了。{/cps}"
    jump ch0_1

label ch0_1:
    scene bg that_video with fade
    if has_phone:
        "你使用在视频简介里发现的群号找到了群。"
    else:
        "你用父母的手机号注册了一个QQ，{w=0.5}使用在视频简介里发现的群号找到了群。"
    
    menu:
        "要加群吗？"
        "加群":
            pass
        "不加群":
            jump chex0_not_join

    "你发送了入群申请。"
    "在等待回复的时候，{w=0.5}你顺便看了这位UP的其他视频。"
    mc "这螃蟹有意思"
    "你发现，{w=0.25}这些“被扭曲成某种奇异而搞笑的风格关卡”有一个统称：{w=0.5}{cps=*0.125}{rb}魔改关卡{/rb}{rt}Cursed Levels{/rt}{/cps}。"
    "没花多久时间，你就把这些视频全都看了一遍。"
    "你发现不同的螃蟹对应着不同的效果，{w=0.5}因此将它们全部记了下来，{w=0.5}以便不时之需。"
    scene bg adofai with fade
    "{......}突然响起的QQ提示音将你的意识从虚无中拉回现实。"
    "等待了将近一个小时的你{w=0.25}此时已经迫不及待了。"
    "你满怀期特地打开了QQ——{nw}"
    "{cps=*0.25}群主拒绝了你的入群申请{/cps}"
    mc "{......}{w=0.5}为什么会这样？"

    menu:
        "再加一遍？"
        "是":
            pass
        "否":
            jump chex0_not_join

    "不信邪的你又发了一遍入群申请——{w=0.5}这次的提示音倒是没过多久就出现了。"
    "QQ的群聊一栏多出了个名叫“Grafrustix的聊天群”的群。\n{w=1.0}你点进群内，{w=0.5}很快就看到了第一条消息："
    nvl clear
    gra.nvl "抱歉啊，{w=0.25}刚刚不小心点错了[[笑哭]"
    if has_phone:
        "你很快就回复了："
    else:
        "你笨拙地找着输入消息的地方，\n{w=0.5}笨拙地打着字，\n{w=0.5}最后{w=0.25}艰难的挤出一条消息："
    mc.nvl "没关系的{w=0.5}{nw}"
    gra.nvl "觉得有兴趣可以进群里玩哦[[doge]"
    if not has_phone:
        "你又笨拙的发送了一条消息："
    mc.nvl "那个，{w=0.25}你能介绍下你是谁吗，{w=0.5}我该怎么称呼您？"
    gra.nvl "不用这么恭敬的啦{w=1.0}{nw}"
    gra.nvl "我是Grafrustix{w=0.5}{nw}"
    gra.nvl "叫我晴柚也行{w=1.0}{nw}"
    gra.nvl "所以 你叫什么"
    if mc.nickname == "奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子":
        menu:
            "[mc]":
                mc.nvl "我叫[mc]"
        gra.nvl "你这个名字很有个性啊{w=1.0}{nw}"
        gra.nvl "我感觉你很适合做魔改啊"
    else:
        menu:
            "[mc]":
                mc.nvl "我叫[mc]"
            "奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子":
                mc.nvl "我叫奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子"
                gra.nvl "？{w=1.0}{nw}"
                gra.nvl "有想法{w=0.5}{nw}"
                gra.nvl "我感觉你很适合做魔改啊{w=1.0}{nw}"
                gra.nvl "不过你不叫这个吧？{w=1.0}我到底怎么叫你？"
                menu:
                    "[mc]":
                        mc.nvl "我叫[mc]"       
    gra.nvl "行，就这么叫你了"
    mc.nvl "Gra，{w=0.25}这个魔改到底是什么，{w=0.5}能给我讲讲吗？{w=1.0}{nw}"
    if not has_phone:
        mc.nvl "还有QQ怎么用[[笑哭]"
    "{......}"
    if has_phone:
        "Gra 耐心地跟你解释了各种事情：\n{w=1.0}什么是魔改，{w=0.5}以及关于QQ群聊的一些信息{...}"
    else:
        "Gra 耐心地跟你解释了各种事情：\n{w=1.0}什么是魔改，{w=0.5}QQ怎么用，{w=0.5}以及关于QQ群聊的一些信息{...}"
    "你还了解到，{w=0.5}Gra 也是一名魔改作者，{w=0.5}而在这个群里还有好几位像 Gra 一样的魔改作者。"
    "你本来还想继续询问“该怎么做魔改”之类的更多疑问——\n{w=0.5}但你母亲却已经在催你去睡觉了。"
    nvl clear
    mc.nvl 'Gra，{w=0.25}我先不聊了，{w=0.5}我["妈" if has_phone else "母亲"]叫我睡觉了'
    gra.nvl "祝你好梦"
    "你躺在床上回想今天发生的一切，{w=0.5}心中充满了干劲，{w=0.5}很快就进入了梦乡。"
    "窗外繁星点点，{w=0.5}或许{w=0.25}象征着无数个明天吧。"

    while True:
        menu:
            "未完待续{......}"
            "查看AI剧情":
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
