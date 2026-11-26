label bone_ch8:
    "ch8"

    yangsy.comment "此时可能已经有部分支线彻底离开主线跑路了，别管（"

    if variables["yangsy_route"]:

        play sound "snd_screen_wipe_out.wav"
        scene black with wipeadofai

        with Pause(1.0)

        play sound "snd_screen_wipe_in.wav"
        scene bg sky with wipeadofai

        "短时间之内第二次出远门让父母开始有些——说是怀疑不太准确，说是担心也不要太对，总之很在意。"
        "不过我花了些办法终于让父母能够确信我还会回家因此放我走了。"
        "我现在正坐在开往■■市方向的列车上。"
        "虽说不是第一次坐火车了，这种感觉还是很新奇。"
        "不过我并不是很在意那些东西——我在意的是我坐在这里的原因。"
        "到底该从哪里算起呢？是接触到电脑的那一天吗？还是接触冰与火之舞的那一天？又或者是魔改？[gra]？[yangsy]？"
        "{......}这很难说。很多事情的界限划分往往并不是那么精确。"
        "或许我不应该想那么多。至少不是往这个方向上想。"

        play sound "snd_screen_wipe_out.wav"
        scene black with wipeadofai

        yangsy.comment "写累了，时间跳跃（"

        play sound "snd_screen_wipe_in.wav"
        scene bg sky with wipeadofai

        "我唯一知道的信息就是Yangsy会在每周六出门的时候经过西直门地铁站两次。"
        "尽管我已经通过以往的聊天记录摸清楚了大概的时间范围，\n不过即便如此，在茫茫人海中找到正确的人也是如同大海捞针一般难的事情。"
        "所以我想了个主意。\n要形容的话就是，试着用磁铁把针给吸过来。"
        "话又说回来了——拿着只一米宽的11-X螃蟹的我在人群中本来就很显眼。\n显然这个“磁铁”吸引到了一大堆我没打算去找的东西。"
        "但我能看出来到目前为止那些注意到我的那些人的神情——他们不认识这玩意。\n并且这其中大部分也都是瞥了一眼就跟没事人一样继续低头刷手机该咋走咋走了。"
        "因此我只需要留意那些视线停留时长超过一秒的人。\n好吧说实话这并没有对现在这个十分棘手的情况有多大的改善。"
        "我越发感觉这像是个捉迷藏游戏。"

        yangsy.comment "好的这里切一下视角"

        $ variables["another_view"] = True
        $ current_perspective = yangsy

        show yangsy fm_cs fp_l at l41
        yangsy "传送带人好多{...}还是走楼梯吧。"
        show yangsy at t42
        yangsy fb_n fe_f fp_non fm_no "话说为啥网上都在说西直门换乘很折磨啊，明明感觉也没多长的样子{......}"
        show yangsy at t11
        yangsy fe_t fp_l "是因为已经习惯了吗？还是因为{......}{nw}"
        $ _history_list.pop()
        yangsy fb_h fp_r fm_cs "是因为已经习惯了吗？还是因为{......}{fast}嗯？"
        show yangsy at h11
        yangsy swt shd fm_n "（不对。不对不对。不对不对不对！）"
        show yangsy at t42
        yangsy fb_a fp_l fm_a "（我该怎么办？我是不是该跑路？他是不是已经看到我了？）"
        show yangsy at d42
        yangsy fb_s fe_f fp_non fm_so "（不要紧张不要紧张不要紧张啊这里是地铁站啊大庭广众下他肯定是不敢杀人的啊安检员是肯定不会放过任何的管制刀具之类的凶器的啊……）"

        $ variables["another_view"] = False
        $ current_perspective = mc

        with Pause(1)

        show yangsy -shd fm_cs at f11

        with Pause(1)

        yangsy fe_t fp_r fm_no "呃{......}{nw}"
        $ _history_list.pop()
        show yangsy at h11
        yangsy bls fb_a fp_c fm_cho "呃{......}{fast}嗨？你是？"
        show yangsy fp_l fm_ch
        mc "我是[mc]。"
        
        show yangsy at rhide
        hide yangsy

        play sound "snd_screen_wipe_out.wav"
        scene black with wipeadofai

        yangsy.comment "算了今天先写到这里吧（"

    else:
        yangsy.comment "oclcc可能会来新人；哦对aclcc成为oclcc的原因也可以岁月史书一下，就说我们觉得圈子开放一些比较好"
        yangsy.comment "又或者这里也可以出俩分支——aclcc是要成为大概十几人或几十人朋友的熟人小圈子还是成为上百人的单纯因为魔改才存在的大圈子"
        yangsy.comment "各有千秋吧，小圈子联系更深，大圈子更有活力，嗯"

    jump bone_ch9