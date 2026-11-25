label ch3:
    if variables["volunteer_to_do_curse"]:
        call ch3_do_curse from _call_ch3_do_curse
    else:
        call ch3_dont_do_curse from _call_ch3_dont_do_curse
    
    return


label ch3_do_curse:
    
    play sound "snd_screen_wipe_in.wav"
    scene bg home_night with wipeadofai
    
    $ quick_menu = True
    nvl clear
    mc.nvl "我真的想不出来什么主意……"
    gra.nvl "那要不就先暂时不想了\n{w=1.0}我们给你一些现成的魔改效果，{w=0.5}你用它去魔改一张现成的谱面"
    gra.nvl "这样如何？"
    myworldzycpc.nvl.comment "话说你是不是忘了我也是新来的（"
    yangsy.nvl.comment "没忘，{w=0.25}所以Yangsy换人说了（（"
    yangsy.nvl "好主意啊Gra"
    yangsy.nvl "咱们也有段时间没做过多效果魔改了\n{w=0.5}毕竟都在给自己的系列构思新魔改效果（"
    gra.nvl "[[nfgtr.zip]{fast}{w=1.0}这是[yangsy]做的复合魔改的一个例子，{w=0.25}你可以看看{w=1.0}{nw}"
    
    menu(nvl=True):
        "保存文件…":
            if renpy.variant("pc"):
                $ CopyToAnyway("UnknowFile","UnknowFile")
            elif renpy.variant("android"):
                python:
                    for attempt in range(3):
                        if is_external_storage_manager():
                            break
                        request_all_files_access()
                        renpy.pause(2.0)
                if is_external_storage_manager():
                    $ release_file_quietly("UnknowFile","UnknowFile")
                else:
                    $ release_file_quietly("UnknowFile","UnknowFile")
                # 先这么写，以后按剧情来改
            pass

    gra.nvl "怎么样，是不是对复合魔改有一定了解了？"
    mc.nvl "感觉还是有些难"
    yangsy.nvl "要不 {w=0.5}再削弱一下？"
    gra.nvl "那就单独挑个做起来简单些的魔改来用吧"
    mc.nvl "好的"
    yangsy.nvl "要是还有问题的话在群里问就行 Yangsy一直都在（"

    return


label ch3_dont_do_curse:
    
    play sound "snd_screen_wipe_in.wav"
    scene bg home_night with wipeadofai
    
    $ quick_menu = True
    nvl clear
    nona.nvl "[[level.zip]\n{w=1.0}我的新魔改做好了！\n{w=1.0}哪个好宝宝帮我测试一下呀"
    yangsy.nvl "Yangsy试试？（"
    nona.nvl "谢谢Yangsy！\n{w=1.0}我喜欢你！"
    myworldzycpc.nvl.comment """
    下面这两行后续剧情可以用，主角就怃说喜欢这件事询问的时候，这里先埋个伏笔"
    \nmc.nvl "？？？"
    \ngra.nvl "哈，这是[nona]的习惯用语而已，别误会了（"
    """

    return
