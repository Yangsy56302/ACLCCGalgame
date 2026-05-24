label vibe_ch6:
    scene black with fade

    play music "audio/mus_setup.ogg" fadein 2.0

    "魔改圈在 ADOFAI 社区中的争议，比预想中来得更快。"

    nvl clear

    "那天，有人在 Adofai 的官方讨论区发了一篇帖子——\n标题是《魔改：创意还是破坏？》"

    "帖子被转到了群里。\n你点进去看了看，评论区已经吵成了一片。"

    "有人说魔改是对原作的不尊重，\n有人说魔改让 Adofai 失去了它原本的魅力，\n也有人在为魔改辩护。"

    lv.nvl "# 这帖子被转到好几个地方了"

    morin.nvl "我看到好多人无脑喷……气死我了"

    mc.nvl "我们要不要也去评论一下？"

    gra.nvl "不用\n去那里吵架只会让事情更糟"

    yangsy.nvl "\" 但也不能什么都不说吧！ \""

    nvl clear

    "群里的情绪开始变得微妙。\nYangysy 明显很愤怒，\n而 Gra 则坚持冷处理。\n两种态度在群里悄然对立起来。"

    scene bg group_photo with fade

    yangsy "\" Gra，我不明白\n为什么别人骂到头上了，我们还要忍着 \""

    gra "我不是说要忍。\n但去评论区对喷不是解决办法。"

    yangsy "\" 那什么是解决办法？\n等他们自己改变想法？ \""

    gra "我们做好自己的作品，自然会有人看到"

    yangsy "\" 如果没人看呢？\n如果官方下场封杀呢？ \""

    gra "……那就到时候再说"

    "气氛有些僵。\n你第一次看到群里的两个核心人物产生这么大的分歧。"

    mc "我能说一句吗……"

    "两人都停了下来，等着你说话。"

    menu:
        "我支持 Gra——做好作品就是最好的回应":
            $ support_gra = True
            $ support_yangsy = False
            mc "我觉得 Gra 说得对……\n去吵架解决不了问题\n不如把精力放在创作上"

            gra "嗯"

            yangsy "\" ……好吧\n反正我就是咽不下这口气 \""

        "我觉得 Yangsy 说得有道理——不能沉默":
            $ support_gra = False
            $ support_yangsy = True
            mc "但是 Yangsy 也有道理……\n完全沉默的话，别人只会当我们好欺负"

            yangsy "\" 对吧！ \""

            gra "我不是说要沉默……\n只是要选对方式"

            "你点了点头，但心里也没想清楚到底什么方式才是对的。"

        "我理解两边，但希望大家别因为这个吵架":
            $ support_gra = False
            $ support_yangsy = False
            mc "我理解两边的心情……\n但不管怎么回应，我们都别因为这个影响群里的氛围"

            gra "……你说得对"

            yangsy "\" 嗯……我也不是要吵架\n就是气不过 \""

    nvl clear

    scene black with fade

    "这场争论没有真正的赢家。\n帖子还在发酵，\n网上的争议还在继续。"

    "但比外界的争议更让你在意的，\n是群里那种微妙的氛围变化。"

    nvl clear

    "以前大家聊天的时候，总是嘻嘻哈哈的。\n现在，每次提到\"魔改\"两个字，\n群里就会不自觉地安静一会儿。"

    "像一根弦，\n在不知不觉中被绷紧了。"

    scene bg group_photo with fade

    '几天后，又有一件事发生了——\n一个知名 Adofai 主播在直播时公开表示\n"魔改就是邪道，毁了这款好游戏"。'

    "这个消息像一颗炸弹，在所有魔改群里炸开了。\nACLC 也不例外。"

    morin "……这人粉丝好多的"

    lv "# 他的视频播放量也很夸张"

    mwam "……"

    mc "mwam，你怎么看？"

    mwam "我不知道……\n我只是个做音效的"

    "mwam 的回答让你有些意外。\n她似乎不想站队，\n只是默默地做自己的事。"

    "但你注意到，那天之后她更少在群里说话了。"

    stop music fadeout 3.0

    scene black with fade

    "外面的声音越来越大。\n群里的空气越来越沉重。\n而真正的风暴，\n才刚刚开始酝酿。"

    jump vibe_ch7
