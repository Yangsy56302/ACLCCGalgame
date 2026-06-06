label ch1:
    scene black with dissolve
    # $ another_view = True
    myworldzycpc.comment "我要写主线了吗…冲突了怎么办呢…"
    myworldzycpc.comment "先写个简单的吧，后续再慢慢改"

    myworldzycpc "听说你要做个谱子下载网站，是这样吗"
    baile "嗯是的喵~"
    menu:
        "可以看一下你做的吗":
            myworldzycpc "我可以看一下你做的吗"
            baile "行喵~"
        "可以教我怎么做吗":
            baile "可以教我怎么做吗喵~"
            myworldzycpc "当然可以"
    
    myworldzycpc "这个群号，我加了一下，为什么被拒了"
    baile "不知道，大概是不能随便进人吧喵~"
    myworldzycpc "好吧{......}"

label ch1_bored:

    $ current_perspective = myworldzycpc

    "有一天，[baile]不在，[myworldzycpc]觉得有点无聊"
    myworldzycpc "（要不我再去试试加那个群吧）"
    myworldzycpc "（上次没通过可能是因为我没写入群消息）"
    "[myworldzycpc]又试了一次，这次写了入群消息。"
    "入群消息问的是：“你是怎么知道这个群的？”"

    nvl clear

    menu:
        "我在网上看到的":
            myworldzycpc.nvl "我在网上看到的"
            "[myworldzycpc]等了很久，终于收到了回复："
            "群主拒绝了你的入群申请，并回复说：“不欢迎水军。”"
            jump ch1_bored
        "我朋友告诉我的":
            myworldzycpc.nvl "我朋友告诉我的"
            "[myworldzycpc]等了很久，终于收到了回复："
            "群主拒绝了你的入群申请，并回复说：“不好有内鬼。”"
            jump ch1_bored
        "从ACLC网站":
            myworldzycpc.nvl "从ACLC网站"
            "不一会，[myworldzycpc]的入群申请就被通过了。"
            gra "你说ACLC网站？你是怎么知道的？"
            myworldzycpc "我的朋友[baile]告诉我的，看到有个链接说可以加入群聊"
            gra "哦，是 [baile] 告诉你的？"
            gra "这样啊…"
            gra "不管怎样，总之欢迎加入 ACLC！"
        " ":
            "[myworldzycpc]没有写入群消息。"
            "[myworldzycpc]等了很久，终于收到了回复："
            "群主拒绝了你的入群申请，并什么都没有回复。"
            jump ch1_bored

    baile "我是后背喵~"
    baile "{......}"
    baile "bro怎么进ACLC了喵？"

    while True:
        stop music fadeout 1.0
        scene black with dissolve
        menu:
            "查看已被废弃的AI剧情":
                jump vibe_ch2
            "查看[yoosee]的建议":
                call chplotadvice_yoosee
            "查看[yangsy]的建议":
                call chplotadvice_yangsy
            "返回主菜单":
                return
        
    return