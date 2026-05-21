init python:

    class CharacterWithData(renpy.character.ADVCharacter):
        def __init__(self, nickname, realname=None, **properties):
            super().__init__(dynamic=True, **properties)
            self.nickname = nickname
            self.realname = nickname if realname is None else realname
            self.meet_irl = False
            self.name = self._name
            self.affection = 0
        def _name(self):
            return self.realname if self.meet_irl else self.nickname
        def str(self):
            return self._name()


default persistent.name_mc = ""
default name_mc = ""
define character.mc = DynamicCharacter("name_mc")


define character.guide = CharacterWithData("？？？")


define character.ashell = CharacterWithData("阿希尔Ashell", image="ashell", what_prefix="a ", what_suffix="")

# image side ashell = "char/ashell/avatar.jpg"
# image ashell = "char/ashell/normal.png"


define character.baile = CharacterWithData("终究是摆了", "李星眠", image="baile", what_prefix="", what_suffix="")

transform tcbaile:
    yanchor 0.5 subpixel True
    zoom 1.0

# image side baile = "char/baile/avatar.jpg"
image baile = At("char/baile/happy.png", tcbaile)
image baile admiration = At("char/baile/admiration.png", tcbaile)
image baile angry = At("char/baile/angry.png", tcbaile)
image baile beg = At("char/baile/beg.png", tcbaile)
image baile cry = At("char/baile/cry.png", tcbaile)
image baile disappointed = At("char/baile/disappointed.png", tcbaile)
image baile happy = At("char/baile/happy.png", tcbaile)
image baile love = At("char/baile/love.png", tcbaile)
image baile pain = At("char/baile/pain.png", tcbaile)
image baile sacred = At("char/baile/sacred.png", tcbaile)
image baile sad = At("char/baile/sad.png", tcbaile)
image baile scared = At("char/baile/scared.png", tcbaile)
image baile serious = At("char/baile/serious.png", tcbaile)
image baile surprise = At("char/baile/surprise.png", tcbaile)
image baile thinking = At("char/baile/thinking.png", tcbaile)
image baile tsundere = At("char/baile/tsundere.png", tcbaile)
image baile worried = At("char/baile/worried.png", tcbaile)


define character.dwen = CharacterWithData("是动听D温呐", image="dwen", what_prefix="~ ", what_suffix="")

# image side dwen = "char/dwen/avatar.jpg"
# image dwen = "char/dwen/normal.png"


define character.gra = CharacterWithData("晴柚-Grafrustix", "晴安柚子", image="gra", what_prefix="< ", what_suffix=" 3")

transform tcgra:
    yanchor 0.625 subpixel True
    zoom 0.75

# image side gra = "char/gra/avatar.jpg"
image gra = At("char/gra/normal.png", tcgra)
image gra flirt = At("char/gra/flirt.png", tcgra)


define character.hale = CharacterWithData("TheHale", image="hale", what_prefix="", what_suffix="")

# image side hale = "char/hale/avatar.jpg"
# image hale = "char/hale/normal.png"


define character.lamb = CharacterWithData("Happylamb029", image="lamb", what_prefix="", what_suffix="")

# image side lamb = "char/lamb/avatar.jpg"
# image lamb = "char/lamb/normal.png"


define character.lingyun = CharacterWithData("飞雨凌云", "凌云", image="lingyun", what_prefix="", what_suffix="")

transform tclingyun:
    yanchor 0.5 subpixel True
    zoom 0.75

# image side lingyun = "char/lingyun/avatar.jpg"
# image lingyun = "char/lingyun/normal.png"


define character.lv = CharacterWithData("小绿君", image="lv", what_prefix="# ", what_suffix="")

# image side lv = "char/lv/avatar.jpg"
# image lv = "char/lv/normal.png"


define character.maoyuna = CharacterWithData("MaoYuNa133", image="maoyuna", what_prefix="", what_suffix="")

# image side maoyuna = "char/maoyuna/avatar.jpg"
# image maoyuna = "char/maoyuna/normal.png"


define character.morin = CharacterWithData("莫邪Morin", "莫邪", image="morin", what_prefix="", what_suffix="")

transform tcmorin:
    yanchor 0.5 subpixel True
    zoom 1.125

# image side morin = "char/morin/avatar.jpg"
image morin = At("char/morin/normal.png", tcmorin)


define character.mwam = CharacterWithData("ms_win_and_mc", "李婉清", image="mwam", what_prefix="", what_suffix="")

transform tcmwam:
    yanchor 0.5 subpixel True
    zoom 0.75

# image side mwam = "char/mwam/avatar.jpg"
image mwam = At("char/mwam/normal.png", tcmwam)
image mwam smile = At("char/mwam/smile.png", tcmwam)
image mwam happy = At("char/mwam/happy.png", tcmwam)
image mwam sad = At("char/mwam/sad.png", tcmwam)
image mwam angry = At("char/mwam/angry.png", tcmwam)


define character.nona = CharacterWithData("怃", image="nona", what_prefix="", what_suffix="")

# image side nona = "char/nona/avatar.jpg"
# image nona = "char/nona/normal.png"


define character.pumi = CharacterWithData("Pumi", image="pumi", what_prefix="", what_suffix="")

# image side pumi = "char/pumi/avatar.jpg"
# image pumi = "char/pumi/normal.png"


define character.uni = CharacterWithData("UNI", image="uni", what_prefix="", what_suffix="")

# image side uni = "char/uni/avatar.jpg"
# image uni = "char/uni/normal.png"


define character.yangsy = CharacterWithData("Yangsy56302", "杨曦", image="yangsy", what_prefix="\" ", what_suffix=" \"")

transform tcyangsy:
    yanchor 0.65625 subpixel True
    zoom 2.5 nearest True

# image side yangsy = "char/yangsy/avatar.jpg"
image yangsy = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_happy.png", (0, 0), "char/yangsy/eye_tareme.png", (0, 0), "char/yangsy/mouth_cat_happy.png"), tcyangsy)
image yangsy angry = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_angry.png", (0, 0), "char/yangsy/eye_jitome.png", (0, 0), "char/yangsy/mouth_sad_open.png"), tcyangsy)
image yangsy bulb = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_happy.png", (0, 0), "char/yangsy/eye_tareme.png", (0, 0), "char/yangsy/mouth_happy_open.png"), tcyangsy)
image yangsy chat = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_tareme.png", (0, 0), "char/yangsy/mouth_neutral_open.png"), tcyangsy)
image yangsy dot = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_jitome.png"), tcyangsy)
image yangsy exclaim = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_angry.png", (0, 0), "char/yangsy/eye_gtlt.png", (0, 0), "char/yangsy/mouth_neutral_open.png"), tcyangsy)
image yangsy heart = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_jitome.png", (0, 0), "char/yangsy/blush.png", (0, 0), "char/yangsy/mouth_happy.png"), tcyangsy)
image yangsy music = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_tareme.png", (0, 0), "char/yangsy/mouth_cat_happy_open.png"), tcyangsy)
image yangsy question = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_happy.png", (0, 0), "char/yangsy/eye_tareme.png", (0, 0), "char/yangsy/mouth_neutral_open.png"), tcyangsy)
image yangsy respond = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_tareme.png", (0, 0), "char/yangsy/mouth_cat_happy_open.png"), tcyangsy)
image yangsy shy = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_happy.png", (0, 0), "char/yangsy/eye_gtlt.png", (0, 0), "char/yangsy/blush.png", (0, 0), "char/yangsy/mouth_cat_sad.png"), tcyangsy)
image yangsy sigh = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_flat.png", (0, 0), "char/yangsy/mouth_neutral_open.png"), tcyangsy)
image yangsy steam = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_angry.png", (0, 0), "char/yangsy/eye_gtlt.png", (0, 0), "char/yangsy/blush.png", (0, 0), "char/yangsy/mouth_cat_sad.png"), tcyangsy)
image yangsy surprise = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_angry.png", (0, 0), "char/yangsy/eye_tareme.png", (0, 0), "char/yangsy/mouth_sad_open.png"), tcyangsy)
image yangsy sweat = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_jitome.png", (0, 0), "char/yangsy/blush.png", (0, 0), "char/yangsy/mouth_cat_happy.png"), tcyangsy)
image yangsy tear = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_sad.png", (0, 0), "char/yangsy/eye_gtlt.png", (0, 0), "char/yangsy/mouth_cat_sad.png"), tcyangsy)
image yangsy think = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_angry.png", (0, 0), "char/yangsy/eye_jitome.png", (0, 0), "char/yangsy/mouth_neutral.png"), tcyangsy)
image yangsy twinkle = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_happy.png", (0, 0), "char/yangsy/eye_jitome.png", (0, 0), "char/yangsy/blush.png", (0, 0), "char/yangsy/mouth_happy_open.png"), tcyangsy)
image yangsy upset = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_jitome.png", (0, 0), "char/yangsy/mouth_sad.png"), tcyangsy)
image yangsy zzz = At(Composite((200, 500), (0, 0), "char/yangsy/body.png", (0, 0), "char/yangsy/bow_flat.png", (0, 0), "char/yangsy/eye_flat.png", (0, 0), "char/yangsy/blush.png", (0, 0), "char/yangsy/mouth_cat_happy.png"), tcyangsy)


define character.yoosee = CharacterWithData("祐荽", image="yoosee", what_prefix="", what_suffix="")

# image side yoosee = "char/yoosee/avatar.jpg"
# image yoosee = "char/yoosee/normal.png"
