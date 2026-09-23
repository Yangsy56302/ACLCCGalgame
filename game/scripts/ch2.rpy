label ch2:

    scene bg sky with fade

    yangsy.comment "Yangsy觉得有必要在这里分一下章节（"
    yangsy.comment "以及这里的剧情Yangsy还没动过，之后再说（"

    nvl clear
    
    mc "（也许{w=0.5}是时候了解一下群内的情况了......）{nw}"
    $ overwatch_first = None
    menu:
        "（也许是时候了解一下群内的情况了......）{fast}"
        "询问群内成员":

            $ overwatch_first = False
            window hide
            nvl show

            mc.nvl "话说，{w=0.25}我好像还不太认识你们呢，{w=0.5}也对这个群的历史不太了解"
            myworldzycpc.nvl "我也是{...}"
            gra.nvl "没关系 {w=0.5}我们给你介绍一下"
            gra.nvl "首先这个群呢\n{w=0.5}是当初Yangsy"
            yangsy.nvl "咳咳（明示"
            gra.nvl "是一群对魔改都感兴趣的人\n{w=0.5}彼此聚在一起\n{w=0.5}构成的一个社区"
            nvl clear
            gra.nvl "首先是Yangsy"
            gra.nvl "她是我们这个社区的重要人物\n{w=1.0}没有她就不可能有我们这个社区"
            gra.nvl "她的魔改系列也是我们现在很多成员能够最终聚集在此的原因"
            gra.nvl "那个系列叫做“{rb}文字魔改{/rb}{rt}String Curse{/rt}”"
            mc.nvl "文字{...}魔改？"
            yangsy.nvl "嗯 {w=0.25}没错（"
            gra.nvl "魔改有许多许多的系列 {w=0.5}而每个系列都有它的名字\n{w=1.0}这样我们就可以区分来自不同魔改作者的魔改了"
            gra.nvl "体现在形象上时 {w=0.5}来自不同魔改系列的魔改会用不同外观的装饰物来表示"
            yangsy.nvl "Yangsy用文字作为形象{w=0.25}主要是为了避免画装饰物导致的额外时间成本（"
            gra.nvl "同样的 {w=0.25}体现在关卡名上时 {w=0.5}就是用各种符号来表示\n{w=1.0}我们把它叫做“魔改标识符”"
            gra.nvl '比如Yangsy为1-X关卡做的魔改：{w=0.5}{color=#ffffcc}{i}1-X 冰与火之舞，但判定限制是变化之神{/i}{/color}\n{w=1.0}加上标识符就是{color=#ffffcc}{i}"1-X" 冰与火之舞，但判定限制是变化之神{/i}{/color}'
            mc.nvl "这样啊{...}"
            voice "voice/crab_mine_and_qing/prelude.ogg"
            lv.nvl "{nw}"
            $ nvl_erase()
            voice "voice/crab_mine_and_qing/1.ogg"
            extend "{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}螃蟹? 地雷* 还有<晴小姐3 ~{/i} 🎵{nw}"
            voice "voice/crab_mine_and_qing/2.ogg"
            lv.nvl '{a=https://www.bilibili.com/video/BV1qNUmYRE8v}🎵 {i}"文字" 萝卜 还有火柴人 ~{/i} 🎵{nw}'
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

        "暗中观察":
            $ overwatch_first = True
            window hide
            nvl show

            nona.nvl "[[level.zip]\n{w=1.0}我的新魔改做好了！\n{w=1.0}哪个好宝宝帮我测试一下呀"
            yangsy.nvl "Yangsy试试（"
            nona.nvl "谢谢Yangsy！\n{w=1.0}我喜欢你！"
            myworldzycpc.nvl.comment """
            下面这两行后续剧情可以用，主角就怃说喜欢这件事询问的时候，这里先埋个伏笔"
            \nmc.nvl "？？？"
            \ngra.nvl "哈，这是[nona]的习惯用语而已，别误会了（"
            """

    gra.nvl "{color=#0080FF}@[mc]{/color} 诶，话说你要不要做个魔改试试水？"
    mc.nvl "我？"
    gra.nvl "对啊，既然来到了这里，就试着融入我们吧"
    yangsy.nvl "我们很期待你做出自己的作品"
    yangsy.nvl.comment "不是等会让才进群两天还啥都没学会的新人去做魔改也有点太离谱了吧（"
    dwen.nvl "也许会有我们都想不到的点子呢"

    menu(nvl=True):
        "好的，我会尝试去做的":
            $ volunteer_to_do_curse = True
            mc.nvl "好的，我争取做出属于自己的魔改作品"
            myworldzycpc.nvl "😰"
            mc.nvl "话说…可以教我怎么做吗？"
            gra.nvl "魔改没有一成不变的做法，主要得看创造力"
            mc.nvl "但我连怎么该音乐都不会呢"
            gra.nvl "emm"
            gra.nvl "用你自己的方式就行，方式远不止一种，现在互联网这么发达，有什么问题不能上网解决呢…"
            nona.nvl "是啊，我还在用Au改音乐呢"
            yangsy.nvl "你那是特例（"

            if not overwatch_first:
                mc.nvl "话说，刚刚听小绿君说的那些，感觉好可怕…"
                gra.nvl "没关系的，做魔改踩坑是很正常的，你问问这些作者，好多人都或多或少踩过坑、撞过魔改创意呢？"
                mc.nvl "这样吗…"

                menu(nvl=True):
                    "那我还是不做了吧…" if not overwatch_first:
                        call ch2_dont_curse from _call_ch2_dont_curse
                    "我会试试的":
                        mc.nvl "你说的有道理，我会试试的。"
                        gra.nvl "嗯，希望你能在踩坑的过程中不断学习，走过这段坑坑洼洼的路，迎接你的将是光明大道。"
                        call ch2_do_curse from _call_ch2_do_curse
            else:
                menu(nvl=True):
                    "我会试试的":
                        mc.nvl "我会试试的。"
                        gra.nvl "太好了，希望你早日做出自己的魔改"
                        call ch2_do_curse from _call_ch2_do_curse_1

        "我暂时还不太想做":
            call ch2_dont_curse from _call_ch2_dont_curse_1

    call gra_birthday

    call to_be_continued("ch2") from _call_to_be_continued_2
        
    return


label gra_birthday:

    scene bg sky with fade

    "时间过得飞快，不久就到了[gra]的生日了。"
    yangsy.comment "不是等会这才两天剧情就开始加速了？别啊（"
    # return

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


label ch2_dont_curse:

    mc.nvl "算了，我暂时还不太想做，我现在只想好好享受这个社区，和大家在一起就够了"
    gra.nvl "没关系，就算不做魔改，我们也一样欢迎！"
    myworldzycpc.nvl "太好了，吓得我都不敢说话了…"
    yangsy.nvl "至于吗…\n[['''.gif]"

    return


label ch2_do_curse:

    scene black with fade

    nvl clear
    mc.nvl "可是我真的想不出来什么主意啊"
    myworldzycpc.nvl "要不我们给你一些现成的魔改效果，你来试着应用到一个谱面上？"
    myworldzycpc.nvl.comment "话说你是不是忘了我也是新来的（"
    yangsy.nvl "正好咱们好像也有段时间没这么做了"
    yangsy.nvl "毕竟大家都在做新魔改效果（"
    gra.nvl "这是[yangsy]做的复合魔改的一个例子，你可以看看"
    menu(nvl=True):
        "保存文件…":
            if renpy.variant("pc"):
                $ CopyToAnyway("UnknowFile","UnknowFile")
            elif renpy.variant("android"):
                while not is_external_storage_manager():
                    $ request_all_files_access()
                    $ renpy.pause(2.0)
                $ release_file_quietly("UnknowFile","UnknowFile")
            pass

    gra.nvl "怎么样，是不是对复合魔改有一定了解了？"

    return
