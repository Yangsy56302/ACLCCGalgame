label chtest:
    jump chtest_exceptscreen


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