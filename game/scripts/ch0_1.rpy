label ch0_1:
    
    scene bg that_video with fade
    play music "mus_astral_calm.mp3"
    
    "你点开了他的头像，{w=0.5}在他的主页里并没有找到什么和群聊有关的信息，{w=0.5}只有寥寥几个和冰与火之舞无关的视频。"
    "而且你一会就要去上学了，{w=0.5}也就没有进一步的寻找下去。"
    "你不是什么记性很好的人，{w=0.5}这事很快便被你抛在脑后。"

    scene bg home_night with fade

    "又过了几天，{w=0.5}你的账号收到了一条私信——"

    nvl clear
    gra.nvl "你好，{w=0.25}有兴趣来我们的群里讨论魔改吗？"
    menu(nvl=True):
        "？":
            mc.nvl "？" 
    "{......}没有回复。"
    "其实你知道他在说什么，{w=0.5}但是你不知道该怎么回复。"
    "你不敢直接同意，{w=0.5}也不好意思直接拒绝，{w=0.5}于是决定装傻充愣——"
    
    mc.nvl "你是？"

    gra.nvl "我是Grafrustix，{w=0.5}之前你在评论区发过回复"
    mc.nvl "你好"
    gra.nvl "我们群里有不少人都对魔改感兴趣，{w=0.5}有兴趣加群一起讨论吗？"
    mc.nvl "魔改是？"
    gra.nvl "就是你之前在视频里看到的那种，{w=1.0}我也不知道怎么解释，{w=0.5}你可以去群里看看"
    mc.nvl "哦哦"
    gra.nvl "怎么样，{w=0.25}要来吗？"
    mc.nvl "呃{......}"
    gra.nvl "没关系，{w=0.25}你可以先考虑一下"
    "你故意等了一会，{w=0.5}才回复——"
    mc.nvl "我先想想吧，{w=0.5}群号可以先给我一下吗？"
    gra.nvl "行"


    scene bg home_night with fade
    
    play music "mus_astral_calm.mp3"
    $ renpy.notify("♪ ms_win_and_mc - Astral Calm")

    # if has_phone:
    #     "你使用在视频简介里发现的群号找到了群。"
    # else:
    "你用父母的手机号注册了一个QQ，{w=0.5}使用在视频简介里发现的群号找到了群。"
    
    menu:
        "要加群吗？"
        "当然":
            pass
        "还是算了......":
            pass

    "你发送了入群申请。"

    # scene bg that_video with fade

    # "在等待回复的途中，{w=0.5}你顺便看了这位UP的其他视频。"
    # mc "这螃蟹有意思{...}"
    # "你发现，{w=0.25}这些“被扭曲成某种奇异而搞笑的风格关卡”有一个统称：{w=0.5}{cps=*0.125}{rb}魔改关卡{/rb}{rt}Cursed Levels{/rt}{/cps}。"
    # "没花多久时间，{w=0.5}你就把这些视频全都看了一遍。"
    # "你还发现不同的螃蟹对应着不同的效果，{w=0.5}于是就将它们全部记了下来，{w=0.5}以便不时之需。"

    

    # scene black with dissolve
    # "{......}"
    scene bg home_midnight with fade
    voice "voice/message_prompt.ogg"
    # "——突然响起的QQ提示音将你的意识拉回现实。"
    # "等了将近一个小时的你{w=0.25}此时已经迫不及待了。"
    # "你满怀期待地打开了QQ——{nw}"

    "过了一会，{w=0.5}手机上弹出一条通知——"

    stop music
    nvl clear
    qq.nvl "群主拒绝了你的入群申请"

    mc "{......}"
    "好吧，{w=0.25}这的确让你有点难受。"
    
    scene black with dissolve

    "过了一会{......}"
    qq.nvl "Grafrustix已添加你为好友"

    scene bg home_midnight with dissolve
    mc "？？？"
    """你点开了手机QQ，{w=0.5}点开主页上那个名字是“Grafrustix”的好友："""
    gra.nvl """抱歉啊，{w=0.25}刚刚不小心点错了[[笑哭]"""
    gra.nvl "我看看能不能把你拉进去"
    mc.nvl "没关系的，{w=0.25}实在不行我重新加一遍"
    gra.nvl "那就好"

    # menu:
    #     "再加一遍？"
    #     "是":
    #         pass
    #     "否":
    #         jump chex_unknown_not_join

    "你又发了一遍入群申请——"
    voice "voice/message_prompt.ogg"
    # extend "这次的提示音倒是没过多久就出现了。"
    "这次的提示音倒是没过多久就出现了。"
    "QQ的群聊一栏多出了个“Grafrustix的聊天群”，{w=0.5}群头像右上角有个小红点。"
    "你点开了群聊——"

    nvl clear
    # gra.nvl "抱歉啊，{w=0.25}刚刚不小心点错了[[笑哭]"
    # if has_phone:
    #     "你很快就回复了："
    # else:
    # "你笨拙地找着输入消息的地方，\n{w=0.5}笨拙地打着字，\n{w=0.5}最后{w=0.25}艰难的挤出一条消息："
    
    # morin.nvl "何意味{fast}{nw}"
    # mwam.nvl "这能点错也是没谁了{fast}{nw}"
    # mc.nvl "没关系的"
    
    play music "mus_astral_calm.mp3"
    $ renpy.notify("♪ ms_win_and_mc - Astral Calm")

    gra.nvl "欢迎新人入群[[doge]"
    morin.nvl "[[新人酱！新人酱！！.gif]{fast}{w=0.25}{nw}"
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

    gra.nvl "话说 我还不知道怎么称呼你呢"
    
    # yangsy.comment "Yangsy也不知道该在哪存剧情分支信息，目前就先这样吧（"
    # myworldzycpc.comment "帮你搬到game/custom_variable.rpy了"

    $ variables["gra_chemistry_name"] = None

    if mc.nickname == "奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子":
        $ variables["gra_chemistry_name"] = True
        menu(nvl=True):
            "[mc]":
                $ renpy.music.set_pause(True)
                mc.nvl "[mc]"
                gra.nvl "你这名字很有个性嘛"
                $ renpy.music.set_pause(False)
                gra.nvl "我感觉你很适合做魔改啊"
    else:
        menu(nvl=True):
            "[mc]":
                $ variables["gra_chemistry_name"] = False
                mc.nvl "[mc]"
            "奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子":
                $ variables["gra_chemistry_name"] = True
                $ renpy.music.set_pause(True)
                mc.nvl "奥苯海墨与孙笑氚发明了铅早砹音和丰氚箱子"
                gra.nvl "？"
                gra.nvl "你这名字很有个性嘛"
                $ renpy.music.set_pause(False)
                gra.nvl "我感觉你很适合做魔改啊"
                gra.nvl "不过你应该不叫这个吧？{w=1.0}我到底该怎么叫你？"
                menu(nvl=True):
                    "[mc]":
                        mc.nvl "[mc]"

    #（男人叹气声）（男人叹气声）（男人叹气声）（男人叹气声）（男人叹气声）————Serrate

    gra.nvl "明白了"

    mc.nvl "Gra，这个{......}魔改{......}可以详细讲一讲吗？"
    gra.nvl "可以的可以的"

    nvl clear

    gra.nvl "首先{...}你应该知道冰与火之舞吧？"
    mc.nvl "知道"
    gra.nvl "那就好，{w=0.5}省的我把整个游戏机制给从头讲一遍了"

    stop music

    gra.nvl """
    {cps=*2.5}魔改是一种对谱面进行修改的方式\n
    通常会先在关卡标题后面加上“但如何如何”的描述{/cps}{nw}
    """
    gra.nvl """
    {cps=*2.5}举个例子，Firestix有个魔改关卡，标题是\n
    “11-X 赫拉克勒斯但每一块地板上都有一个旋转”\n
    其中的描述部分就是“但每一块地板上都有一个旋转”{/cps}{nw}
    """
    gra.nvl """
    {cps=*2.5}然后对谱面进行修改，使谱面符合指定的描述\n
    这里就需要给每块地板上都添加旋转\n
    改完谱面之后还要修改音乐，确保与修改后的谱面所契合\n
    这点很重要，毕竟冰与火之舞是一款音乐游戏\n
    音乐与关卡不一致是很严重的问题{/cps}{nw}
    """
    gra.nvl """
    {cps=*2.5}魔改后的关卡会与原关卡产生一种强烈的反差感\n
    我们喜欢这种反差感，并因此聚集在这里\n
    其实我和另外几位成员也会自己制作魔改{/cps}{nw}
    """
    if variables["gra_chemistry_name"]:
        gra.nvl "{cps=*0.5}哪天你也该去试一试{/cps}"
    else:
        gra.nvl "{cps=*0.5}或许你也可以试一试{/cps}"
    
    play music "mus_astral_calm.mp3"
    $ renpy.notify("♪ ms_win_and_mc - Astral Calm")

    mc.nvl "{......}{w=1.0}谢谢，{w=0.5}我大概明白了"
    gra.nvl "那就好\n{w=0.5}我还担心这么多字会不会把你给看迷糊呢"
    yangsy.nvl "这年头持有长文本阅读能力的人确实不多了（"
    
    nvl clear

    # # if not has_phone:
    # mc.nvl "哦对，{w=0.25}还有，{w=0.5}QQ应该怎么用？我不是很熟悉[[笑哭]"

    # "{......}"
    # "Grafrustix又开始耐心地跟你解释起了QQ的使用方法，{w=0.5}以及关于QQ群聊的一些信息。"
    # "你本来还想继续询问“该怎么做魔改”之类的更多疑问——\n{w=0.5}但你母亲却已经在催你去睡觉了。"

    nvl clear
    mc.nvl "我先不聊了"
    gra.nvl "？"
    gra.nvl "这么早就睡？"
    baile.nvl "睡啥睡"
    baile.nvl "起来嗨"
    mwam.nvl "养生呢搁这"
    mc.nvl "不是，是我['妈' if has_phone else '母亲']叫我睡觉了"
    gra.nvl "这样"
    gra.nvl "那就祝你好梦"
    mwam.nvl "明天见"
    morin.nvl "晚安"
    system.nvl "[yangsy.nvl]回应了你的消息：🌙{fast}"
    
    scene black with dissolve
    "{......}"
    scene bg star with dissolve
    stop music fadeout 2.0

    "你躺在床上回想今天发生的一切，{w=0.5}心中充满了干劲，{w=0.5}很快就进入了梦乡。"
    "窗外繁星点点，{w=0.5}或许{w=0.25}象征着无数个明天吧。"
    $ persistent.variables["has_seen_ending"] = True


    call to_be_continued("ch0") from _call_to_be_continued_from_ch0

    return