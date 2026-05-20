# 向导 by 祐荽


init python:
    import os
    import time
    import string
    import unicodedata


label guide_naming_start:
    
    scene black with fade
    
    qqq "{......}噢，{w=0.25}嘿，{w=0.25}你好。"

    # 如果已经选择了一个名字：
    if persistent.name_mc:
        qqq "等等，{w=0.5}我认得你。"
        qqq "你的名字是不是{......}算了，{w=0.25}我还是叫你玩家吧。"
        qqq "不知道为什么，{w=0.5}直呼别人的名字会让我有种{w=0.5}奇怪的羞耻感。"
        qqq "我想{w=0.25}你应该知道自己叫什么吧。"

        menu:
            "要使用上次的名字吗？"
            "当然。":
                $ name_mc = persistent.name_mc
                qqq "非常感谢，{w=0.5}这样我就不用再重新念一遍那无聊的稿子了。"
                return
            "我还是换一个吧。":
                qqq "当然，{w=0.5}换个身份也是个很好的选择。"
                qqq "让我找找取名界面被我收拾到哪去了{......}"
                jump guide_naming_loop

    qqq "我想，{w=0.25}你应该就是玩家了。"
    qqq "首先，{w=0.5}感谢你愿意游玩我们的作品。"
    # yangsy "谁家 B-X 感谢你玩我们的游戏（"
    qqq "{......}\n{w=1.0}该死的，{w=0.25}我又忘记我要说什么了。"
    qqq "抱歉，{w=0.25}我早该在这之前准备好文案的，{w=0.25}我总是这样。"
    qqq "算了，{w=0.25}既然如此，{w=0.5}不妨先取个名字？"

    "↓试着给自己想个名字？{nw}"
    python:
        start_time = time.time()
    default player_input = ""
    call screen volatile_input_screen("↓试着给自己想个名字？", 1.0)
    $ entered = _return
    python:
        delta_time = time.time() - start_time
    $ renpy.block_rollback()

    # 如果在一秒内成功地输入了名字：
    if entered == "Entered":
        qqq "哇，{w=0.25}你的速度可真快，只用了[delta_time:.3f]秒就{......}\n你大概只是乱敲了下键盘吧，{w=0.25}我猜。"
        qqq "也许你是个速通玩家，{w=0.5}谁知道呢？\n{w=1.0}我反正不明白为什么一个galgame也会有人尝试速通。"
        jump guide_naming_entered

    qqq "——啊，{w=0.25}不好意思，{w=0.5}我得提醒你一下。"
    qqq "尽管这个游戏理论上是完全离线的，{w=0.5}但是——"
    qqq "不论如何，{w=0.5}在任何的地方暴露你的真实姓名都是\n{w=0.25}{red}{cps=*0.25}极其危险的行为{/cps}{/red}。"
    qqq "尽管我并不会限制你输入自己的名字（我的程序也没办法识别），\n{w=0.25}但还是请你{red}{cps=*0.5}一定一定不要这么做{/cps}{/red}，{w=0.25}好吗？{nw}"
    $ _history_list.pop()
    menu:
        qqq "尽管我并不会限制你输入自己的名字（我的程序也没办法识别），\n但还是请你{red}一定一定不要这么做{/red}，好吗？{fast}"
        "当然可以。":
            pass

    qqq "唔，{w=0.25}看来选择模块运行正常。"
    qqq "实在是不好意思，{w=0.5}让不知情的你参与了一下调试。\n{w=1.0}我不太擅长调用这些功能，{w=0.5}所以有时可能会出现一些小错误。"
    qqq "非常感谢你的配合。"
    qqq "咳咳，{w=0.25}扯远了。"

    jump guide_naming_loop


label guide_naming_loop:

    "↓试着给自己想个名字？{nw}"
    python:
        player_input = renpy.input(_("↓试着给自己想个名字？")).strip()
    jump guide_naming_entered

label guide_naming_entered:

    python:
        currentuser = ""
        for name in ("LOGNAME", "USER", "LNAME", "USERNAME"):
            user = os.environ.get(name)
            if user:
                currentuser = user
    
    # 如果不输入名字，或者输入的名字全部为空白字符：
    if not player_input:
        qqq "怎么，{w=0.25}你觉得这样会触发什么彩蛋吗？\n{w=1.0}还是说你叫棍母？\n{w=1.0}又或者你是那个睿智的国王？{w=0.5}名字只有聪明人才能看见？"
        qqq "{......}"
        qqq "咳咳，{w=0.25}我开玩笑的。"
        qqq "总有些人不太擅长取名字，{w=0.5}我也一样。"
        qqq "或者他们就喜欢主角的名字，{w=0.5}也许是为了沉浸感？"
        qqq "不过这样的话，{w=0.5}我就得替你想一个名字了。\n{w=1.0}这可真是个艰巨的任务。"
        qqq "{......}"
        qqq "算了，{w=0.25}稍等一下，{w=0.5}我好像有个随机名字生成器，{w=0.5}我找找{......}"

        "{......}"

        qqq "嗯，{w=0.25}你觉得，{w=0.5}“XDDCC”这个名字怎么样？"
        qqq "啊哈哈，{w=0.25}抱歉，{w=0.25}你可能不知道这个梗，{w=0.5}实在是不好意思。\n{w=1.0}我绝对不会用这个名字的，{w=0.5}这名字太烂了。"
        qqq "看来还得我自己想一个{......}{nw}"
        qqq "噢，{w=0.25}你觉得“Era”这个名字怎么样？\n{w=0.5}{nw}"
        $ _history_list.pop()
        menu:
            qqq "噢，你觉得“Era”这个名字怎么样？\n{fast}{w=0.5}我实在是不擅长取名字，{w=0.5}这已经是我能想到的比较好的一个了。"
            "当然。": 
                $ name_mc = "Era"
                jump guide_naming_done
            "我再想想......": 
                qqq "好吧，{w=0.5}显然你需要一个中文名字。"
                qqq "那就叫“殷夏”吧，{w=0.25}{nw}"
                $ _history_list.pop()
                menu:
                    qqq "那就叫“殷夏”吧，{fast}{w=0.25}这是我朋友的名字。"
                    "当然。": 
                        $ name_mc = "殷夏"
                        jump guide_naming_done
                    "我再想想......": 
                        $ name_mc = "玩家"
                        $ persistent.name_mc = name_mc
                        $ renpy.block_rollback()
                        qqq "什么，{w=0.5}这都不满意吗？\n{w=1.0}我明白了，{w=0.5}你莫不是来消遣洒家？"
                        qqq "我已经没有耐心了，{w=0.25}你就叫玩家吧，{w=0.25}我不会给你选择的机会了。"
                        return
    
    # 否则，如果输入的名字是administrator等管理员用户名：
    elif player_input.lower() in ("admin", "administrator", "system", "root", "wheel"):
        qqq "{......}我不明白。"
        qqq "我应该没有调用获取系统账户名称的API吧{......}"
        qqq "难道说你觉得这样做就能获得什么“{green}管理员权限{/green}”之类的？"
        qqq "谁知道呢，{w=0.5}说不定某次更新之后作者就会为这个加点什么？"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则，如果输入的名字是当前系统用户名：
    elif player_input == currentuser:
        qqq "唔{...}这好像是你系统账户的名字。\n{w=1.0}你不会所有地方都会用一样的名字吧？"
        qqq "没什么好说的，你喜欢就好。"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则，如果输入的名字是qwq/awa等：
    elif player_input.lower() in ("qwq", "awa", "uwu", "xwx"):
        qqq "[player_input]"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则，如果输入的名字含有特殊符号（通过检查Unicode字符分类判断）：
    elif any(unicodedata.category(c) in ("So", "Zl", "Zp", "Cc", "Cf", "Cs", "Co", "Cn") for c in player_input):
        qqq "虽然说输入框能支持，{w=0.25}但是{...}\n{...}你取个这样的名字，{w=0.5}我该怎么念呢？"
        qqq "难道说你在聊天框里塞了颜文字？{w=1.0}我的程序检测不出来。"
        $ name_mc = player_input
        jump guide_naming_confirm

    # 否则，如果输入的名字长度大于20个字符：
    elif len(player_input) > 20:
        qqq "哇，{w=0.25}这可真是个很长的名字。\n{w=1.0}不过这么长的名字，{w=0.5}我可不能确定UI能不能适配。\n{w=1.0}也许换个名字是个更好的选择？"
        jump guide_naming_loop

    # 否则，如果输入的名字长度小于3字节：
    elif len(bytes(player_input, encoding="utf-8")) < 3:
        qqq "或许你不太擅长取名字，{w=0.5}我也一样。\n{w=1.0}没关系，{w=0.25}在这里，{w=0.25}名字并不重要。"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则，如果输入的名字是纯数字：
    elif all(c in string.digits for c in player_input):
        qqq "纯数字吗，{w=0.5}真是无趣，{w=0.5}像是系统分配的一样。"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则，如果输入的名字是纯英文字符（A-Z, a-z, 0-9）：
    elif all(c in string.digits + string.ascii_letters for c in player_input):
        qqq "英文字符，{w=0.5}很聪明的选择。"
        qqq "虽然输入框可以支持中文，{w=0.5}但是纯英文的兼容性往往更好。\n{w=1.0}看来你对这方面的知识的确有一点了解。"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则（以上条件均没能满足）：
    else:
        # yangsy "（此处应为[name_qqq]对玩家所取的名称（[player_input]）的默认评价）"
        $ name_mc = player_input
        jump guide_naming_confirm



label guide_naming_confirm:

    "确定要使用这个名字吗？{nw}"
    $ _history_list.pop()
    menu:
        "确定要使用这个名字吗？{fast}"
        "当然。": 
            jump guide_naming_done
        "我再想想......": 
            "好吧，那就重新{......}{nw}"
            jump guide_naming_loop


label guide_naming_done:

    $ persistent.name_mc = name_mc
    $ renpy.block_rollback()
    qqq "好的，{w=0.25}看来你决定好自己叫什么了。"
    qqq "不过我还是叫你玩家吧，{w=0.5}我还是习惯这么叫你。"
    qqq "——啊，{w=0.25}好奇我的名字吗，{w=0.5}我想这并不重要。"
    qqq "稍等一下，{w=0.5}我得找找剧情被我放在哪了{......}{nw}"
    
    return


# 以下是已被弃用的仿UNDERTALE取名系统


label ut_naming:
    scene black with fade

    if persistent.name_mc:
        $ name_mc = persistent.name_mc
        mc "A name has already been chosen."
    else:
        call ut_naming_loop from _call_ut_naming_loop
    
    return


label ut_naming_loop:
    "Name the main character.{nw}"
    $ name_mc = renpy.input(_("Name the main character.{fast}"), length=56).strip()
    if not name_mc:
        "You must choose a name."
        jump ut_naming_loop
    # elif any(name_mc.lower() in n for n in ["ashell", "阿希尔"]):
    #     character.ashell("大概是取名彩蛋对话啥的")
    #     jump guide_naming_loop
    # elif name_mc.lower() == "你的名字":
    #     name_mc = "韦一敏"
    mc "Is this name correct?{nw}"
    $ _history_list.pop()
    menu:
        mc "Is this name correct?{fast}"
        "Yes":
            $ persistent.name_mc = name_mc
            $ renpy.block_rollback()
            return
        "No":
            jump ut_naming_loop
