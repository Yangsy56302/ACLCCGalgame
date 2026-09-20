init python:
    is_debug_installed = True
    

screen debug_menu(title, scroll=None, yinitial=0.0):
    tag menu
    style_prefix "debug_menu"
    
    if main_menu:
        add gui.main_menu_background 
    else:
        add gui.game_menu_background 
    frame:
        style "debug_menu_outer_frame"
        hbox:
            frame:
                style "debug_menu_navigation_frame"

            frame:
                style "debug_menu_content_frame"
                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
    vbox:
        style_prefix "debug_menu_navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        if is_ingame:
            textbutton _("Variable") action ShowMenu("variable")

        textbutton _("Persistent Variable"):
            action ShowMenu("per_variable")

    textbutton _("Return"):
        style "return_button"
        action ShowMenu("debug_screen")
    
    
    label title


screen variable():
    tag menu
    use debug_menu("Variable"):
        vbox:
            style_prefix "debug_menu"

            text "another_view:"
            if another_view:
                textbutton "True":
                    action SetVariable("another_view",False)
            else:
                textbutton "False":
                    action SetVariable("another_view",True)

            text "gra_chemistry_name:"
            if gra_chemistry_name:
                textbutton "True":
                    action SetVariable("gra_chemistry_name",False)
            else:
                textbutton "False":
                    action SetVariable("gra_chemistry_name",True)

            text "overwatch_first:"
            if overwatch_first:
                textbutton "True":
                    action SetVariable("overwatch_first",False)
            else:
                textbutton "False":
                    action SetVariable("overwatch_first",True)

            text "volunteer_to_do_curse:"
            if volunteer_to_do_curse:
                textbutton "True":
                    action SetVariable("volunteer_to_do_curse",False)
            else:
                textbutton "False":
                    action SetVariable("volunteer_to_do_curse",True)


screen per_variable():
    tag menu
    use debug_menu("Persistent Variable"):
        vbox:
            style_prefix "debug_menu"

            text "has_seen_ending:"
            if persistent.has_seen_ending:
                textbutton "True":
                    action SetVariable("persistent.has_seen_ending",False)
            else:
                textbutton "False":
                    action SetVariable("persistent.has_seen_ending",True)

            text "duplicate_name_fixed:"
            if persistent.duplicate_name_fixed:
                textbutton "True":
                    action SetVariable("persistent.duplicate_name_fixed",False)
            else:
                textbutton "False":
                    action SetVariable("persistent.duplicate_name_fixed",True)

            text "setup_saw_debug_screen:"
            if persistent.setup_saw_debug_screen:
                textbutton "True":
                    action SetVariable("persistent.setup_saw_debug_screen",False)
            else:
                textbutton "False":
                    action SetVariable("persistent.setup_saw_debug_screen",True)


label debug_unlock(Type):
    nvl clear
    debug "unlock: Now unlocking all [Type]{fast}{w=1.0}{nw}"
    if Type == "CG":
        scene bg home_midnight
        scene bg home_night
        scene bg home_noon
        scene bg sbeam
        scene bg sky
        scene bg sky_night
        scene bg star
        scene bg that_video
        scene black
        debug "unlock: Success.{fast}{w=1.0}{nw}"
    elif Type == "Music":
        play music "mus_astral_calm.mp3"
        play music "mus_aurora.mp3"
        play music "mus_setup.ogg"
        stop music
        debug "unlock: Success.{fast}{w=1.0}{nw}"
    else:
        debug "unlock: Failed to find [Type]{fast}{w=1.0}{nw}"
    if is_ingame:
        return
    else:
        $ renpy.full_restart()


label debug(thing):
    if thing == "reset":
        nvl clear
        menu(nvl=True):
            debug "clean: Do you want to Clear All Persistent Data? (Y/N){fast}"
            "{font=MapleMono.otf}Yes{/font}":
                nvl clear
                debug "clean: Do you want to Clear All Persistent Data? (Y/N) Y{fast}{w=1.0}{nw}"
                debug "clean: Success.{fast}{w=1.0}{nw}"
                $ persistent._clear(progress=True)
            "{font=MapleMono.otf}No{/font}":
                nvl clear
                debug "clean: Do you want to Clear All Persistent Data? (Y/N) N{fast}{w=1.0}{nw}"
                pass
        $ persistent.debug_mode = True
    if is_ingame:
        return
    else:
        $ renpy.full_restart()


screen debug_confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5
                text_font debug_gui_font

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action text_font debug_gui_font
                textbutton _("No") action no_action text_font debug_gui_font
