label ch1:
    scene black with dissolve
    $ another_view = True
    myworldzycpc.comment "我要写主线了吗{...}冲突了怎么办呢{...}"
    myworldzycpc.comment "先写个简单的吧，{w=0.5}后续再慢慢改"

    nvl clear
    $ session_title = baile

    myworldzycpc.nvl "听说你要做个谱子下载网站，{w=0.5}是这样吗"
    baile.nvl "嗯是的喵~"
    voice sustain
    menu(nvl=True):
        "可以看一下你做的吗":
            myworldzycpc.nvl "我可以看一下你做的吗"
            baile.nvl "行喵~"
        "可以教我怎么做吗":
            myworldzycpc.nvl "可以教我怎么做吗喵~"
            baile.nvl "当然可以"
    
    myworldzycpc.nvl "这个群号，{w=0.5}我加了一下，{w=0.5}为什么被拒了"
    baile.nvl "不知道，{w=0.5}大概是不能随便进人吧喵~"
    myworldzycpc.nvl "好吧{......}"
    $ no_group_message = True


    while True:

        $ current_perspective = myworldzycpc

        "有一天，{w=0.5}[baile] 不在，{w=0.5}[myworldzycpc] 觉得有点无聊。"
        myworldzycpc "（要不我再去试试加那个群吧）"
        if no_group_message:
            myworldzycpc "（上次没通过可能是因为我没写入群消息）"
        # yangsy.comment '这里的描述与后面的"[myworldzycpc]没有写入群消息。"冲突，所以Yangsy删了（'
        "[myworldzycpc]又试了一次。"

        nvl clear
        $ session_title = None

        system.nvl "加入群聊之前，需要先回答问题：\n{w=1.0}你是怎么知道这个群的？{nw}"

        menu(nvl=True):
            "我在网上看到的":
                $ no_group_message = False
                myworldzycpc.nvl "我在网上看到的"
                "[myworldzycpc] 等了很久，{nw=0.5}"
                voice "voice/message_prompt.ogg"
                extend "终于收到了回复："
                system.nvl "群主拒绝了你的入群申请：\n{w=1.0}“不欢迎水军。”"
            "我朋友告诉我的":
                $ no_group_message = False
                myworldzycpc.nvl "我朋友告诉我的"
                "[myworldzycpc] 等了很久，{nw=0.5}"
                voice "voice/message_prompt.ogg"
                extend "终于收到了回复："
                system.nvl "群主拒绝了你的入群申请：\n{w=1.0}“不好有内鬼。”"
            "从ACLC网站":
                myworldzycpc.nvl "从ACLC网站"
                "不一会，{nw=0.25}"
                voice "voice/message_prompt.ogg"
                extend "[myworldzycpc] 的入群申请就被通过了。"
                system.nvl "你已经是群成员了"
                gra.nvl "你说ACLC网站？{w=1.0}你是怎么知道的？"
                myworldzycpc.nvl "我的朋友 [baile] 告诉我的，{w=0.5}看到有个链接说可以加入群聊"
                gra.nvl "哦，{w=0.25}是 [baile] 告诉你的？"
                gra.nvl "这样啊{...}"
                gra.nvl "不管怎样，{w=0.5}总之欢迎加入 ACLC！"
                jump ch1_baick
            "[' '*80]":
                $ no_group_message = True
                "[myworldzycpc] 没有写入群消息。"
                "[myworldzycpc] 等了很久，{nw=0.5}"
                voice "voice/message_prompt.ogg"
                extend "终于收到了回复："
                system.nvl "群主拒绝了你的入群申请"

label ch1_baick:

    nvl clear
    $ session_title = baile
    baile.nvl "我是后背喵~"
    baile.nvl "{......}"
    baile.nvl "bro怎么进ACLC了喵？"

    $ another_view = False
    $ current_perspective = mc
    scene bg star with dissolve

    call show_chapter("第二天")

    "又是一天，{w=0.5}你迫不及待的打开了群聊。"

    nvl clear
    $ session_title = None
    system.nvl "[myworldzycpc]加入了群聊{fast}"
    gra.nvl "你说ACLC网站？你是怎么知道的？{fast}"
    myworldzycpc.nvl "我的朋友 [baile] 告诉我的，看到有个链接说可以加入群聊{fast}"
    gra.nvl "哦，是 [baile] 告诉你的？{fast}"
    gra.nvl "这样啊{...}{fast}"
    gra.nvl "不管怎样，总之欢迎加入 ACLC！{fast}"
    mc "{cps=*0.25}{......}{/cps}"

    myworldzycpc.nvl "另外我还在摆了的Clever Box地图介绍里看到了群号呢"
    gra.nvl "什么？你说Clever Box？"
    gra.nvl "CB在哪发介绍了？"
    myworldzycpc.nvl "没有，地图正处于开发阶段，而且这个群号在他B站个人简介也有"
    mwam.nvl "到底是cb还是sb（）"
    maoyuna.nvl "ccb"
    gra.nvl "cb"
    gra.nvl "那你是从哪进来的？"
    myworldzycpc.nvl "ACLC网站啊"
    gra.nvl "已畏惧。"
    myworldzycpc.nvl "qwq"
    gra.nvl "据我推测你应该会写数据包"
    myworldzycpc.nvl "会一点吧"
    gra.nvl "你会写碰撞模拟和抛物线吗"
    myworldzycpc.nvl "这是什么东西"
    gra.nvl "那没事了"
    gra.nvl "那你会写什么"
    myworldzycpc.nvl "我不确定，大概得说说我才知道会不会写"
    myworldzycpc.nvl "如果要抛物线的话，大概可以用带Motion的箭模拟一下？"
    gra.nvl "你看过CB的代码吗"
    myworldzycpc.nvl "看过，而且有一部分是我写的"
    gra.nvl "比如？"
    myworldzycpc.nvl "函数、各种json，比如选关、机关之类的吧"
    gra.nvl "说点大家不知道的"
    gra.nvl "其实我还没看过CB，我对CB的唯一了解就是推箱子基本逻辑是我写的"
    myworldzycpc.nvl "我还以为是摆了写的呢"
    gra.nvl "他他妈根本不会写"
    myworldzycpc.nvl "？？"
    myworldzycpc.nvl.comment "？？？"
    gra.nvl "[[摆了写的地图代码，包含循环清除活塞掉落物的代码]\n摆了力作"
    yangsy.nvl "全世界的活塞掉落物瞬间神秘失踪\n这究竟是人性的扭曲还是道德的沦丧（"
    myworldzycpc.nvl "好在这个世界上一般不会出现活塞掉落物"
    gra.nvl "明显就是，啥也不会"

    baile.nvl "是这样的"
    baile.nvl "我是废物"
    baile.nvl "ok"
    myworldzycpc.nvl "啊这，不要啊qwq"
    lingyun.nvl "66"
    hale.nvl "盐都不盐了"
    baile.nvl "是这样的"
    baile.nvl "嗯"

    myworldzycpc.nvl.comment "-------分割线------"

    myworldzycpc.nvl "qwq，听说你们有个MC服务器？"
    gra.nvl "是的，欢迎你来玩"

    call to_be_continued("ch1")
        
    return
