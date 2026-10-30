label ch2:
    if variables["volunteer_to_do_curse"]:
        call ch2_do_curse
    else:
        call ch2_dont_do_curse
    
    call to_be_continued("ch2") from _call_to_be_continued_2


label ch2_do_curse:
    
    scene bg home_night with fade

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
                $ CopyToAnyway("UnknowFile", "UnknowFile")
            elif renpy.variant("android"):
                while not is_external_storage_manager():
                    $ request_all_files_access()
                    $ renpy.pause(2.0)
                $ release_file_quietly("UnknowFile", "UnknowFile")
            pass

    # gra.nvl "怎么样，是不是对复合魔改有一定了解了？"
    mc.nvl "感觉还是有些难"
    yangsy.nvl "要不 {w=0.5}再削弱一下？"
    gra.nvl "那就单独挑个做起来简单些的魔改来用吧"
    mc.nvl "好的"
    yangsy.nvl "要是还有问题的话在群里问就行 Yangsy一直都在（"

    return


label ch2_dont_do_curse:
    
    scene bg home_night with fade

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


label gra_birthday:

    scene bg sky with fade

    "时间过得飞快，不久就到了[gra]的生日了。"
    yangsy.comment "不是等会这才两天剧情就开始加速了？别啊（"
    $ _history_list.pop()
    $ _history_list.pop()
    "今天是[gra]的生日。"
    yangsy.comment "这段还没改，不过其实也没啥改的必要，挪一下剧情位置就行（"

    nvl clear
    gra.nvl "是时候发我的生日作了"
    yangsy.nvl "诶Gra生日到了？"

    myworldzycpc.nvl.comment "下文部分摘自生日作"
    lingyun.nvl "快生"
    hale.nvl "晴柚生日快乐"
    nona.nvl "生日快乐，我喜欢你"
    image gra_birthday grass = Transform('images/icon/gra_birthday/grass.png', zoom=0.25)
    grass.nvl "{size=*1.5}生日快乐\n{image=gra_birthday grass}"
    gra.nvl "哇，谢谢[grass]！"
    yangsy.nvl "祝 [gra] 生日快乐，并且这辈子能在现实中与不是重度病娇的晴小姐相遇相爱相伴一生"
    ashell.nvl "还记得那次，我突发奇想，想做官谱魔改，是你指引我着方向，在我迷茫的时候对我伸出援手，即使后面出了些小插曲你也不生气，多谢你这么多天的陪伴。祝你之后的每一天都会如此美好，祝我们ACLC的各位群友的友谊能够长长久久"
    morin.nvl "祝我们的瓜服梯克斯（Grafrustix）生↑日↗快↘乐→~\n{color=#808080}省略若干行{/color}\n∴ 综上所述，祝Grafrustix生日快乐"
    uni.nvl "柚子生了!!!"
    maoyuna.nvl "我在地球，我是人类，我要说话了，G开头的字母哥话话话话话话话，然后震撼nm"
    lv.nvl "生日快乐呀\n愿你{......}呃呃好吧没什么想祝福的\n给你留个{color=#FF0000}省略号{/color}\n这里面有我想说的\n但是被省略了！"
    nvl clear
    image gra_birthday baile = Transform('images/icon/gra_birthday/baile.png', zoom=0.5)
    baile.nvl "{image=gra_birthday baile}"
    yoosee.nvl "生日快乐\n祝你明天不会死\n明天的明天也不会死\nwhile {rb}{u}true{/u}{/rb}{rt}[[原文如此]{/rt}"
    pumi.nvl "日了什么时候快生\n以及\n#1.2*大天空转adofai when"

    return
