init python:
    
    def texttag_green(tag, argument, contents):
        return [
            (renpy.TEXT_TAG, "color=#5fff4e"),
        ] + contents + [
            (renpy.TEXT_TAG, "/color"),
        ]
    
    def texttag_yellow(tag, argument, contents):
        return [
            (renpy.TEXT_TAG, "color=#fcff4d"),
        ] + contents + [
            (renpy.TEXT_TAG, "/color"),
        ]

    def texttag_orange(tag, argument, contents):
        return [
            (renpy.TEXT_TAG, "color=#ff6f4d"),
        ] + contents + [
            (renpy.TEXT_TAG, "/color"),
        ]

    def texttag_red(tag, argument, contents):
        return [
            (renpy.TEXT_TAG, "color=#ff0000"),
        ] + contents + [
            (renpy.TEXT_TAG, "/color"),
        ]

    def texttag_magenta(tag, argument, contents):
        return [
            (renpy.TEXT_TAG, "color=#da59ff"),
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
    
    config.custom_text_tags["green"] = texttag_green
    config.custom_text_tags["yellow"] = texttag_yellow
    config.custom_text_tags["orange"] = texttag_orange
    config.custom_text_tags["red"] = texttag_red
    config.custom_text_tags["magenta"] = texttag_magenta
    config.self_closing_custom_text_tags["..."] = texttag_ellipsis
    config.self_closing_custom_text_tags["......"] = texttag_ellipsis2