label ch1:
    scene black with dissolve
    $ another_view = True
    $ current_perspective = myworldzycpc

    myworldzycpc.comment "我要写主线了吗{...}冲突了怎么办呢{...}"
    myworldzycpc.comment "先写个简单的吧，{w=0.5}后续再慢慢改"

    scene black with dissolve
    $ current_perspective = yangsy

    show yangsy at l11
    pause 1.0
    show yangsy at hf11
    yangsy.comment brow_angry mouth_cat_sad_open "不是什么叫第二天一开始视角就换了？{w=0.5}这也太突兀了吧（"
    show yangsy at d11
    yangsy.comment brow_jitome mouth_cat_happy "Yangsy稍微试着改一下这段，抱歉了myworld（"
    show yangsy at rhide
    hide yangsy

    scene black with dissolve
    $ another_view = False
    $ current_perspective = mc

    call show_chapter("第二天") from _call_show_chapter

    scene bg home_noon with dissolve

    "又是一天，{w=0.5}你迫不及待的打开了群聊。"

    window hide
    $ session_title = None
    nvl clear
    nvl show

    mc.nvl "各位早上好"

    # morin.nvl "[[早上好 上午好 中午好 下午好 晚上好 半夜好 凌晨好\n专门做了一张图 用来问好 适用于各类人群]{fast}{w=1.0}{nw}"
    # gra.nvl "早{w=0.5}{nw}"
    system.nvl "[yangsy.nvl]回应了你的消息：☀{fast}{w=0.5}{nw}"
    yangsy.nvl "早（"
    
    yangsy.nvl "[mc.nvl]你起的还挺早的\n{w=0.5}群里大部分成员现在这个时候都还在补觉呢（"

    yangsy.nvl "话说 {w=0.25}昨天几乎没见你主动发言来着"
    yangsy.nvl "别紧张 {w=0.5}进了群就都是自己人（\n{w=0.5}想说些什么的话放心说就是了（"

    mc.nvl "{......}知道了"

    yangsy.nvl "我们这些做魔改的{w=0.25}其实不太受冰与火之舞圈待见"
    yangsy.nvl "那边普遍都觉得\n{w=0.5}所谓“魔改”什么的 {w=0.5}不过就是\n{w=0.25}这里随便塞点事件 {w=0.25}那里随便塞点轨道就行了的\n{w=0.5}对谱面的恶搞行为"
    yangsy.nvl "该说是刻板印象吗{...}"
    
    yangsy.nvl "诶正好\n{w=1.0}[mc.nvl] {w=0.5}你对魔改的印象是？（"

    menu(nvl=True):
        "认为魔改用一句话就能大幅改变谱面很神奇":
            mc.nvl "魔改关卡明明只是遵循着标题里那一句简单的改动描述\n关卡就会产生如此天差地别的变化"
            mc.nvl "我觉得这种现象很奇妙"
            pass
        "魔改谱与原谱的反差感很有意思":
            mc.nvl "我觉得魔改谱与原谱的那种反差感很有意思"
            mc.nvl "就感觉像见到了平时所熟知的关卡的另一面这样"
            pass
        "对魔改这种创作方式感兴趣":
            mc.nvl "我对魔改这种创作方式很感兴趣"
            mc.nvl "毕竟其他作者也不会把已经完成的关卡作为创作素材"
            pass
        "说不太上来但就是喜欢":
            mc.nvl "我也不太清楚该怎么描述{......}"
            mc.nvl "或许就是单纯喜欢？"
            pass
        "诶魔改原来不是这里\n随便塞点事件那里随便塞点轨道就行了的吗":
            mc.nvl "跟你说的那些人差不多"
            yangsy.nvl "{......}"
            pass
    
    yangsy.nvl.comment "感觉[mc.nvl]有些ooc了 希望下一位能改一下（"
    yangsy.nvl.comment "总之这里要给主线剧情设目标"

    yangsy.nvl "我希望 {w=0.5}有朝一日{w=0.25}我们魔改圈的成员{w=0.25}不会再被别人带着有色眼镜对待"
    mc.nvl "{......}"
    yangsy.nvl "啊{w=0.25}Yangsy是不是说着说着就跑题了 {w=0.25}抱歉（（（"
    mc.nvl "没关系的"
    yangsy.nvl "那就好（"
    yangsy.nvl "总之 {w=0.5}既然其他成员还得过几个小时才醒\n{w=1.0}[mc.nvl]可以过会儿再来检查新消息（"
    mc.nvl "嗯 感谢提醒"
    yangsy.nvl "不用谢（"
    
    nvl hide

    mc "{......}还是先做点作业吧。"

    scene black with dissolve
    call show_chapter("三小时后")
    scene bg home_noon with dissolve
    
    "刚刚做完了英语作业的你突然意识到，{w=0.5}是时候检查一下QQ消息了。"

    window hide
    $ session_title = None
    nvl clear
    nvl show

    morin.nvl "一日之计在于晨\n我醒了{fast}{nw}"
    gra.nvl "早{fast}{nw}"
    yangsy.nvl "早（{fast}{nw}"
    system.nvl "[myworldzycpc]加入了群聊。{fast}{nw}"
    morin.nvl "[[新人酱！新人酱！！.gif]{fast}{nw}"
    mwam.nvl "欢迎新人{fast}{nw}"
    yangsy.nvl "诶不是连着两天来新人这概率合理吗（{fast}{nw}"
    gra.nvl "你说ACLC网站？\n你是怎么知道的？{fast}{nw}"
    myworldzycpc.nvl "我的朋友 [baile] 告诉我的，看到有个链接说可以加入群聊{fast}"

    nvl hide

    call ch1_myworld_view

    scene home_noon with pixelate
    $ another_view = False
    $ current_perspective = mc
    $ session_title = None
    # nvl clear
    nvl show

    gra.nvl "哦，是 [baile] 告诉你的？{fast}{nw}"
    gra.nvl "这样啊{...}{fast}{nw}"
    gra.nvl "不管怎样，总之欢迎加入 ACLC！{fast}"
    mc "{cps=*0.25}{......}{/cps}"

    call ch1_clever_box
    yangsy.comment "小事（指严重程度\n大事（指篇幅占比"
    yangsy.comment "说实话CB这段偏题剧情放在剧情开头属实有些长了\n这段可以做成中期的分支剧情（"

    jump ch2


label ch1_myworld_view:

    scene black with pixellate
    $ another_view = True
    $ current_perspective = myworldzycpc
    $ session_title = baile
    nvl clear
    nvl show

    myworldzycpc.nvl "听说你要做个谱子下载网站，{w=0.5}是这样吗"
    baile.nvl "嗯是的喵~"
    voice sustain
    myworldzycpc.nvl "我可以看一下你做的吗"
    baile.nvl "行喵~"
    
    myworldzycpc.nvl "这个群号，{w=0.5}我加了一下，{w=0.5}为什么被拒了"
    baile.nvl "不知道，{w=0.5}大概是不能随便进人吧喵~"
    myworldzycpc.nvl "好吧{......}"

    nvl hide
    scene black with pixellate
    $ renpy.notify("某一天")
    nvl clear
    nvl show

    myworldzycpc "（[baile]不在，总觉得有点无聊）"
    myworldzycpc "（要不我再去试试加那个群吧）\n{w=1.0}（上次没通过可能是因为我没写入群消息）"

    nvl clear
    $ session_title = None
    
    system.nvl "加入群聊之前，需要先回答问题：\n{w=1.0}你是怎么知道这个群的？{nw}"
    myworldzycpc.nvl "从ACLC网站"
    "{.....}"

    nvl clear
    $ session_title = None
    voice "voice/message_prompt.ogg"
    system.nvl "你已经是群成员了。"

    nvl clear
    $ session_title = baile
    baile.nvl "我是后背喵~"
    baile.nvl "{......}"
    baile.nvl "bro怎么进ACLC了喵？"

    nvl hide

    return


label ch1_clever_box:
    
    myworldzycpc.nvl "话说回来，之前另外我还在摆了的Clever Box地图介绍里看到过群号呢"
    gra.nvl "什么？你说Clever Box吗？"
    gra.nvl "CB在哪发介绍了？"
    myworldzycpc.nvl "没有，地图正处于开发阶段，而且这个群号在他B站个人简介也有"
    mwam.nvl "到底是cb还是sb（）"
    maoyuna.nvl "ccb"
    gra.nvl "cb"
    gra.nvl "那你是从哪进来的？"
    myworldzycpc.nvl "ACLC网站啊"
    gra.nvl "好吧"
    myworldzycpc.nvl "qwq"
    gra.nvl "那你应该会写数据包吧"
    myworldzycpc.nvl "会一点吧"
    yangsy.nvl "[[惊讶.png]"
    myworldzycpc.nvl.comment "不能{s}锯🪚晴{/s}让[gra]一个人承受{fast}{nw}"
    yangsy.nvl "诶，你会写碰撞模拟和抛物线吗？"
    myworldzycpc.nvl "我不是很确定…"
    yangsy.nvl "没事，会写数据包已经很不错了（"
    myworldzycpc.nvl "如果你想知道我会写什么，大概得说说我才知道会不会写"
    myworldzycpc.nvl "另外如果要抛物线的话，大概可以用带Motion的箭模拟一下？"
    myworldzycpc.nvl.comment "不能让[gra]一个人承受{fast}{nw}"
    mwam.nvl "诶，你看过CB的代码吗"
    myworldzycpc.nvl "看过，而且有一部分是我写的"
    mwam.nvl "比如？"
    myworldzycpc.nvl "函数、各种json，比如选关、机关之类的吧"
    yangsy.nvl "[['''.png]"
    mwam.nvl "其实我还没看过CB，不过听说推箱子基本逻辑有一部分是[yangsy]写的"
    myworldzycpc.nvl "我还以为是[baile]一个人写的呢…"
    mwam.nvl "[baile]好像并不是很会写。"
    mwam.nvl "[[[baile]写的地图代码，包含循环清除活塞掉落物的代码]\n这是摆了的力作"
    yangsy.nvl "全世界的活塞掉落物瞬间神秘失踪\n这究竟是人性的扭曲还是道德的沦丧（"
    
    baile.nvl "可能是这样的吧。"
    myworldzycpc.nvl "没关系的qwq"
    lingyun.nvl "66"
    hale.nvl "盐都不盐了"
    baile.nvl "嗯"

    myworldzycpc.nvl.comment "等等，不能把摆了写死了…"

    menu(nvl=True):
        "你其实一直发挥着很重要的作用":
            mc.nvl "没关系的，你看，如果没有你的创意，ACLC也不会有网站，CB也不可能到这一步啊，你其实一直发挥着很重要的作用"
            baile.nvl "是这样吗喵？"
            myworldzycpc.nvl "其实我感觉我除了机械的写指令以外好像也没有很多创造性的东西"
            myworldzycpc.nvl "没有你，我也做不下去了"
            baile.nvl "感觉你们说的有点道理喵…"

    myworldzycpc.nvl "qwq，听说你们有个MC服务器？"
    myworldzycpc.nvl.comment "这就是摆了之前提到的服务器了？"
    gra.nvl "是的，欢迎你来玩"
    myworldzycpc.nvl "我是新来的，不过我在服务器里翻箱倒柜只找到5块牛排，还是生的，想问一下这个服务器有提供食物的地方吗…"
    gra.nvl "应该没有（"
    myworldzycpc.nvl "你们平时都吃什么呢？"
    mwam.nvl "将军肉"
    myworldzycpc.nvl "好"
    myworldzycpc.nvl "我去偷村民的胡萝卜炖金子吃了（"
    mwam.nvl "66"
    mwam.nvl "金胡萝卜就金胡萝卜"
    mwam.nvl "神TM胡萝卜炖金子"

    "没想到刚进群第二天，[mc]就遇到了一个和自己一样的新人。"

    scene black with fade

    "是的，群里总是时不时的出现一些小事，但是呢，又能很快和解。"
    myworldzycpc.comment "话说这算得上事吗（"

    return

