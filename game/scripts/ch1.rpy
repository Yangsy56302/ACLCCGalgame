label ch1:
    scene black with dissolve
    $ another_view = True
    $ current_perspective = myworldzycpc

    myworldzycpc.comment "我要写主线了吗{...}冲突了怎么办呢{...}"
    myworldzycpc.comment "先写个简单的吧，{w=0.5}后续再慢慢改"

    scene black with dissolve
    $ current_perspective = yangsy

    show yangsy at l11
    pause 0.5
    show yangsy brow_angry mouth_cat_sad_open at hf11
    yangsy.comment "不是什么叫第二天一开始视角就换了？{w=0.5}这也太突兀了吧（"
    show yangsy brow_sad mouth_cat_happy_open at d11
    yangsy.comment "Yangsy稍微试着改一下这段，抱歉了myworld（"
    show yangsy at rhide
    hide yangsy

    scene black with dissolve
    $ another_view = False
    $ current_perspective = mc

    call show_chapter("第二天") from _call_show_chapter

    scene bg home_noon with dissolve

    "星期六早上的太阳已经从地平线上升起，\n{w=1.0}它现在正缓慢地从窗户对面的居民楼房顶再一次为你升起。"
    "阳光照亮到了你的房间，\n{w=0.5}也照亮了你那沉睡的意识。"
    "你揉了揉眼睛，{w=0.5}环顾了一下四周以适应早晨的光线，\n{w=0.5}然后迫不及待地拿出手机，{w=0.25}打开了群聊。"

    $ session_title = None
    nvl clear

    mc.nvl "各位早上好"

    play music "mus_astral_calm.mp3"
    $ renpy.notify("♪ ms_win_and_mc - Astral Calm")

    # morin.nvl "[[早上好 上午好 中午好 下午好 晚上好 半夜好 凌晨好\n专门做了一张图 用来问好 适用于各类人群]{fast}{w=1.0}{nw}"
    # gra.nvl "早{w=0.5}{nw}"

    system.nvl "[yangsy.nvl]回应了你的消息：☀{fast}{w=0.5}{nw}"
    yangsy.nvl "早啊（"

    "{......}"

    mc.nvl "其他成员呢？"
    yangsy.nvl "大部分估计都还在补觉吧（"
    yangsy.nvl "毕竟基本都刚连着上了五天的学 {w=0.5}休息日休息是很正常的事（"
    mc.nvl "这样吗"

    "早上的群聊确实很冷寂——{w=0.5}与记忆中昨晚的盛况简直是天差地别。"

    mc.nvl "Yangsy为什么这么早就醒了呢？"
    yangsy.nvl "问得好\n{w=0.5}Yangsy自己也不知道（"
    yangsy.nvl "或许是因为潜意识里想早点见到大家吧\n{w=1.0}虽说起得这么早通常谁也见不到的说（"

    yangsy.nvl "话说 {w=0.25}昨天几乎没见你主动发言来着"
    yangsy.nvl "别紧张 {w=0.5}进了群就都是自己人（\n{w=0.5}想说些什么的话放心说就是了（"
    mc.nvl "知道了"
    
    yangsy.nvl "诶突然想到个问题"
    yangsy.nvl "[mc.nvl] {w=0.5}你对魔改的印象是...？（"
    yangsy.nvl.comment "这里的选项主要用来暗示普通线与作者线两条路线\n现在就分开两条线还是太早了（"

    $ yangsy_curse_impression = None
    menu(nvl=True):
        "反差感很有意思":
            $ yangsy_curse_impression = 1
            mc.nvl "我觉得魔改谱与原谱的那种反差感很有意思"
            mc.nvl "就感觉像见到了平时所熟知的关卡的另一面这样"
            yangsy.nvl "入坑原因跟大家差不多呢（"
        "对魔改创作很感兴趣":
            $ yangsy_curse_impression = 2
            mc.nvl "我对魔改这种用一句话改变谱面的这种创作方式很感兴趣"
            mc.nvl "毕竟其他作者也不会把已经完成的关卡作为创作素材"
            yangsy.nvl "很少有一上来就对魔改这么感兴趣的人呢"
            if variables["gra_chemistry_name"] is True:
                yangsy.nvl "看来Gra昨天的预感还挺准的？（（（"
            yangsy.nvl "等哪天有想法了你或许可以试试自己做一个？（"
        "说不太上来但就是喜欢":
            $ yangsy_curse_impression = 0
            mc.nvl "我也不太清楚该怎么描述{......}"
            mc.nvl "或许就是单纯喜欢？"
            yangsy.nvl "目前还说不太上来吗\n{w=1.0}没关系的 {w=0.25}很正常（"
            yangsy.nvl "以后说不定哪一天你可能就明白了呢（（"
        "诶魔改原来不是这里\n随便塞点事件那里随便塞点轨道就行了的吗":
            $ yangsy_curse_impression = -1
            mc.nvl "跟你说的那些人差不多"
            yangsy.nvl "{......}"
    
    yangsy.nvl.comment "感觉[mc.nvl]有些ooc了 希望下一位能改一下（"
    yangsy.nvl.comment "总之这里要给主线剧情设目标"

    yangsy.nvl "其实吧\n{w=0.5}我们这些做魔改的\n{w=0.25}其实不太受冰与火之舞圈待见"
    yangsy.nvl "那边普遍都觉得\n{w=0.5}所谓“魔改”什么的 {w=0.5}不过就是\n{w=0.25}这里随便塞点事件 {w=0.25}那里随便塞点轨道就行了的\n{w=0.5}对谱面的恶搞行为"
    yangsy.nvl "但魔改明明就不是随便乱改！\n{w=1.0}我们明明也不是为了恶心观众才这么做的！"
    yangsy.nvl "就因为“魔改”这个名字不太好听\n{w=0.5}连自己骂的到底是什么都不去了解\n{w=0.25}就带着刻板印象去攻击我们"
    yangsy.nvl "到底谁才是恶魔啊喂！"

    mc.nvl "{......}"
    yangsy.nvl "啊 {w=0.25}抱歉（（（\n{w=0.5}Yangsy说着说着就跑题了（（（（（"
    mc.nvl "没关系的"
    yangsy.nvl "那就好（（（"
    yangsy.nvl "总之 {w=0.5}既然其他成员还得过几个小时才醒\n{w=1.0}[mc.nvl]可以过会儿再来检查新消息（"
    mc.nvl "嗯 感谢提醒"
    yangsy.nvl "不用谢（"
    
    mc "{......}还是先做点作业吧。"

    scene black with dissolve
    call show_chapter("三小时后")
    scene bg home_noon with dissolve
    
    "刚刚写完英语作业的你突然意识到，{w=0.5}也许是时候检查一下群内的情况了。"
    
    yangsy.comment "myworld相关剧情Yangsy先移走了"
    yangsy.comment "各位写剧情的时候别忘了现在是2022（划掉）2024年\n很多现ACLCC成员还没加入呢（"
    yangsy.comment "以及这是ACLCCGame 不要过于偏题（（"

    nvl clear

    yangsy.nvl.comment "这段随便填点日常对话吧（"

    mc.nvl "各位早上好"
    lv.nvl "早上好"
    gra.nvl "早安\n{w=1.0}看来你起得还挺早的嘛"
    yangsy.nvl "确实 {w=0.5}要不是Yangsy起得早 {w=0.5}[mc]就得等好几个小时了（"
    mc.nvl "话说，{w=0.25}我好像还不太认识你们呢\n{w=1.0}这个群的历史我也不太了解"
    # myworldzycpc.nvl "我也是{...}"
    gra.nvl "没关系 {w=0.5}我们给你介绍一下"
    gra.nvl "这个群呢 {w=0.5}是当初Yangsy{nw}"
    yangsy.nvl "咳咳（明示{w=1.0}{nw}"
    gra.nvl "是一群对魔改都感兴趣的人\n{w=0.5}彼此聚在一起\n{w=0.5}构成的一个社区"

    nvl clear

    gra.nvl "首先，Yangsy"
    gra.nvl """
    她是我们这个社区的重要人物\n{w=0.5}
    没有她就不可能有我们这个社区

    她的魔改系列也是我们现在很多成员能够聚集在此的原因

    那个系列叫做“{rb}文字魔改{/rb}{rt}String Curse{/rt}”
    """
    mc.nvl "文字{...}魔改？"
    yangsy.nvl "对的对的（"
    gra.nvl """
    魔改有许多许多的系列，{w=0.5}而每个系列都会有它的名字\n{w=1.0}
    我们会用很多这样的元素区分来自不同魔改作者的魔改
    
    体现在形象上时\n{w=0.5}来自不同魔改系列的魔改{w=0.25}会用不同外观的装饰物来表示
    
    像是Yangsy{w=0.25}就会在自己的关卡底部放上两行文本装饰
    """
    yangsy.nvl "Yangsy用文字作为形象的主要原因\n{w=0.25}其实是为了避免画装饰物导致的额外时间成本（"
    gra.nvl '''
    类似的\n{w=0.5}体现在关卡名上时{w=0.25}就会在关卡号附近用各种符号来表示\n{w=1.0}我们把这叫做“魔改标识符”

    比如说，{w=0.25}Yangsy为1-X关卡做的魔改：\n{w=0.5}
    {color=#ffffcc}{i}1-X 冰与火之舞，但判定限制是变化之神{/i}{/color}
    
    加上魔改标识符之后，{w=0.25}就是：\n{w=0.25}
    {color=#ffffcc}{i}"1-X" 冰与火之舞，但判定限制是变化之神{/i}{/color}

    这样只要看到双引号就能认出来这是Yangsy做的魔改了
    '''
    mc.nvl "这样啊……"
    yangsy.nvl "等会咱不是说要介绍群历史来着吗 跑题了啊喂（"
    gra.nvl "不要在意这些细节嘛"

    $ renpy.music.set_pause(True)
    voice "voice/crab_mine_and_qing/prelude.ogg"
    lv.nvl "{nw}"
    $ nvl_erase()
    voice "voice/crab_mine_and_qing/1.ogg"
    extend "{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}螃蟹? 地雷* 还有<晴小姐3 ~{/i} 🎵{nw}"
    voice "voice/crab_mine_and_qing/2.ogg"
    lv.nvl '{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}"文字" 萝卜∇ 还有火柴人 ~{/i} 🎵{nw}'
    voice "voice/crab_mine_and_qing/3.ogg"
    lv.nvl '{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}改曲无授权，根本不是人{/i} 🎵{nw}'
    voice "voice/crab_mine_and_qing/4.ogg"
    lv.nvl '{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}随便乱改圈子被骂有可能{/i} 🎵{nw}'
    voice "voice/crab_mine_and_qing/5.ogg"
    lv.nvl '{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}乱改谱面，tm的过分{/i} 🎵{nw}'
    voice "voice/crab_mine_and_qing/6.ogg"
    lv.nvl '{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}未经授权，小行星无能{/i} 🎵{nw}'
    voice "voice/crab_mine_and_qing/7.ogg"
    lv.nvl '{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}改曲有授权，圈子爽一爽{/i} 🎵{nw}'
    voice "voice/crab_mine_and_qing/8.ogg"
    lv.nvl '{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}魔改谱面，我们共建ACL！{/i} 🎵{nw}'
    gra.nvl "{cps=*0.25}{......}{/cps}"
    $ renpy.music.set_pause(False)

    gra.nvl "{color=#0080FF}@[mc]{/color} 诶，{w=0.5}话说{w=0.25}你要不要做个魔改试试水？"
    yangsy.nvl.comment "{...}Yangsy要不做一个{{at=[[mc]}这样的标签？（"
    mc.nvl "我？"
    gra.nvl "对啊"
    gra.nvl "毕竟都加入ACLC了"
    dwen.nvl "也许会有我们都想不到的点子呢"
    gra.nvl "说不定下一个出名的魔改作者就是你呢？"
    yangsy.nvl "我们都很期待你能做出自己的作品哦"
    yangsy.nvl "不过其实不做也没事的 {w=0.5}你这不才刚进群两天嘛（"
    gra.nvl "并且这里很多成员也都不做魔改\n{w=1.0}好的魔改所需的想象力和创造力也不是所有人都拥有的"
    gra.nvl "总之，{w=0.5}看你的决定了"

    $ variables["volunteer_to_do_curse"] = None
    menu(nvl=True):
        "我会尝试去做的":
            $ variables["volunteer_to_do_curse"] = True
            mc.nvl "好吧"
            mc.nvl "我会争取做出属于自己的魔改的"
            yangsy.nvl "嗯 {w=0.25}勇气可嘉（"
            gra.nvl "那我们就等着你发作品的那一天了哦？"
            # myworldzycpc.nvl "😰"
            mc.nvl "话说{......}{w=0.5}可以教我怎么做吗？\n{w=1.0}我现在连怎么改音乐都不会"
            gra.nvl "emm"
            gra.nvl "现在互联网这么发达，{w=0.5}有什么问题上网解决就是了"
            # nona.nvl "是啊，我还在用Au改音乐呢"
            # yangsy.nvl "你那是特例（"
            yangsy.nvl "诶别这么说 {w=0.5}网上教程哪有自己人教的好（"

            mc.nvl "话说，{w=0.25}刚刚听小绿君说的那些，{w=0.5}感觉好可怕……"
            gra.nvl "没事的，{w=0.25}做魔改一开始踩坑很正常"
            yangsy.nvl "我们这些魔改作者也都或多或少踩过些坑的"
            yangsy.nvl "但正是因为踩过这些坑\n{w=0.5}我们才会知道哪里有坑 {w=0.25}以及该怎么躲开它们"
            mc.nvl "这样吗"
            gra.nvl "嗯，{w=0.25}希望你能在踩坑的过程中不断学习，{w=0.5}走过这段坑坑洼洼的路，{w=0.5}迎接你的将是光明大道"
            
        "我暂时还不太想做":
            $ variables["volunteer_to_do_curse"] = False
            mc.nvl "算了"
            mc.nvl "我暂时还不太想做，和大家在一起就够了"
            yangsy.nvl "意料之中呢 {w=1.0}不过没关系（"
            gra.nvl "无论做不做魔改，{w=0.5}我们ACLC都一样欢迎你！"
            # myworldzycpc.nvl "太好了，吓得我都不敢说话了…"
            # yangsy.nvl "至于吗…\n[['''.gif]"

    jump ch2
