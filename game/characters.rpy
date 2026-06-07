init python:
    class CharacterDataKey:
        def __init__(self, name: str):
            self.name = name

    AFFECTION = CharacterDataKey("affection")

    class CharacterWithData(renpy.character.ADVCharacter):
        def __init__(self, name, realname=None, session_title_color=None, meet_irl=False, meet_irl_nvl=False, is_dynamic=True, root=None, **raw_properties):
            self.nickname = name
            self.realname = realname
            self.session_title_color=session_title_color
            self.meet_irl = meet_irl
            self.meet_irl_nvl = meet_irl_nvl
            self.raw_properties = raw_properties
            self.is_dynamic = is_dynamic
            if root is None:
                self.root = self
            else:
                self.root = root
            super().__init__(self.get_name, **raw_properties)

            self.data: dict[CharacterDataKey, object] = {}

        def copy(self, **raw_properties):
            new_raw_properties = self.raw_properties | raw_properties
            obj = self.__class__(self.nickname, self.realname, session_title_color=self.session_title_color, meet_irl=self.meet_irl, meet_irl_nvl=self.meet_irl_nvl, is_dynamic=self.is_dynamic, root=self.root, **new_raw_properties)
            obj.data = self.data
            return obj

        @property
        def char(self):
            return Character(str(self), **self.raw_properties)

        @property
        def nvl(self):
            return self.copy(kind=nvl)

        @property
        def center(self):
            return self.copy(what_text_align=0.5, what_xalign=0.5)

        @property
        def right(self):
            return self.copy(what_text_align=1.0, what_xalign=0.5, who_text_align=0.0, who_xalign=0.85)

        @property
        def comment(self):
            char = self.copy(what_prefix="# " + self.raw_properties.get("what_prefix", ""), what_color="#808080")
            char.is_dynamic = False
            return char

        def get_name(self):
            if not self.is_dynamic or self.realname is None:
                return self.nickname
            if self.meet_irl:
                return self.realname
            return self.nickname

        def get_nvl_name(self):
            if not self.is_dynamic or self.realname is None:
                return self.nickname
            if self.meet_irl_nvl:
                return self.realname
            return self.nickname

        def __str__(self):
            name = self.get_name() if self.raw_properties.get('kind') != nvl else self.get_nvl_name()
            if name is None:
                return ""
            return name

        def __repr__(self):
            return f"CharacterWithData(name={self.nickname}, realname={self.realname}, meet_irl={self.meet_irl}, meet_irl_nvl={self.meet_irl_nvl}, raw_properties={self.raw_properties}, data={self.data})"

        def __getitem__(self, key: CharacterDataKey):
            return self.data[key]

        def __call__(self, what, interact=True, _call_done=True, multiple=None, **kwargs):
            if self.raw_properties.get('kind') == nvl and current_perspective == self.root:
                char = self.right.char
            else:
                char = self.char
            return char(what, interact=interact, _call_done=_call_done, multiple=multiple, **kwargs)


default persistent.name_mc = ""
default mc = CharacterWithData("undefined")
default current_perspective = mc


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


default gra = CharacterWithData("晴柚-Grafrustix", "晴安柚子", image="gra", what_prefix="< ", what_suffix=" 3", session_title_color="#FFAEC9")

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
        attribute normal default:
            "char/yangsy/body/default.png"
        attribute no_bag:
            "char/yangsy/body/without_bag.png"
        attribute no_legwear:
            "char/yangsy/body/without_legwear.png"
        attribute no_both:
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

default narrator = CharacterWithData(None)


default system = narrator.center  # 别名？

define debug = CharacterWithData(None, kind=nvl, what_color="#00ff00")