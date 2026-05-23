init python:

    class CharacterWithNVL(renpy.character.ADVCharacter):
        def __init__(self, name, **properties):
            super().__init__(name, **properties)
            self.nvl = Character(name, kind=nvl, **properties)
    
    class CharacterWithData(CharacterWithNVL):
        def __init__(self, name, realname=None, **properties):
            super().__init__(self.get_name, dynamic=True, **properties)
            self.nickname = name
            self.realname = name if realname is None else realname
            self.meet_irl = False
            # self.affection = 0
        def get_name(self):
            return self.realname if self.meet_irl else self.nickname
        def str(self):
            return self.get_name()


default persistent.name_mc = ""
default name_mc = ""
define mc = CharacterWithNVL("name_mc", dynamic=True)


define guide = CharacterWithData("？？？")


define ashell = CharacterWithData("阿希尔Ashell", image="ashell", what_prefix="a ", what_suffix="")

# image side ashell = "char/ashell/avatar.jpg"
# image ashell = "char/ashell/normal.png"


define baile = CharacterWithData("终究是摆了", "李星眠", image="baile", what_prefix="", what_suffix="")

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


define dwen = CharacterWithData("是动听D温呐", image="dwen", what_prefix="~ ", what_suffix="")

# image side dwen = "char/dwen/avatar.jpg"
# image dwen = "char/dwen/normal.png"


define gra = CharacterWithData("晴柚-Grafrustix", "晴安柚子", image="gra", what_prefix="< ", what_suffix=" 3")

transform tcgra:
    yanchor 0.625 subpixel True
    zoom 0.75

# image side gra = "char/gra/avatar.jpg"
image gra = At("char/gra/normal.png", tcgra)
image gra flirt = At("char/gra/flirt.png", tcgra)


define hale = CharacterWithData("TheHale", image="hale", what_prefix="", what_suffix="")

# image side hale = "char/hale/avatar.jpg"
# image hale = "char/hale/normal.png"


define lamb = CharacterWithData("Happylamb029", image="lamb", what_prefix="", what_suffix="")

# image side lamb = "char/lamb/avatar.jpg"
# image lamb = "char/lamb/normal.png"


define lingyun = CharacterWithData("飞雨凌云", "凌云", image="lingyun", what_prefix="", what_suffix="")

transform tclingyun:
    yanchor 0.5 subpixel True
    zoom 0.75

# image side lingyun = "char/lingyun/avatar.jpg"
# image lingyun = "char/lingyun/normal.png"


define lv = CharacterWithData("小绿君", image="lv", what_prefix="# ", what_suffix="")

# image side lv = "char/lv/avatar.jpg"
# image lv = "char/lv/normal.png"


define maoyuna = CharacterWithData("MaoYuNa133", image="maoyuna", what_prefix="", what_suffix="")

# image side maoyuna = "char/maoyuna/avatar.jpg"
# image maoyuna = "char/maoyuna/normal.png"


define morin = CharacterWithData("莫邪Morin", "莫邪", image="morin", what_prefix="", what_suffix="")

transform tcmorin:
    yanchor 0.5 subpixel True
    zoom 1.125

# image side morin = "char/morin/avatar.jpg"
image morin = At("char/morin/normal.png", tcmorin)


define mwam = CharacterWithData("ms_win_and_mc", "李婉清", image="mwam", what_prefix="", what_suffix="")

transform tcmwam:
    yanchor 0.5 subpixel True
    zoom 0.75

# image side mwam = "char/mwam/avatar.jpg"
image mwam = At("char/mwam/normal.png", tcmwam)
image mwam smile = At("char/mwam/smile.png", tcmwam)
image mwam happy = At("char/mwam/happy.png", tcmwam)
image mwam sad = At("char/mwam/sad.png", tcmwam)
image mwam angry = At("char/mwam/angry.png", tcmwam)


define nona = CharacterWithData("怃", image="nona", what_prefix="", what_suffix="")

# image side nona = "char/nona/avatar.jpg"
# image nona = "char/nona/normal.png"


define pumi = CharacterWithData("Pumi", image="pumi", what_prefix="", what_suffix="")

# image side pumi = "char/pumi/avatar.jpg"
# image pumi = "char/pumi/normal.png"


define uni = CharacterWithData("UNI", image="uni", what_prefix="", what_suffix="")

# image side uni = "char/uni/avatar.jpg"
# image uni = "char/uni/normal.png"


define yangsy = CharacterWithData("Yangsy56302", "杨曦", image="yangsy", what_prefix="\" ", what_suffix=" \"")

transform tcyangsy:
    yanchor 0.65625 subpixel True
    zoom 2.5 nearest True

layeredimage yangsy:
    at tcyangsy
    group body prefix body:
        attribute _default default:
            "char/yangsy/body/default.png"
        attribute without_bag:
            "char/yangsy/body/without_bag.png"
        attribute without_legwear:
            "char/yangsy/body/without_legwear.png"
        attribute without_both:
            "char/yangsy/body/without_both.png"
    group brow prefix brow:
        attribute angry: 
            "char/yangsy/brow/angry.png"
        attribute flat default:
            "char/yangsy/brow/flat.png"
        attribute happy: 
            "char/yangsy/brow/happy.png"
        attribute sad: 
            "char/yangsy/brow/sad.png"
    group eye prefix eye:
        attribute flat:
            "char/yangsy/eye/flat.png"
        attribute gtlt:
            "char/yangsy/eye/gtlt.png"
        attribute jitome:
            "char/yangsy/eye/jitome.png"
        attribute tareme default:
            "char/yangsy/eye/tareme.png"
    group mouth prefix mouth:
        attribute cat_happy default: 
            "char/yangsy/mouth/cat_happy.png"
        attribute cat_happy_open: 
            "char/yangsy/mouth/cat_happy_open.png"
        attribute cat_sad: 
            "char/yangsy/mouth/cat_sad.png"
        attribute cat_sad_open: 
            "char/yangsy/mouth/cat_sad_open.png"
        attribute happy: 
            "char/yangsy/mouth/happy.png"
        attribute happy_open: 
            "char/yangsy/mouth/happy_open.png"
        attribute neutral: 
            "char/yangsy/mouth/neutral.png"
        attribute neutral_open: 
            "char/yangsy/mouth/neutral_open.png"
        attribute sad: 
            "char/yangsy/mouth/sad.png"
        attribute sad_open: 
            "char/yangsy/mouth/sad_open.png"
    attribute blush:
        "char/yangsy/blush.png"


define yoosee = CharacterWithData("祐荽", image="yoosee", what_prefix="", what_suffix="")

# image side yoosee = "char/yoosee/avatar.jpg"
# image yoosee = "char/yoosee/normal.png"

define myworldzycpc = CharacterWithData("myworldzycpc", image="myworldzycpc", what_prefix="", what_suffix="")

# image side myworldzycpc = "char/myworldzycpc/avatar.jpg"
# image myworldzycpc = "char/myworldzycpc/normal.png"
