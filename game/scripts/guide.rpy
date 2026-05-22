# 向导 by 祐荽


init python:
    import os
    import time
    import string
    import unicodedata


label guide_naming_start:
    
    scene black with fade

    python:
        duplicate_name_attempts = 0
        empty_name_attempts = 0
    guide "{......}噢，{w=0.25}嘿，{w=0.25}你好。"

    # 如果已经选择了一个名字：
    if persistent.name_mc:
        guide "等等，{w=0.5}我认得你。"
        guide "你的名字是不是{......}算了，{w=0.25}我还是叫你玩家吧。"
        guide "不知道为什么，{w=0.5}直呼别人的名字会让我有种{w=0.5}奇怪的羞耻感。"
        guide "我想{w=0.25}你应该知道自己叫什么吧。"

        menu:
            "要使用上次的名字吗？"
            "当然。":
                $ name_mc = persistent.name_mc
                guide "非常感谢，{w=0.5}这样我就不用再重新念一遍那无聊的稿子了。"
                return
            "我还是换一个吧。":
                $ duplicate_name_attempts = 0
                guide "当然，{w=0.5}换个身份也是个很好的选择。"
                guide "让我找找取名界面被我收拾到哪去了{......}"
                jump guide_naming_loop

    guide "我想，{w=0.25}你应该就是玩家了。"
    guide "首先，{w=0.5}感谢你愿意游玩我们的作品。"
    # yangsy "谁家 B-X 感谢你玩我们的游戏（"
    guide "{......}\n{w=1.0}该死的，{w=0.25}我又忘记我要说什么了。"
    guide "抱歉，{w=0.25}我早该在这之前准备好文案的，{w=0.25}我总是这样。"
    guide "算了，{w=0.25}既然如此，{w=0.5}不妨先取个名字？"

    "↓试着给自己想个名字？{nw}"
    python:
        start_time = time.time()
    default player_input = ""
    window hide None
    with None
    call screen volatile_input_screen("↓试着给自己想个名字？", 1.0)
    with None
    window auto None
    $ entered = _return
    python:
        delta_time = time.time() - start_time
    $ renpy.block_rollback()

    # 如果在一秒内成功地输入了名字：
    if entered == "Entered":
        guide "哇，{w=0.25}你的速度可真快，只用了[delta_time:.3f]秒就{......}\n你大概只是乱敲了下键盘吧，{w=0.25}我猜。"
        guide "也许你是个速通玩家，{w=0.5}谁知道呢？\n{w=1.0}我反正不明白为什么一个galgame也会有人尝试速通。"
        jump guide_naming_entered

    guide "——啊，{w=0.25}不好意思，{w=0.5}我得提醒你一下。"
    guide "尽管这个游戏理论上是完全离线的，{w=0.5}但是——"
    guide "不论如何，{w=0.5}在任何的地方暴露你的真实姓名都是\n{w=0.25}{red}{cps=*0.25}极其危险的行为{/cps}{/red}。"
    guide "尽管我并不会限制你输入自己的名字（我的程序也没办法识别），\n{w=0.25}但还是请你{red}{cps=*0.5}一定一定不要这么做{/cps}{/red}，{w=0.25}好吗？{nw}"
    $ _history_list.pop()
    menu:
        guide "尽管我并不会限制你输入自己的名字（我的程序也没办法识别），\n但还是请你{red}一定一定不要这么做{/red}，好吗？{fast}"
        "当然可以。":
            pass

    guide "唔，{w=0.25}看来选择模块运行正常。"
    guide "实在是不好意思，{w=0.5}让不知情的你参与了一下调试。\n{w=1.0}我不太擅长调用这些功能，{w=0.5}所以有时可能会出现一些小错误。"
    guide "非常感谢你的配合。"
    guide "咳咳，{w=0.25}扯远了。"

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
        $ empty_name_attempts += 1
    
        if empty_name_attempts == 1:
            guide "你刚刚是不是{...}不小心把取名环节给跳过去了？\n{w=1.0}问题不大，{w=0.5}我们再来一次。"
            jump guide_naming_loop

        elif empty_name_attempts == 2:
            guide "{...}是我的问题，{w=0.5}还是说你好像又一次什么名字都没有输入？"
            jump guide_naming_loop
            
        else:
            guide "怎么，{w=0.25}你觉得这样会触发什么彩蛋吗？\n{w=1.0}还是说你叫棍母？\n{w=1.0}又或者你是那个睿智的国王？{w=0.5}名字只有聪明人才能看见？"
            guide "{......}"
            guide "咳咳，{w=0.25}我开玩笑的。"
            guide "总有些人不太擅长取名字，{w=0.5}我也一样。"
            guide "或者他们就喜欢主角的名字，{w=0.5}也许是为了沉浸感？"
            guide "不过这样的话，{w=0.5}我就得替你想一个名字了。\n{w=1.0}这可真是个艰巨的任务。"
            guide "{......}"
            guide "算了，{w=0.25}稍等一下，{w=0.5}我好像有个随机名字生成器，{w=0.5}我找找{......}"

            "{......}"

            guide "嗯，{w=0.25}你觉得，{w=0.5}“XDDCC”这个名字怎么样？"
            guide "啊哈哈，{w=0.25}抱歉，{w=0.25}你可能不知道这个梗，{w=0.5}实在是不好意思。\n{w=1.0}我绝对不会用这个名字的，{w=0.5}这名字太烂了。"
            guide "看来还得我自己想一个{......}{nw}"
            guide "噢，{w=0.25}你觉得“Era”这个名字怎么样？\n{w=0.5}{nw}"
            $ _history_list.pop()
            menu:
                guide "噢，你觉得“Era”这个名字怎么样？\n{fast}{w=0.5}我实在是不擅长取名字，{w=0.5}这已经是我能想到的比较好的一个了。"
                "当然。": 
                    $ name_mc = "Era"
                    jump guide_naming_done
                "我再想想......": 
                    guide "好吧，{w=0.5}显然你需要一个中文名字。"
                    guide "那就叫“殷夏”吧，{w=0.25}{nw}"
                    $ _history_list.pop()
                    menu:
                        guide "那就叫“殷夏”吧，{fast}{w=0.25}这是我朋友的名字。"
                        "当然。": 
                            $ name_mc = "殷夏"
                            jump guide_naming_done
                        "我再想想......": 
                            $ name_mc = "玩家"
                            $ persistent.name_mc = name_mc
                            $ renpy.block_rollback()
                            guide "什么，{w=0.5}这都不满意吗？\n{w=1.0}我明白了，{w=0.5}你莫不是来消遣洒家？"
                            guide "我已经没有耐心了，{w=0.25}你就叫玩家吧，{w=0.25}我不会给你选择的机会了。"
                            return

    # 否则，如果输入的名字与剧情中存在的角色撞名：
    elif player_input in names:
        python:
            duplicate_name_attempts += 1
            quick_menu = False
        # 显示自定义错误对话框
            error_message = f"NameError: '{player_input}' is already defined.\nPress Ignore to continue..."
        window hide None
        with None
        call screen naming_error_message(error_message)
        with None
        window auto None
        # 显示错误提示（不再使用 raise）
        python: 
            quick_menu = True
            renpy.block_rollback()
        if duplicate_name_attempts == 1:
            guide "哦不{...}{w=0.5}我没考虑到这一点。\n{w=1.0}大概是你的名字和游戏内角色冲突了，{w=0.5}我的程序没考虑到这点。"
            guide "我想，{w=0.25}你可能得试试别的名字了，{w=0.5}非常抱歉。"
            guide "稍等一下，{w=0.5}我得回退一下进程{......}{nw}"
        elif duplicate_name_attempts == 2:
            guide "啊，{w=0.25}你运气真不好。\n{w=1.0}我想{w=0.25}你得再试一次了。"
        elif duplicate_name_attempts == 3:
            guide "喂，{w=0.25}你是故意的吧。"
            guide "你是不是在网络上看过攻略了？{w=0.5}还是你认识他们？"
            guide "我劝你最好{cps=*0.5}认真考虑一下，{w=0.5}我的耐心是有限的。{/cps}"
        else:
            guide "{......}"
            $ name_mc = player_input
        
        # 返回重新输入
        jump guide_naming_loop
    
    # 否则，如果输入的名字是administrator等管理员用户名：
    elif player_input.lower() in ("admin", "administrator", "system", "root", "wheel"):
        guide "{......}我不明白。"
        guide "我应该没有调用获取系统账户名称的API吧{......}"
        guide "难道说你觉得这样做就能获得什么“{green}管理员权限{/green}”之类的？"
        guide "谁知道呢，{w=0.5}说不定某次更新之后作者就会为这个加点什么？"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则，如果输入的名字是当前系统用户名：
    elif player_input == currentuser:
        guide "唔{...}这好像是你系统账户的名字。\n{w=1.0}你不会所有地方都会用一样的名字吧？"
        guide "没什么好说的，你喜欢就好。"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则，如果输入的名字是qwq/awa等：
    elif player_input.lower() in ("qwq", "awa", "uwu", "xwx"):
        guide "[player_input]"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则，如果输入的名字含有特殊符号（通过检查Unicode字符分类判断）：
    elif any(unicodedata.category(c) in ("So", "Zl", "Zp", "Cc", "Cf", "Cs", "Co", "Cn") for c in player_input):
        guide "虽然说输入框能支持，{w=0.25}但是{...}\n{...}你取个这样的名字，{w=0.5}我该怎么念呢？"
        guide "难道说你在聊天框里塞了颜文字？{w=1.0}我的程序检测不出来。"
        $ name_mc = player_input
        jump guide_naming_confirm

    # 否则，如果输入的名字长度大于20个字符：
    elif len(player_input) > 20:
        guide "哇，{w=0.25}这可真是个很长的名字。\n{w=1.0}不过这么长的名字，{w=0.5}我可不能确定UI能不能适配。\n{w=1.0}也许换个名字是个更好的选择？"
        jump guide_naming_loop

    # 否则，如果输入的名字长度小于3字节：
    elif len(bytes(player_input, encoding="utf-8")) < 3:
        guide "或许你不太擅长取名字，{w=0.5}我也一样。\n{w=1.0}没关系，{w=0.25}在这里，{w=0.25}名字并不重要。"
        $ name_mc = player_input
        jump guide_naming_confirm
    
    # 否则（以上条件均没能满足）：
    else:
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
    guide "好的，{w=0.25}看来你决定好自己叫什么了。"
    guide "不过我还是叫你玩家吧，{w=0.5}我还是习惯这么叫你。"
    guide "——啊，{w=0.25}好奇我的名字吗，{w=0.5}我想这并不重要。"
    guide "稍等一下，{w=0.5}我得找找剧情被我放在哪了{......}{nw}"
    
    return


# 自定义错误提示屏幕（在 screens.rpy 中添加，或直接加在这里）
screen naming_error_message(error_message):
    modal True
    frame:
        background "#ffffff"
        xfill True
        yfill True
        padding (50, 50)
        
        vbox:
            spacing 15
            xfill True
            
            text "Oops! Something went wrong.":
                size 60
                color "#000000"
                font debug_gui_font
            
            frame:
                background "#f5f5f5"
                padding (15, 15)
                xfill True
                
                text "[error_message]":
                    size 30
                    color "#000000"
                    font debug_gui_font
            
            hbox:
                spacing 20
                xalign 0.0
                textbutton "Rollback" action Rollback() text_color "#000000" text_font debug_gui_font
                textbutton "Ignore" action Return() text_color "#000000" text_font debug_gui_font
                textbutton "Reload" action None text_color "#999999" text_font debug_gui_font
                textbutton "Console" action None text_color "#999999" text_font debug_gui_font
