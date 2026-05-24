label vibe_epilogue:
    scene black with fade

    play music "audio/mus_aurora.mp3" fadein 3.0

    "多年以后。"

    "你坐在电脑前，\n习惯性地打开那个置顶的群聊。"

    "ACLCC 已经是一个很大的社区了。\n群里时不时有人发新的魔改作品，\n有人求助技术问题，\n有人在闲聊吹水。"

    "偶尔会有新人问——\n"ACLCC 是怎么来的？""

    "然后就会有老人给他们讲过去的故事。\n讲那个叫 ACLC 的群，\n讲螃蟹事件，讲解散，\n讲一群人在废墟上重建了一个社区。"

    "新人们听完，感慨地说"好厉害"。\n他们不知道——\n那些故事里，有多少失落，多少遗憾，多少没说完的话。"

    "但他们也不需要知道。\n重要的是，这个社区还在。"

    nvl clear

    "你打开 ACLCC 的网站——\n现在它已经迭代了好几个版本。\n不再是当初 baile 和 lv 搭的那个简单的页面了。\n但首页上还是那句话："

    "{cps=*0.5}欢迎所有热爱魔改的人{/cps}"

    "你笑了笑，关掉了浏览器。"

    nvl clear

    "你的手机震了一下。\n是群里有人 @ 了你。"

    "你点开看了看——\n有人在问一个关于魔改的问题。\n你打字回复了他。"

    "很简单。很日常。\n和过去无数个日日夜夜一样。"

    "你把手机放在桌上，伸了个懒腰。\n窗外是普通的夜空。\n没有星星——城市的灯光太亮了。"

    "但你想起了一个很遥远的夜晚——\n有人告诉过你，宇宙这么大。\n不要因为一点挫折就觉得一切都结束了。"

    nvl clear

    "ACLC 曾经死过一次。\n但 ACLCC 还在。\nGra 回来了，Yangsy 也回来了。\n一些人走了，更多的人来了。"

    "故事还在继续。\n而你是它的一部分。"

    "这个游戏叫 ACLCC Galgame。\n但说到底，这不是一个关于魔改的故事——"

    "{cps=*0.5}这是关于一群在数字世界里找到彼此的人的故事。{/cps}"

    nvl clear
    stop music fadeout 5.0

    pause 2.0

    "{size=+4}{color=#cccccc}—— Fin ——{/color}{/size}"

    pause 1.5

    $ persistent.has_seen_ending = True

    scene black with fade

    menu:
        "感谢游玩。"
        "返回主菜单":
            return
