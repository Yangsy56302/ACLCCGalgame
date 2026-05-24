label vibe_route_baile:
    scene black with fade

    play music "audio/mus_aurora.mp3" fadein 3.0

    "你走向了 baile。"

    if ch0ex_oi_has_been_seen:
        "在所有角色里，她是和你相识最久的。\n在OI群里，你们早就是竞争对手兼网友了。\n这份缘分从代码的世界延续到了魔改的世界。"
    else:
        mwam "你们来填吧{nw}"


    nvl clear

    "你们之间有一种默契——\n不需要多说话就能理解的默契。"
    if ch0ex_oi_has_been_seen:
        "也许是因为你们都在 OI 的赛场上战斗过，\n也许是因为你们都在深夜敲过代码。\n但你知道，有些东西比代码更深。"
    else:
        "也许是因为之前的深夜对话，\n你们对某些事情有着独特的暗号。"
        mwam "感觉怪怪的，不知道为什么{nw}"
    "比如，一起看星星。"

    nvl clear

    "ACLCC 重建后的一个夜晚，baile 又像以前一样给你发了照片——"
    "她家天台上的星空。"

    baile.nvl "今晚的星星特别多喵"

    mc.nvl "你在暗示我去找你？"

    baile.nvl "……如果你能来的话"

    "你去了。"

    nvl clear

    scene black with fade

    "你第一次在线下见到 baile。\n她比照片上看起来更小只，\n白色的猫耳发饰在夜风中轻轻晃动。\n她看到你的时候，第一反应是躲到了天台的门后面。"

    baile "你……你真的来了喵"

    mc "不是你叫我来的吗"

    baile "我没想到你真的会来喵……"

    nvl clear

    "你们坐在天台边上。\n她把外套分了一半给你。\n头顶的星空比照片里还要亮。"

    baile "我以前经常一个人来这里喵。\nOI 比赛输了的时候，\n和家里人吵架的时候，\n代码怎么都调不通的时候……"

    baile "但自从认识了你喵——\n我好像来得少了一些"

    mc "为什么？"

    baile "因为不需要了喵。"

    "她转过头看着你。\n蓝色的眼睛里映着星光。"

    baile "因为有人陪我说话了喵。"

    nvl clear

    scene black with fade
    stop music fadeout 3.0

    "李星眠线·结局"
    play music "audio/mus_astral_calm.mp3" fadein 3.0

    "后来，你们经常一起做很多事。"

    "一起在 OJ 上刷题——\n她总是比你快一点，\n然后发一个\"喵\"的表情。\n一起做魔改——\n她写代码，你负责创意。\n一起看星星——\n她教你认星座，你给她讲魔改的故事。"

    "有一天，她靠在你的肩膀上，\n声音很轻很轻地说——"

    baile "以后也想和你一起看星星喵"

    "你低下头看着她。\n她已经闭上了眼睛，\n嘴角带着一丝笑意。\n夜风很轻，星空很亮。"

    "你知道，这就是答案了。"

    jump vibe_epilogue
