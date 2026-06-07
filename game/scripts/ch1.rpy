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
            baile.nvl "可以教我怎么做吗喵~"
            myworldzycpc.nvl "当然可以"
    
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
                extend "终于收到了回复："
                system.nvl "群主拒绝了你的入群申请：\n{w=1.0}“不欢迎水军。”"
            "我朋友告诉我的":
                $ no_group_message = False
                myworldzycpc.nvl "我朋友告诉我的"
                "[myworldzycpc] 等了很久，{nw=0.5}"
                extend "终于收到了回复："
                system.nvl "群主拒绝了你的入群申请：\n{w=1.0}“不好有内鬼。”"
            "从ACLC网站":
                myworldzycpc.nvl "从ACLC网站"
                "不一会，{nw=0.25}"
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

    call to_be_continued("ch1")
        
    return
