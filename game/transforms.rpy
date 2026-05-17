# 决定直接挪用DDLC位置变换了（

transform tcommon(x=640, z=0.80):
    subpixel True
    on show:
        ypos 1.03125
        alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x
        parallel:
            easein .15 yoffset 0 ypos 1.03125

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 alpha 1.00 ypos 1.03125

# This transform makes the character when they talk.
transform focus(x=640, z=0.80):
    ypos 1.03125 subpixel True
    on show:
        alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 alpha 1.00
        ypos 1.03125
    
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x
        parallel:
            easein .15 yoffset 0

# This transform causes the character to sink down on the screen.
transform sink(x=640, z=0.80):
    xcenter x yoffset 0 ypos 1.03125 alpha 1.00 subpixel True
    easein .5 ypos 1.06

# This transform makes the character jump for a bit
transform hop(x=640, z=0.80):
    xcenter x yoffset 0 ypos 1.03125 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

# This transform makes the character jump and be in focus at the same time.
transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 ypos 1.03125 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

# This causes the character to sink down from the screen then come back up.
transform dip(x=640, z=0.80):
    xcenter x yoffset 0 ypos 1.03125 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

# This transform causes the character to wobble on-screen.
# This might be a left-over transform from DDLC's development for Natsuki's Closet CG.
transform panic(x=640, z=0.80):
    xcenter x yoffset 0 ypos 1.03125 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

# This transform causes the character to "fly in" (enter the scene) from the left.
transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 ypos 1.03125 alpha 1.00 subpixel True
    easein .25 xcenter x

# This transform causes the character to "fly in" (enter the scene) from the right.
transform rightin(x=640, z=0.80):
    xcenter 2000 yoffset 0 ypos 1.03125 alpha 1.00 subpixel True
    easein .25 xcenter x

# This transform hides the character from the screen.
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:
        easein .25 alpha 0.00 yoffset -20

# This transform hides the character by moving them to the left.
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

# This transform hides the character by moving them to the left.
transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000

# These transforms have the characters stand still at a given position given
# how many characters are on screen and which character number they are.
transform t41:
    tcommon(300)
transform t42:
    tcommon(740)
transform t43:
    tcommon(1180)
transform t44:
    tcommon(1620)
transform t31:
    tcommon(360)
transform t32:
    tcommon(960)
transform t33:
    tcommon(1560)
transform t21:
    tcommon(600)
transform t22:
    tcommon(1320)
transform t11:
    tcommon(960)

# These transforms makes the character pop in.
transform i41:
    tinstant(300)
transform i42:
    tinstant(740)
transform i43:
    tinstant(1180)
transform i44:
    tinstant(1620)
transform i31:
    tinstant(360)
transform i32:
    tinstant(960)
transform i33:
    tinstant(1560)
transform i21:
    tinstant(600)
transform i22:
    tinstant(1320)
transform i11:
    tinstant(960)

# These transforms makes the character be the main focus on-screen.
transform f41:
    focus(300)
transform f42:
    focus(740)
transform f43:
    focus(1180)
transform f44:
    focus(1620)
transform f31:
    focus(360)
transform f32:
    focus(960)
transform f33:
    focus(1560)
transform f21:
    focus(600)
transform f22:
    focus(1320)
transform f11:
    focus(960)

# These transforms makes the character sink downwards.
transform s41:
    sink(300)
transform s42:
    sink(740)
transform s43:
    sink(1180)
transform s44:
    sink(1620)
transform s31:
    sink(360)
transform s32:
    sink(960)
transform s33:
    sink(1560)
transform s21:
    sink(600)
transform s22:
    sink(1320)
transform s11:
    sink(960)

# These transforms makes the character hop.
transform h41:
    hop(300)
transform h42:
    hop(740)
transform h43:
    hop(1180)
transform h44:
    hop(1620)
transform h31:
    hop(360)
transform h32:
    hop(960)
transform h33:
    hop(1560)
transform h21:
    hop(600)
transform h22:
    hop(1320)
transform h11:
    hop(960)

# These transforms makes the character hop and be in focus at the same time.
transform hf41:
    hopfocus(300)
transform hf42:
    hopfocus(740)
transform hf43:
    hopfocus(1180)
transform hf44:
    hopfocus(1620)
transform hf31:
    hopfocus(360)
transform hf32:
    hopfocus(960)
transform hf33:
    hopfocus(1560)
transform hf21:
    hopfocus(600)
transform hf22:
    hopfocus(1320)
transform hf11:
    hopfocus(960)

# These transforms makes the character dip down the screen, then come back up.
transform d41:
    dip(300)
transform d42:
    dip(740)
transform d43:
    dip(1180)
transform d44:
    dip(1620)
transform d31:
    dip(360)
transform d32:
    dip(960)
transform d33:
    dip(1560)
transform d21:
    dip(600)
transform d22:
    dip(1320)
transform d11:
    dip(960)

# These transforms makes the character fly in from the left.
transform l41:
    leftin(300)
transform l42:
    leftin(740)
transform l43:
    leftin(1180)
transform l44:
    leftin(1620)
transform l31:
    leftin(360)
transform l32:
    leftin(960)
transform l33:
    leftin(1560)
transform l21:
    leftin(600)
transform l22:
    leftin(1320)
transform l11:
    leftin(960)

# These transforms makes the character fly in from the right.
transform r41:
    rightin(300)
transform r42:
    rightin(740)
transform r43:
    rightin(1180)
transform r44:
    rightin(1620)
transform r31:
    rightin(360)
transform r32:
    rightin(960)
transform r33:
    rightin(1560)
transform r21:
    rightin(600)
transform r22:
    rightin(1320)
transform r11:
    rightin(960)

# 以下变换用于单独设置每个角色的 缩放 和 Y轴锚点。

transform tyahalf:
    yanchor 0.5 subpixel True

transform tcgra:
    tyahalf
    zoom 0.75

transform tclingyun:
    tyahalf
    zoom 0.875

transform tcmwam:
    tyahalf
    zoom 0.875