init python:
    is_debug_installed = True
    

style debug_menu_outer_frame is game_menu_outer_frame
style debug_menu_navigation_frame is game_menu_navigation_frame
style debug_menu_content_frame is game_menu_content_frame
style debug_menu_viewport is game_menu_viewport
style debug_menu_side is game_menu_side
style debug_menu_scrollbar is game_menu_scrollbar
style debug_menu_text is gui_text
style debug_menu_label is game_menu_label
style debug_menu_label_text is game_menu_label_text
style debug_menu_button is gui_button
style debug_menu_button_text is gui_button_text
style debug_menu_return_button is return_button
style debug_menu_return_button_text is return_button_text
style debug_menu_navigation_button is gui_button
style debug_menu_navigation_button_text is gui_button_text

style debug_text is gui_text
style debug_label is gui_label
style debug_label_text is gui_label_text
style debug_button is gui_button
style debug_button_text is gui_button_text
style debug_radio_button is radio_button
style debug_radio_button_text is radio_button_text
style debug_check_button is check_button
style debug_check_button_text is check_button_text

style debug_menu_text:
    font debug_gui_font
style debug_menu_label_text:
    font debug_gui_font
style debug_menu_button_text:
    font debug_gui_font
style debug_menu_return_button_text:
    font debug_gui_font
style debug_menu_navigation_button_text:
    font debug_gui_font
style debug_text:
    font debug_gui_font
style debug_label_text:
    font debug_gui_font
style debug_button_text:
    font debug_gui_font
style debug_radio_button_text:
    font debug_gui_font
style debug_check_button_text:
    font debug_gui_font


screen debug_screen():

    tag menu

    use game_menu(_("Debug Mode"), scroll="viewport"):

        vbox:
            style_prefix "debug"
        
            textbutton _("Disable Debug Mode") action Show("debug_confirm", None, _("Disable debug mode?"), yes_action=[SetVariable("persistent.debug_mode", False), Hide()], no_action=Hide())
            textbutton _("Unlock All Music") action Call("debug_unlock", "Music")
            textbutton _("Unlock All CG") action Call("debug_unlock", "CG")
            textbutton _("Edit Variables...") action Show("per_variable")
            textbutton _("Clear Persistent Data") action Call("debug", "reset")
            if renpy.variant("pc"):
                textbutton _("Copy test file to Desktop") action Function(CopyToAnyway, "test/XS-X but delay event.zip", get_desktop_path() + "\\level file.zip")
            elif renpy.variant("android"):
                textbutton _("Copy test file to Download") action Function(release_file_quietly, "test/XS-X but delay event.zip", "Download/ACLCC Galgame", "level file.zip")


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


init python:
    def SetGameplayVariable(var, val):
        global variables
        variables[var] = val
    def SetPersistentVariable(var, val):
        global persistent
        persistent.variables[var] = val

screen variable():
    tag menu
    use debug_menu("Variable"):
        vbox:
            style_prefix "debug"
            for var, val in variables.items():
                hbox:
                    label "[var]"
                    text ": [val]"
                hbox:
                    textbutton "None" action Function(SetGameplayVariable, var, None)
                    textbutton "True" action Function(SetGameplayVariable, var, True)
                    textbutton "False" action Function(SetGameplayVariable, var, False)

screen per_variable():
    tag menu
    use debug_menu("Persistent Variable"):
        vbox:
            style_prefix "debug"
            for var, val in persistent.variables.items():
                hbox:
                    label "[var]"
                    text ": [val]"
                hbox:
                    textbutton "None" action Function(SetPersistentVariable, var, None)
                    textbutton "True" action Function(SetPersistentVariable, var, True)
                    textbutton "False" action Function(SetPersistentVariable, var, False)


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
