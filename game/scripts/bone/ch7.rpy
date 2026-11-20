label bone_ch7:
    "ch7"

    yangsy.comment "漫展！Yangsy是不会来的哈哈哈（没错Yangsy线Yangsy打算从Yangsy没来漫展然后mc打算要不要去找Yangsy开始决定进线"
    yangsy.comment "mc可以选择跟某人（或者某些；Gra可以跟mwan或lingyun或三人一起行动，然后根据谁有好感来变化剧情）一起行动"
    yangsy.comment "Yangsy不熟悉漫展所以这段得别人负责了（"

    play sound "snd_screen_wipe_out.wav"
    scene black with wipeadofai

    yangsy.comment "……呃回想一下要不Yangsy还是先扩展一下Yangsy线进线部分吧（（"

    play sound "snd_screen_wipe_in.wav"
    scene bg sky with wipeadofai

    if True: # yangsy.comment "之后会填上真正的条件 大概会是mc选过任意一个Yangsy的选项就能触发这段剧情"
        mc "哦对，你们有谁见到Yangsy了吗？"
        gra "哦这个啊，她没来。"
        mc "{...}啊？"
        gra "我说她没来，再说了她之前也在咱群里说过的来着——等会你不会是没看到她发那条消息吧？"
        mc "可是——"
        gra "唉算了算了又没说所有人都要来咱几个好不容易碰个面就先别想啥杂七杂八的了逛一圈去吧来？"
        lingyun "走！"
        mc "{......}"
        "你看着[gra]一行人渐行渐远的样子{nw}"
        gra "诶不是[mc]你怎么不动弹了？"
        "沉默。"
        gra "听着。"
        "[gra]走回了你的面前，一只手搭在你的肩上。"
        gra "如果你真的在意Yangsy她的话，那就应该尊重她不打算来这里的这个选择。"
        gra "即使你能现在硬把她给拽过来的话，她说不定也不会感觉有多好受的吧？"
        mc "可是我总有种感觉——Yangsy她其实很想来漫展，也很想跟我们一起——"
        gra "既然Yangsy想来那她为什么不来？"
        lingyun "以及，Yangsy那条的消息写的也是自己“不打算来”，而不是出于什么原因“没办法来”。"
        "你略微地被吓了一跳——[gra]完全挡住了由于觉察到不对劲而原路返回查看状况的[lingyun]和[mwam]二人。"
        "[lingyun]把她的手机屏幕对准了你，不过你没去看，你也没必要确认了。"
        $ variables["yangsy_route"] = None
        menu:
            "我有一个主意":
                $ variables["yangsy_route"] = False
                mc "{......}她大概真的不想来吧。"
                gra "嗯。所以我们{nw}"
                mc "但是。"
                gra "嗯？"
                mwam "诶？"
                "你举起了自己的手机。"
                mc "谁说她来不了漫展就不能跟我们一起体验漫展了？"
                gra "等会，你这是打算{...}视频通话？"
                mc "没错。"
                gra "那我先说好——这么做可是很费流量的。"
                mc "{......}"
                gra "所以让我来。我流量管够。"
                mc "？"
                gra "毕竟你要是在这就花光流量导致回不了家会很麻烦的——好了好了咱们别站着不动了赶紧走吧？"
            "还有一种可能":
                $ variables["yangsy_route"] = True
                mc "{......}她大概真的不想来吧。"
                gra "嗯。所以我们{nw}"
                mc "但是。"
                gra "嗯？"
                mwam "诶？"
                "你抬起头来，注视着[gra]的眼睛。"
                mc "即使Yangsy真的不想来，无论出于何种原因。"
                mc "我还是能感觉到她透露出的那种的愿望，她渴望与我们见面聊天一同逛漫展什么的。"
                mc "这两者并不冲突。因为出发点不一样。"
                # "就如同为一个关卡设计合适的魔改和为一个魔改寻找合适的关卡也有区别一样，你如是想着。"
                mc "{...}Yangsy之前跟我透露过她在现实中没有朋友。一方面这导致她很希望有一个现实生活中的朋友——"
                mc "——而另一方面，她又害怕自己在互联网所表现出的形象与其现实世界中真实形象的落差，可能导致自己连网络上仅有的那些朋友都会最终失去。"
                mc "这样两难的局面她经历的太多了。所以她一直不敢迈出这一步，因为在两难的情形下保持不变是最容易的。"
                gra "{......}"
                mc "既然她不敢的话，那由我来迈出这一步就好了。"
                gra "你不怕那个落差？万一你真就因为那个落差而成为了第一个她所失去的朋友该怎么办？"
                mc "总得有人试一试的。"
                mc "以及，我相信Yangsy不是那样的人。"
                gra "{......}唉，好吧，你赢了。去找她吧。"
                mc "嗯。嗯？不对我没说我现在就要走啊我当然是跟你们一起玩完了再{nw}"
                gra "诶呀，逗你玩的你还当真了？该说是整段垮掉吗{...}好了好了咱们别站着不动了赶紧走吧？"

        yangsy.comment "好的那么让我们跳过一大段剧情（"

        play sound "snd_screen_wipe_out.wav"
        scene black with wipeadofai

    jump bone_ch8