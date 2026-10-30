label myworld:
    $ session_title = None
    nvl clear

    $ config.nvl_list_length = 9

    morin.nvl "一日之计在于晨\n我醒了{fast}{nw}"
    gra.nvl "早{fast}{nw}"
    yangsy.nvl "早（{fast}{nw}"
    system.nvl "[myworldzycpc]加入了群聊。{fast}{nw}"
    morin.nvl "[[新人酱！新人酱！！.gif]{fast}{nw}"
    mwam.nvl "欢迎新人{fast}{nw}"
    yangsy.nvl "诶不是连着两天来新人这概率合理吗（{fast}{nw}"
    gra.nvl "你说ACLC网站？\n你是怎么知道的？{fast}{nw}"
    myworldzycpc.nvl "我的朋友 [baile] 告诉我的，看到有个链接说可以加入群聊{fast}"

    $ config.nvl_list_length = 6

    call myworld_view

    scene home_noon with pixellate
    $ another_view = False
    $ current_perspective = mc
    $ session_title = None
    # nvl clear

    gra.nvl "哦，是 [baile] 告诉你的？{fast}{nw}"
    gra.nvl "这样啊{...}{fast}{nw}"
    gra.nvl "不管怎样，总之欢迎加入 ACLC！{fast}"
    mc "{cps=*0.25}{......}{/cps}"

    call myworld_clever_box
    yangsy.comment "小事（指严重程度\n大事（指篇幅占比"
    yangsy.comment "说实话CB这段偏题剧情放在剧情开头属实有些长了\n这段可以做成中期的分支剧情（"

    return


label myworld_view:

    scene black with pixellate
    $ another_view = True
    $ current_perspective = myworldzycpc
    $ session_title = baile
    nvl clear

    myworldzycpc.nvl "听说你要做个谱子下载网站，{w=0.5}是这样吗"
    baile.nvl "嗯是的喵~"
    voice sustain
    myworldzycpc.nvl "我可以看一下你做的吗"
    baile.nvl "行喵~"
    
    myworldzycpc.nvl "这个群号，{w=0.5}我加了一下，{w=0.5}为什么被拒了"
    baile.nvl "不知道，{w=0.5}大概是不能随便进人吧喵~"
    myworldzycpc.nvl "好吧{......}"

    scene black with pixellate
    $ renpy.notify("某一天")
    nvl clear

    myworldzycpc "（[baile]不在，总觉得有点无聊）"
    myworldzycpc "（要不我再去试试加那个群吧）\n{w=1.0}（上次没通过可能是因为我没写入群消息）"

    nvl clear
    $ session_title = None
    
    system.nvl "加入群聊之前，需要先回答问题：\n{w=1.0}你是怎么知道这个群的？{nw}"
    myworldzycpc.nvl "从ACLC网站"
    "{......}"

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


label myworld_clever_box:
    
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

