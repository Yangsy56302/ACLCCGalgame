# 向导 by 祐荽


init -99 python:
    import os
    import math
    import time
    import string
    import unicodedata

label setup_naming_start:
    
    scene black with fade

    python:
        duplicate_name_attempts = 0
        empty_name_attempts = 0

    """
    {cps=8}{nw}· · · · · ·{w=1}

    {cps=8}{nw}· · · · · ·{w=1}

    {cps=8}{nw}· · · · · ·{w=1}

    {cps=128}{nw}· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 
    · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 
    · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·
    """

    setup "噢，{w=0.25}嘿，{w=0.5}你好。"

    play music "mus_setup.ogg" fadein 2.0
    $ renpy.notify("♪ ms_win_and_mc - Before Beginning")

    # 如果已经选择了一个名字：
    if persistent.name_mc:
        setup """
        等等，{w=0.5}我认得你。

        你的名字是不是{......}算了，{w=0.25}我还是叫你玩家吧。

        不知道为什么，{w=0.5}直呼别人的名字会让我有种奇怪的羞耻感。

        我想你应该知道自己叫什么吧，{w=0.5}对吧？
        """

        menu:
            "要使用上次的名字吗？"
            "当然。":
                $ mc.nickname = persistent.name_mc
                setup "非常感谢，{w=0.5}这样我就不用再重新念一遍那无聊的稿子了。"
                return
            "我还是换一个吧。":
                $ duplicate_name_attempts = 0
                setup "好吧，{w=0.5}换个身份也是个很好的选择。{w=0.25}稍等一下，{w=0.25}谢谢。\n{w=1}{color=#cccccc}（我把取名界面丢到哪去了{......}）"
                jump setup_naming_loop

    setup "呃，{w=0.25}所以，{cps=*0.9}{w=0.25}我应该叫你{......}{w=0.5}{cps=*0.9}玩家？"
    setup "{cps=*0.9}行吧，{w=0.5}好吧，{w=0.5}你好玩家，{w=0.5}玩家你好，{w=0.5}嗯。"
    setup "那么首先，{w=0.25}呃，{w=0.25}谢谢你愿意游玩我们的作品，{w=0.25}我想是的。"
    stop music fadeout 2.0
    setup "然后，{w=1}{cps=*0.8}呃{......}{w=2}{nw}"
    setup "{cps=*0.7}呃{......}{w=2}{nw}"
    setup "{cps=*0.5}呃{......}{......}{w=1}{nw}"
    setup "啊，该死的，我又忘记我要说什么了。"
    play music "mus_setup.ogg" fadein 2.0
    setup "抱歉，{w=0.25}我应该在这之前准备好的，{w=0.25}我总是这样。"
    setup "算了，{w=0.25}又不是什么重要的内容，{w=0.25}你直接取名算了。"


    "↓ 给自己想个名字？{nw}"
    python:
        start_time = time.time()
    default player_input = ""
    window hide None
    with None
    call screen volatile_input_screen("↓ 给自己想个名字？", 0.5)
    with None
    window auto None
    $ entered = _return
    python:
        delta_time = time.time() - start_time
    $ renpy.block_rollback()

    # 如果在显示时间内输入了内容：
    if entered == "Entered":
        setup "哇，{w=0.25}你的速度可真快，只用了[delta_time:.3f]秒{......}\n你大概只是乱敲了下键盘吧，{w=0.25}我猜。"
        setup "也许你是个速通玩家，{w=0.5}谁知道呢？\n{w=1.0}我反正不明白为什么一个galgame也会有人尝试速通。"
        jump setup_naming_entered

    setup "——啊，{w=0.25}不好意思，{w=0.5}我得提醒你一下。"
    setup "尽管这个游戏理论上是完全离线的，{w=0.5}但是——"
    stop music fadeout 2.0
    setup "不论如何，{w=0.5}在任何的地方暴露你的真实姓名都是\n{red}{cps=*0.5}极其危险的行为{/cps}{/red}。"
    setup "尽管我并不会限制你输入自己的名字{w=0.25}（我的程序也没办法识别），\n{w=0.25}但还是请你{red}{cps=*0.5}一定一定不要这么做{/cps}{/red}，{cps=*0.5}{w=0.25}好吗？{nw}"
    $ _history_list.pop()
    menu:
        setup "尽管我并不会限制你输入自己的名字（我的程序也没办法识别），\n但还是请你{red}一定一定不要这么做{/red}，好吗？{fast}"
        "当然可以。":
            pass
    play music "mus_setup.ogg" fadein 2.0
    setup "唔，{w=0.25}看来选择模块运行正常。"
    setup "实在是不好意思，{w=0.5}让不知情的你参与了一下调试。\n{w=1.0}我不太擅长调用这些功能，{w=0.5}所以有时可能会出现一些小错误。"
    setup "非常感谢你的配合。"
    setup "咳咳，{w=0.25}扯远了。"

    jump setup_naming_loop


label setup_naming_loop:

    "↓ 给自己想个名字？{nw}"
    python:
        player_input = renpy.input(_("↓ 给自己想个名字？")).strip()
    jump setup_naming_entered

label setup_naming_entered:

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
            setup "{......}奇怪，我的程序没对这种情况做出限制吗？{w=1.0}开发者还真是粗心。"
            setup "算了，{w=0.25}将就着用吧，{w=0.25}反正一个存档也只用一次。"
            jump setup_naming_loop

        elif empty_name_attempts == 2:
            setup "你是故意的吗？{w=0.25}我可不觉得这很好玩。"
            setup "抱歉，{w=0.25}我不是在威胁你，{w=0.25}不过我们还是别在取名界面耽搁太久吧。"
            jump setup_naming_loop
            
        else:
            stop music fadeout 2.0
            setup "怎么，{w=0.25}你觉得这样会触发什么彩蛋吗？"
            setup "还是说你叫棍母？\n{w=0.5}又或者你是那个睿智的国王？{w=0.5}名字只有聪明人才能看见？"
            setup "{......}{w=0.25}{nw}"
            play music "mus_setup.ogg" fadein 2.0
            setup "咳咳，{w=0.25}我开玩笑的。"
            setup "总有些人不太擅长取名字，{w=0.5}我也一样。"
            setup "或者他们就喜欢主角的名字，{w=0.5}也许是为了沉浸感？"
            setup "不过这样的话，{w=0.5}我就得替你想一个名字了。\n{w=1.0}这可真是个艰巨的任务。"
            setup "{......}{w=0.25}{nw}"
            setup "算了，{w=0.25}稍等一下，{w=0.5}我好像有个随机名字生成器，{w=0.5}我找找{......}"

            setup "嗯，{w=0.25}你觉得，{w=0.5}“XDDCC”这个名字怎么样？{w=0.25}{nw}"
            setup "啊哈哈，{w=0.25}抱歉，{w=0.25}我只是开个玩笑，{w=0.25}你可能不知道这个梗，{w=0.5}实在是不好意思。"
            setup "我可没有什么随机名字生成器，{w=0.25}不过这个名字绝对不能用。"
            setup "{w=0.25}我可不想惹上官司，{w=0.5}更不用说这名字简直烂透了。"
            setup "看来还得我自己想一个{......}{nw}"
            setup "噢，{w=0.25}你觉得“Era”这个名字怎么样？\n{w=0.5}{nw}"
            $ _history_list.pop()
            menu:
                setup "噢，你觉得“Era”这个名字怎么样？\n{fast}{w=0.5}我实在是不擅长取名字，{w=0.5}这已经是我能想到的比较好的一个了。"
                "当然。": 
                    $ mc.nickname = "Era"
                    jump setup_naming_done
                "换一个吧。": 
                    setup "好吧，{w=0.5}显然你需要一个中文名字。"
                    setup "那就叫“殷夏”吧，{w=0.25}{nw}"
                    $ _history_list.pop()
                    menu:
                        setup "那就叫“殷夏”吧，{fast}{w=0.25}这是我朋友的名字。"
                        "当然。": 
                            $ mc.nickname = "殷夏"
                            jump setup_naming_done
                        "再换一个吧": 
                            $ mc.nickname = "玩家"
                            $ persistent.name_mc = mc.nickname
                            $ renpy.block_rollback()
                            stop music fadeout 2.0
                            setup "啊，{w=0.5}都不满意吗？"
                            setup "我明白了，{w=0.5}你莫不是来消遣洒家？"
                            setup "我已经没有耐心了，{w=0.25}你就叫玩家吧，{w=0.25}我不会给你选择的机会了。"
                            return

    # 否则，如果输入的名字与剧情中存在的角色撞名：
    elif player_input in names:
        # $ raise NameError("f'{player_input}' is already defined")
        python:
            duplicate_name_attempts += 1
            quick_menu = False
            error_message = "\n".join([
                f'  {{a}}File "game/script.rpy", line ???{{/a}}, in script call',
                f'    call setup_naming_start from _call_setup_naming_start',
                f'  {{a}}File "game/scripts/setup.rpy", line ???{{/a}}, in script',
                f'    {player_input} = CharacterWithData(',
                f'  {{a}}File "game/scripts/setup.rpy", line ???{{/a}}, in <module>',
                f'    {player_input} = CharacterWithData(',
                f"NameError: '{player_input}' is already defined",
            ])
        # 显示错误提示（不再使用 raise）
        window hide None
        stop music
        with None
        show screen custom_exception(error_message)
        python: 
            quick_menu = True
            renpy.block_rollback()
        pause 1.0
        window auto
        if duplicate_name_attempts == 1:
            setup "哦不{......}{w=0.5}我没考虑到这一点。\n{w=1.0}大概是你的名字和游戏内角色冲突了，{w=0.5}我的程序没考虑到这点。"
            setup "我想，{w=0.25}你可能得试试别的名字了，{w=0.5}非常抱歉。"
            setup "稍等一下，{w=0.5}我得回退一下进程{......}{nw}"
        elif duplicate_name_attempts == 2:
            setup "啊，{w=0.25}你运气真不好。\n{w=1.0}我想{w=0.25}你得再试一次了。"
        elif duplicate_name_attempts == 3:
            setup "喂，{w=0.25}你是故意的吧。"
            setup "你是不是在网络上看过攻略了？{w=0.5}还是你认识他们？"
            setup "我劝你最好{cps=*0.5}认真考虑一下，{w=0.5}我的耐心是有限的。{/cps}"
        else:
            setup "{......}"
            $ mc.nickname = player_input
        
        with None
        hide screen custom_exception
        play music "mus_setup.ogg"
        # 返回重新输入
        jump setup_naming_loop
    
    # 否则，如果输入的名字是administrator等管理员用户名：
    elif player_input.lower() in ("admin", "administrator", "system", "root", "wheel"):
        setup "{......}我不明白。"
        setup "我应该没有调用获取系统账户名称的API吧{......}"
        setup "难道说你觉得这样做就能获得什么“{green}管理员权限{/green}”之类的？"
        setup "谁知道呢，{w=0.5}说不定某次更新之后作者就会为这个加点什么？"
        $ mc.nickname = player_input
        jump setup_naming_confirm
    
    # 否则，如果输入的名字是当前系统用户名：
    elif player_input == currentuser:
        setup "唔{......}这好像是你系统账户的名字。\n{w=1.0}你不会所有地方都会用一样的名字吧？"
        setup "没什么好说的，你喜欢就好。"
        $ mc.nickname = player_input
        jump setup_naming_confirm
    
    # 否则，如果输入的名字是qwq/awa等：
    elif player_input.lower() in ("qwq", "awa", "uwu", "xwx"):
        setup "[player_input]"
        $ mc.nickname = player_input
        jump setup_naming_confirm
    
    # 否则，如果输入的名字含有特殊符号（通过检查Unicode字符分类判断）：
    elif any(unicodedata.category(c) in ("So", "Zl", "Zp", "Cc", "Cf", "Cs", "Co", "Cn") for c in player_input):
        setup "虽然说输入框能支持，{w=0.25}但是{......}你取个这样的名字，{w=0.5}我该怎么念呢？"
        setup "难道说你在聊天框里塞了颜文字？{w=1.0}我的程序可检测不出来。"
        $ mc.nickname = player_input
        jump setup_naming_confirm

    # 否则，如果输入的名字长度大于20个字符：
    elif len(player_input) > 20:
        setup "哇，{w=0.25}这可真是个很长的名字。\n{w=1.0}不过这么长的名字，{w=0.5}我可不能确定UI能不能适配。\n{w=1.0}也许换个名字是个更好的选择？"
        jump setup_naming_loop

    # 否则，如果输入的名字长度小于3字节：
    elif len(bytes(player_input, encoding="utf-8")) < 3:
        setup "或许你不太擅长取名字，{w=0.5}我也一样。\n{w=1.0}没关系，{w=0.25}名字又不是什么很重要的东西。"
        $ mc.nickname = player_input
        jump setup_naming_confirm
    
    # 否则（以上条件均没能满足）：
    else:
        $ mc.nickname = player_input
        jump setup_naming_confirm



label setup_naming_confirm:

    "确定要使用这个名字吗？{nw}"
    $ _history_list.pop()
    menu:
        "确定要使用这个名字吗？{fast}"
        "当然。": 
            jump setup_naming_done
        "我再想想······": 
            jump setup_naming_loop


label setup_naming_done:

    $ persistent.name_mc = mc.nickname
    $ renpy.block_rollback()
    setup "好的，{w=0.25}看来你决定好自己叫什么了。"
    setup "不过我还是叫你玩家吧，{w=0.5}叫别人的名字我总感觉挺羞耻的。"
    setup "呃，{w=0.5}你还有其他疑问吗？{w=2}{nw}"
    setup "哦不对，{w=0.25}你又问不了我。（笑）"
    setup "好吧，稍等一下，{w=0.5}我得找找剧情被我放在哪了{......}{nw}"
    stop music fadeout 2.0
    
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
            
            text "Something went wrong.":
                size 60
                color "#000000"
                font debug_gui_font
            
            frame:
                background "#eeeeee"
                padding (15, 15)
                xfill True
                
                text "[error_message]":
                    size 30
                    color "#000000"
                    font debug_gui_font
            
            hbox:
                spacing 20
                xalign 0.0
                textbutton "Rollback" action Rollback() text_color "#000000" text_hover_color "#555555" text_font debug_gui_font
                textbutton "Ignore" action Return() text_color "#000000" text_hover_color "#555555" text_font debug_gui_font
                textbutton "Reload" action None text_color "#aaaaaa" text_font debug_gui_font
                textbutton "Console" action None text_color "#aaaaaa" text_font debug_gui_font
