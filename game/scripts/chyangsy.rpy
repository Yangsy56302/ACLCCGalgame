label chyangsy_1:

    scene home_night with dissolve

    # "回想到之前做魔改谱的时候时不时就需要到群里求助，\n{w=0.5}然后目睹着自己的信息分分钟被其他成员的信息冲走的情景{...}"
    "你决定去加[yangsy.nvl]的QQ好友。"
    # "毕竟在你的印象中，\n{w=0.5}她是ACLC成员中少数既愿意帮忙也有能力帮忙的成员。"
    "不知道为什么，{w=0.5}但你总感觉，\n{w=0.5}相比于[gra.nvl]而言，{w=0.5}跟[yangsy.nvl]聊天时你会更放得开一些。"
    "可能是她那种对谁都一样的自来熟性格导致的吧。"
    # "和她成为QQ好友之后，{w=0.5}你的求助消息就不会再被群内的信息流冲走了。"
    # "……或许，{w=0.25}在遇到其他困难的时候，{w=0.5}也能去找她倾诉？"
    "说不定，哪天自己也去做魔改关卡的话，还能直接找她求助呢？"
    
    nvl clear

    system.nvl "请输入验证信息：{fast}{w=1.0}{nw}"
    mc.nvl "我是ACLCC群的[mc.nvl]"

    mc "{......}"
    "当然，{w=0.25}这些天来在群里与[yangsy.nvl]相处的回忆使你很清楚一件事——\n{w=0.5}那就是她平时的反射弧，{w=0.5}据粗略估计，{w=0.25}足以绕地球三圈。"
    "一直在这里等着她接受好友邀请显然是不现实的；\n{w=1.0}与其坐在屏幕前干等着浪费光阴，{w=0.5}还不如去找点其他事情做做。"
    "你打消了刚刚冒出的找她求助的念头。\n{w=1.0}有这时间等着她的话，{w=0.5}只凭自己摸索估计都更有可能误打误撞先把问题给解决掉。"

    scene black with dissolve

    "{......}"

    scene home_midnight with dissolve

    system.nvl "以上为验证消息{fast}{nw}"
    yangsy.nvl "我们已成功添加为好友，现在可以开始聊天啦～{fast}{nw}"

    yangsy.nvl "抱歉 {w=0.5}一下午都没检查消息（（（"
    mc.nvl "没关系的"
    yangsy.nvl "话说[mc.nvl]你竟然特地来加Yangsy好友了\n{w=1.0}是有什么事嘛？（"
    mc.nvl "现在还没有"
    mc.nvl "就是觉得以后遇到需要找你求助的情况的话私聊会方便些"
    yangsy.nvl "啊原来是这个原因吗（"
    yangsy.nvl "那到时候有问题的话就来找Yangsy吧\n{w=1.0}Yangsy很乐意提供帮助:3"

    mc.nvl ":3是？"
    yangsy.nvl "诶？"
    yangsy.nvl "[mc.nvl]既然看不出来嘛（\n{w=1.0}试试把手机转个270°再看？"
    mc.nvl "可是我现在用的是电脑"
    yangsy.nvl "啊这"
    yangsy.nvl "算了Yangsy还是直说吧 {w=0.25}这是个猫猫笑脸（"
    yangsy.nvl "冒号是两只眼睛 {w=0.5}阿拉伯数字三是嘴巴\n{w=1.0}现在能看出来了吧？"
    mc.nvl "看出来了，{w=0.5}不过为什么要用猫呢？"
    yangsy.nvl """
    这个嘛 {w=0.5}其实有两个原因
    
    一个是因为猫猫可爱\n{w=1.0}至于另一个 {w=0.5}还记得Firestix吗？
    
    他的Steam头像是他自己画的一只猫\n{w=0.5}这猫的表情就是用:3代替的（
    """
    mc.nvl "这样啊"
    mc.nvl "感觉原因很像Grafrustix\n{w=1.0}她之前说过她的名字是Grapefruit和Firestix的合成词来着"
    yangsy.nvl "毕竟地位摆在那嘛（"

    yangsy.nvl "总之要是没事的话Yangsy就去找点其他事情干了（"
    mc.nvl "嗯"

    yangsy.comment "此处插入一些mc的感想 Yangsy对mc不熟所以就先跳了（（"

    # return

    jump chyangsy_2


label chyangsy_2:

    scene home_night with dissolve

    mc.nvl "{at=[yangsy.nvl]} 求助{fast}{nw}"
    mc.nvl "[[文件] level.zip{fast}{nw}"
    mc.nvl "我从你的魔改关卡里借用了一些文本装饰，{w=0.5}但这些字看上去不知道为什么要比在你的关卡里时小得多{fast}{nw}"
    mc.nvl "[[图片] QQ20240727-192107.png{fast}{nw}"
    mc.nvl "[[图片] QQ20240727-192341.png{fast}{nw}"
    mc.nvl "明明是直接复制粘贴的，{w=0.5}参数一个都没动过，{w=0.5}但就是不一样"
    mc.nvl "请问你能帮我看一看吗？"

    "本来想在群里求助的你{w=0.25}发现大家都在讨论着些你看不太懂的东西，\n{w=0.5}不太敢打扰到对话的你只好退而求其次单独找[yangsy.nvl]求助。"
    "当然，{w=0.25}在这期间你也没闲着——\n{w=1.0}文本大小不对也妨碍不了你先把该展示的文本给填上。"
    "实在等不到答复的话，{w=0.5}你也可以自己重新调整大小，\n{w=0.5}反正只要看着与原来差不多大就没问题——"
    "有点出乎你意料的是，{w=0.5}[yangsy.nvl]竟然很快就回信了。"

    yangsy.nvl """
    哦这个啊

    Yangsy之前也遇到过这个问题来着（
    
    咳咳 是这样的\n{w=0.5}
    冰与火之舞出于某种原因是基于初始镜头缩放来计算固定大小装饰物的显示大小\n{w=1.0}
    因此如果两个关卡的初始镜头缩放不一致 {w=0.5}那么装饰物的显示大小也会不一致
    """
    mc.nvl "[yangsy.nvl]的解决方案是？"
    yangsy.nvl "把自己所做的所有关卡的初始镜头缩放都统一设置为默认值 {w=0.25}也就是100%"

    "得知解决方案的你迅速回到了编辑器，\n{w=0.5}然后将关卡设置的镜头缩放{w=0.25}从原本的150%{w=0.25}调整到10{nw}"
    $ _history_list.pop()
    "得知解决方案的你迅速回到了编辑器，\n然后{fast}意识到{w=0.25}如果这样做的话{w=0.25}关卡开始时的缩放就会与原关卡的不一致。"
    "于是你决定去找[yangs.nvl]讨个说法{nw}"

    with None
    nvl show

    yangsy.nvl "如果有需要设置初始镜头缩放的情况 {w=0.5}就在第0块砖放一个时长为0拍子的镜头移动事件来设置"
    
    mc "{...}"
    mc "（原来是我漏看消息了吗……）"
    yangsy.comment "换位思考说是（"

    "你又回到了编辑器，{w=0.5}按照[yangsy.nvl]的完整指示设置了参数和事件，{w=0.5}然后播放了一遍关卡开头以确保没有问题。"
    "做完这些之后，{w=0.5}你切回到了QQ界面。"

    mc.nvl "谢谢"
    yangsy.nvl "不用谢（"

    yangsy.nvl "其实这点挺不直观的 {w=0.5}Yangsy当时也是摆弄了好一会儿才知道原因（"
    yangsy.nvl "只能说 {w=0.25}7BG在这方面的脑回路确实很{......}清奇（（\n{w=1.0}该说不愧是7th Bug Games吗（（（"

    yangsy.nvl.comment "下面这段等mc的设定确定下来之后可能得改（"
    yangsy.nvl "哦对 关卡做的挺不错的（"
    mc.nvl "诶，{w=0.25}真的？"
    yangsy.nvl "第一次做魔改能做到这个水平其实已经超过包括Yangsy在内的很多人了"
    if variables["gra_chemistry_name"] is True:
        yangsy.nvl "Gra说的果然没错（"
    mc.nvl "谢谢"
    yangsy.nvl "都说了不用谢了啦（（"
    yangsy.nvl.comment "以上"

    yangsy.comment "这次同样暂时跳过感想（"

    return
