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
    
    yangsy.nvl "[mc.nvl]起的还挺早的\n{w=0.5}群里大部分成员现在这个时候都还在补觉呢（"

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
    
    jump ch1_before_myworld_view


label ch1_before_myworld_view:

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

    jump ch1_myworld_view


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

    jump ch1_after_myworld_view


label ch1_after_myworld_view:

    scene home_noon with pixelate
    $ another_view = False
    $ current_perspective = mc
    $ session_title = None
    nvl clear
    nvl show

    gra.nvl "哦，是 [baile] 告诉你的？{fast}{nw}"
    gra.nvl "这样啊{...}{fast}{nw}"
    gra.nvl "不管怎样，总之欢迎加入 ACLC！{fast}"
    mc "{cps=*0.25}{......}{/cps}"

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
    yangsy.comment "小事（指严重程度\n大事（指篇幅占比"
    yangsy.comment "说实话CB这段偏题剧情放在剧情开头属实有点长了 可以做成中期的分支剧情（"

    jump ch2



label ch2:

    yangsy.comment "Yangsy觉得有必要在这里分一下章节（"
    yangsy.comment "以及这里的剧情Yangsy还没动过，之后再说（"

    scene bg sky with fade
    nvl clear

    menu:
        "也许是时候了解一下群内的情况了，你想直接问还是先观望一会呢？"
        "直接问":
            mc.nvl "话说，我好像还不太认识你们呢，也对这个群的历史不太了解"
            myworldzycpc.nvl "我也是…"
            gra.nvl "没关系，我们给你介绍一下"
            gra.nvl "首先这个群呢"
            gra.nvl "是当初Yangsy…"
            yangsy.nvl "(嘘{...})"
            gra.nvl "是一群对魔改都感兴趣的人，彼此聚在一起，构成的一个社区"
            gra.nvl "首先是Yangsy，她是我们这个社区的前身，没有她就不可能有我们这个社区，她的魔改系列叫做“{rb}文字魔改{/rb}{rt}String Curse{/rt}”。"
            mc.nvl "文字…魔改？"
            gra.nvl "是的，魔改有许多许多的系列，而每个系列都有它的名字，这样我们就可以区分来自不同人的魔改了。"
            gra.nvl '同样的，体现在关卡名上，就是用各种符号来表示，我们把它叫做“魔改标识符”。比如Yangsy做的1-X文字魔改，加上标识符就是\n{color=#ffffcc}{i}"1-X" 冰与火之舞，但判定限制是变化之神{/i}{/color}'
            mc.nvl "这样啊…"
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
        "观望":
            $ overwatch_first = True
            nona.nvl "我的新魔改做好了，哪个好宝宝帮我测试一下呀"
            yangsy.nvl "👌"
            nona.nvl "我喜欢你！"
            myworldzycpc.nvl.comment """
            下面这两行后续剧情可以用，主角就怃说喜欢这件事询问的时候，这里先埋个伏笔"
            \nmc.nvl "？？？"
            \ngra.nvl "哈，这是[nona]的习惯用语而已，别误会了（"
            """

    gra.nvl "{color=#0080FF}@[mc]{/color} 诶，话说你要不要做个魔改试试水？"
    mc.nvl "我？"
    gra.nvl "对啊，既然来到了这里，就试着融入我们吧"
    yangsy.nvl "我们很期待你做出自己的作品"
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

    scene bg sky with fade

    "时间过得飞快，不久就到了[gra]的生日了。"

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
    

    call to_be_continued("ch1") from _call_to_be_continued_1
        
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
