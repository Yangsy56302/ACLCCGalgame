init python:
    class CharacterDataKey:
        def __init__(self, name: str):
            self.name = name

    AFFECTION = CharacterDataKey("affection")

    class CharacterWithData(renpy.character.ADVCharacter):
        def __init__(self, name, realname=None, **properties):
            properties["dynamic"] = True
            super().__init__(self.get_name, **properties)
            self.nickname = name
            self.realname = realname
            self.meet_irl = False
            self.meet_irl_nvl = False

            self.nvl = Character(self.get_nvl_name, kind=nvl, **properties)
            
            old_what_text_align = properties.get("what_text_align", None)
            old_what_xalign = properties.get("what_xalign", None)
            properties["what_text_align"] = 0.5
            properties["what_xalign"] = 0.5
            self.center = Character(name, **properties)
            self.nvl.center = Character(self.get_nvl_name, kind=nvl, **properties)

            properties["what_text_align"] = old_what_text_align
            properties["what_xalign"] = old_what_xalign

            properties["what_prefix"] = "# " + properties.get("what_prefix", "")
            properties["what_color"] = "#808080"
            properties["dynamic"] = False
            self.comment = Character(name, **properties)
            self.nvl.comment = Character(name, kind=nvl, **properties)

            properties["what_text_align"] = 0.5
            properties["what_xalign"] = 0.5
            self.comment.center = Character(name, **properties)
            self.nvl.comment.center = Character(name, kind=nvl, **properties)

            self.data: dict[CharacterDataKey, object] = {}

        def get_name(self):
            if self.realname is None:
                return self.nickname
            if self.meet_irl:
                return self.realname
            return self.nickname

        def get_nvl_name(self):
            if self.realname is None:
                return self.nickname
            if self.meet_irl_nvl:
                return self.realname
            return self.nickname

        def __str__(self):
            return self.get_name()

        def __getitem__(self, key: CharacterDataKey):
            return self.data[key]

default persistent.name_mc = ""
default mc = CharacterWithData("undefined")


default setup = CharacterWithData("？？？")


default ashell = CharacterWithData("阿希尔Ashell", image="ashell", what_prefix="a ", what_suffix="")

# image side ashell = "char/ashell/avatar.jpg"
# image ashell = "char/ashell/normal.png"


default baile = CharacterWithData("终究是摆了", "李星眠", image="baile", what_prefix="", what_suffix="")

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


default dwen = CharacterWithData("是动听D温呐", image="dwen", what_prefix="~ ", what_suffix="")

# image side dwen = "char/dwen/avatar.jpg"
# image dwen = "char/dwen/normal.png"


default gra = CharacterWithData("晴柚-Grafrustix", "晴安柚子", image="gra", what_prefix="< ", what_suffix=" 3")

transform tcgra:
    yanchor 0.625 subpixel True
    zoom 0.75

# image side gra = "char/gra/avatar.jpg"
image gra = At("char/gra/normal.png", tcgra)
image gra flirt = At("char/gra/flirt.png", tcgra)


default hale = CharacterWithData("TheHale", image="hale", what_prefix="", what_suffix="")

# image side hale = "char/hale/avatar.jpg"
# image hale = "char/hale/normal.png"


default lamb = CharacterWithData("Happylamb029", image="lamb", what_prefix="", what_suffix="")

# image side lamb = "char/lamb/avatar.jpg"
# image lamb = "char/lamb/normal.png"


default lingyun = CharacterWithData("飞雨凌云", "凌云", image="lingyun", what_prefix="", what_suffix="")

transform tclingyun:
    yanchor 0.5 subpixel True
    zoom 0.75

# image side lingyun = "char/lingyun/avatar.jpg"
# image lingyun = "char/lingyun/normal.png"


default lv = CharacterWithData("小绿君", image="lv", what_prefix="# ", what_suffix="")

# image side lv = "char/lv/avatar.jpg"
# image lv = "char/lv/normal.png"


default maoyuna = CharacterWithData("MaoYuNa133", image="maoyuna", what_prefix="", what_suffix="")

# image side maoyuna = "char/maoyuna/avatar.jpg"
# image maoyuna = "char/maoyuna/normal.png"


default morin = CharacterWithData("莫邪Morin", "莫邪", image="morin", what_prefix="", what_suffix="")

transform tcmorin:
    yanchor 0.5 subpixel True
    zoom 1.125

# image side morin = "char/morin/avatar.jpg"
image morin = At("char/morin/normal.png", tcmorin)


default mwam = CharacterWithData("ms_win_and_mc", "李婉清", image="mwam", what_prefix="", what_suffix="")

transform tcmwam:
    yanchor 0.5 subpixel True
    zoom 0.75

# image side mwam = "char/mwam/avatar.jpg"
image mwam = At("char/mwam/normal.png", tcmwam)
image mwam smile = At("char/mwam/smile.png", tcmwam)
image mwam happy = At("char/mwam/happy.png", tcmwam)
image mwam sad = At("char/mwam/sad.png", tcmwam)
image mwam angry = At("char/mwam/angry.png", tcmwam)


default nona = CharacterWithData("怃", image="nona", what_prefix="", what_suffix="")

# image side nona = "char/nona/avatar.jpg"
# image nona = "char/nona/normal.png"


default pumi = CharacterWithData("Pumi", image="pumi", what_prefix="", what_suffix="")

# image side pumi = "char/pumi/avatar.jpg"
# image pumi = "char/pumi/normal.png"


default uni = CharacterWithData("UNI", image="uni", what_prefix="", what_suffix="")

# image side uni = "char/uni/avatar.jpg"
# image uni = "char/uni/normal.png"


default yangsy = CharacterWithData("Yangsy56302", "杨曦", image="yangsy", what_prefix="\" ", what_suffix=" \"")

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


default yoosee = CharacterWithData("祐荽", image="yoosee", what_prefix="", what_suffix="")

# image side yoosee = "char/yoosee/avatar.jpg"
# image yoosee = "char/yoosee/normal.png"

default myworldzycpc = CharacterWithData("myworldzycpc", image="myworldzycpc", what_prefix="", what_suffix="")

# image side myworldzycpc = "char/myworldzycpc/avatar.jpg"
# image myworldzycpc = "char/myworldzycpc/normal.png"

default comment = CharacterWithData("# ", what_color="#808080")

define narrator = CharacterWithData(None)