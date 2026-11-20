label chtest:
    jump test_console


label test_console:
    if not renpy.windows:
        return
    python:
        console = CmdWindow("DEBUG MODE", interactive=True)
        console.Create()
        console.Color("0A")
        console.Clear()
        console.ShowText("欢迎使用 RenPy 控制台！")
        console.ShowText("正在测试输入")
        command = console.Input()
        console.Close()
    mwam.comment "你刚才输入的是[command]"
    return


label chany:
    $ label_name = renpy.input("label:")
    menu:
        "renpy.call('[label_name]')":
            $ renpy.call(label_name)
        "renpy.jump('[label_name]')":
            $ renpy.jump(label_name)
    # mwam.comment "不加return的来了"
    return


label chtest_char:
    
    show yangsy zorder 2 at t41
    show gra zorder 2 at t11
    show mwam angry zorder 2 at t43
    show morin zorder 2 at t44
    show baile zorder 3 at t42
    ""

    return


label chtest_control:
    show gra
    gra "靠左"
    gra.right "靠右" 
    gra "靠左"

    return

label chtest_mwam_remake:
    show mwam
    mwam "尝试一点东西"
    mwam blush mouth_happy eye_happy "嗯，对"
    mwam -blush angry mouth_angry eye_normal brow_angry "I'm Very ANGRY!!!!"
    mwam "I Want You To DIE!!!!!!!!!!!!"
    hide mwam
    return

label chtest_exceptscreen:

    pause 1.0

    show yangsy body_no_bag eye_flat zorder 3 at f11
    yangsy brow_angry eye_jitome "诶，Yangsy试试看能不能卡个bug（"
    show yangsy at h11
    yangsy brow_happy eye_flat mouth_cat_happy_open '咳咳，{w=0.5}"\n$ raise StopIteration()\n"{nw}'
    # $ raise StopIteration()
    show screen custom_exception('  {a}File "game/scripts/chtest.rpy", line ???{/a}, in script\n    $ raise StopIteration()\nStopIteration')
    yangsy brow_happy eye_tareme mouth_cat_sad_open "{w=1.0}{......}"
    show yangsy at d11
    yangsy blush brow_angry mouth_happy_open "（诶不是咋还真卡崩了？？？）"
    hide yangsy

    return


label chtest_session_title:
    nvl clear
    $ session_title = gra
    gra.nvl "这是什么颜色？"


label chtest_select_file:
    nvl clear
    gra.nvl "给我看看你做的？"
    menu(nvl=True):
        "选择文件上传…":
            pass