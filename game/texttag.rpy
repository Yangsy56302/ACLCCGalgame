init python:

    def texttag_color(color: str):
        def texttag_color_inner(tag: str, argument: str, contents: list[int, str]) -> list[int, str]: 
            return [
                (renpy.TEXT_TAG, f"color={color}"),
            ] + contents + [
                (renpy.TEXT_TAG, "/color"),
            ]
        return texttag_color_inner
    
    def texttag_at(tag: str, argument: str, contents: list[int, str]) -> list[int, str]: 
        "{at}[yoosee.nvl]{/at} -> @ゆすい"
        return [
            (renpy.TEXT_TAG, "atcolor"),
            (renpy.TEXT_TEXT, "@"),
        ] + contents + [
            (renpy.TEXT_TAG, "/atcolor"),
        ]
    
    def texttag_reply(tag: str, argument: str, contents: list[int, str]) -> list[int, str]: 
        "[myworld.nvl]{reply}😰{/reply} -> myworldzycpc回应了你的消息：😰"
        return [
            (renpy.TEXT_TEXT, "回应了你的消息："),
        ] + contents

    def texttag_poke(tag: str, argument: str, contents: list[int, str]) -> list[int, str]:
        "你{poke=nonym}[nonym.nvl]{/poke} -> 你揉了揉实在没必要取昵称的毛茸茸的兔耳朵uwu"
        poke_reaction = poke_reactions.get(argument, ("戳了戳", ))
        if len(poke_reaction) == 1:
            return [
                (renpy.TEXT_TEXT, f"{poke_reaction[0]}"),
            ] + contents
        return [
            (renpy.TEXT_TEXT, f"{poke_reaction[0]}"),
        ] + contents + [
            (renpy.TEXT_TEXT, f"{poke_reaction[1]}"),
        ]

    def text_filter_ellipsis(text: str) -> str:
        return text.replace(
            "{...}", 
            "{cps=*0.25}...\u200B{/cps}"
        ).replace(
            "{......}", 
            "{cps=*0.25}......\u200B{/cps}"
        )

define poke_reactions = {
    "myworld": ("戳了戳", ),
    "morin": ("揉了揉", "的脸，嘿嘿⊙▽⊙"),
    "nonym": ("揉了揉", "的毛茸茸的兔耳朵uwu"),
    "yangsy": ("拍了拍", "的头像，One!"),
}

define config.custom_text_tags = {
    "green": texttag_color("#5fff4e"),
    "yellow": texttag_color("#fcff4d"),
    "orange": texttag_color("#ff6f4d"),
    "red": texttag_color("#ff0000"),
    "magenta": texttag_color("#da59ff"),
    "atcolor": texttag_color("#0080ff"),
    "at": texttag_at,
    "poke": texttag_poke,
    "reply": texttag_reply,
}

define config.say_menu_text_filter = text_filter_ellipsis