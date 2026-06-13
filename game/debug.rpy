init python:
    is_debug_installed = True


screen debug_mode(title, scroll=None, yinitial=0.0):
    tag menu
    style_prefix "game_menu" 
    
    if main_menu:
        add gui.main_menu_background 
    else:
        add gui.game_menu_background 
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"
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
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        if is_ingame:
            textbutton _("Variable") action ShowMenu("variable") text_font debug_gui_font

            textbutton _("Persistent Variable"):
                action ShowMenu("per_variable")
                text_font debug_gui_font
                text_size 27

    textbutton _("Return"):
        style "return_button"
        text_font debug_gui_font
        action Return()
            

    label title text_font debug_gui_font

screen variable():
    tag menu
    use debug_mode("Variable"):
        vbox:
            text "another_view:" font debug_gui_font
            if another_view:
                textbutton "True":
                    action SetVariable("another_view",False)
                    text_font debug_gui_font
            else:
                textbutton "False":
                    action SetVariable("another_view",True)
                    text_font debug_gui_font
            text "gra_chemistry_name:" font debug_gui_font
            if gra_chemistry_name:
                textbutton "True":
                    action SetVariable("gra_chemistry_name",False)
                    text_font debug_gui_font
            else:
                textbutton "False":
                    action SetVariable("gra_chemistry_name",True)
                    text_font debug_gui_font
            text "overwatch_first:" font debug_gui_font
            if overwatch_first:
                textbutton "True":
                    action SetVariable("overwatch_first",False)
                    text_font debug_gui_font
            else:
                textbutton "False":
                    action SetVariable("overwatch_first",True)
                    text_font debug_gui_font
            text "volunteer_to_do_curse:" font debug_gui_font
            if volunteer_to_do_curse:
                textbutton "True":
                    action SetVariable("volunteer_to_do_curse",False)
                    text_font debug_gui_font
            else:
                textbutton "False":
                    action SetVariable("volunteer_to_do_curse",True)
                    text_font debug_gui_font
screen per_variable():
    tag menu
    use debug_mode("Persistent Variable"):
        vbox:
            text "has_seen_ending:" font debug_gui_font
            if persistent.has_seen_ending:
                textbutton "True":
                    action SetVariable("persistent.has_seen_ending",False)
                    text_font debug_gui_font
            else:
                textbutton "False":
                    action SetVariable("persistent.has_seen_ending",True)
                    text_font debug_gui_font

            text "duplicate_name_fixed:" font debug_gui_font
            if persistent.duplicate_name_fixed:
                textbutton "True":
                    action SetVariable("persistent.duplicate_name_fixed",False)
                    text_font debug_gui_font
            else:
                textbutton "False":
                    action SetVariable("persistent.duplicate_name_fixed",True)
                    text_font debug_gui_font

            text "setup_saw_debug_screen:" font debug_gui_font
            if persistent.setup_saw_debug_screen:
                textbutton "True":
                    action SetVariable("persistent.setup_saw_debug_screen",False)
                    text_font debug_gui_font
            else:
                textbutton "False":
                    action SetVariable("persistent.setup_saw_debug_screen",True)
                    text_font debug_gui_font

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
