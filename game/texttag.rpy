init python:

    def texttag_color(color):
        return lambda tag, argument, contents: [
            (renpy.TEXT_TAG, f"color={color}"),
        ] + contents + [
            (renpy.TEXT_TAG, "/color"),
        ]
    
    def texttag_ellipsis(tag, argument):
        return [
            (renpy.TEXT_TAG, "cps=*0.25"),
            (renpy.TEXT_TEXT, "...\u200B"),
            (renpy.TEXT_TAG, "/cps"),
        ]
    
    def texttag_ellipsis2(tag, argument):
        return [
            (renpy.TEXT_TAG, "cps=*0.25"),
            (renpy.TEXT_TEXT, "......\u200B"),
            (renpy.TEXT_TAG, "/cps"),
        ]
    
    def texttag_at(tag, argument):
        return [
            (renpy.TEXT_TAG, "color=#0080ff"),
            (renpy.TEXT_TEXT, "@{}".format(argument)),
            (renpy.TEXT_TAG, "/color"),
        ]
    
    config.custom_text_tags["green"] = texttag_color("#5fff4e")
    config.custom_text_tags["yellow"] = texttag_color("#fcff4d")
    config.custom_text_tags["orange"] = texttag_color("#ff6f4d")
    config.custom_text_tags["red"] = texttag_color("#ff0000")
    config.custom_text_tags["magenta"] = texttag_color("#da59ff")
    config.self_closing_custom_text_tags["..."] = texttag_ellipsis
    config.self_closing_custom_text_tags["......"] = texttag_ellipsis2
    config.self_closing_custom_text_tags["at"] = texttag_at