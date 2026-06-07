init python:

    def custom_error_quit():
        renpy.game.QuitException(status=1)

    class CustomEditFile(Action):
        def __init__(self, filename, line=1):
            self.filename = filename
            self.line = line

        def __call__(self):
            try:
                if renpy.android:
                    try:
                        import jnius
                        activity = jnius.autoclass("org.renpy.android.PythonSDLActivity")
                        activity.mActivity.openEditor(renpy.exports.fsencode(self.filename))
                    except Exception:
                        traceback.print_exc()
                else:
                    renpy.launch_editor([ self.filename ], self.line, transient=1)
            except Exception:
                pass

    class CustomCopyFile(Action):
        def __init__(self, filename, template = u"{}"):
            self.filename = filename
            self.template = template

        def __call__(self):
            try:
                import renpy.pygame as pygame

                with open(self.filename, "rb") as f:
                    f.read(3) # skip the BOM.
                    s = self.template.format(f.read().decode("utf-8"))

                s = s.replace("\n", "\r\n")
                s = s.replace("\r\r", "\r")

                pygame.scrap.put(pygame.SCRAP_TEXT, s.encode("utf-8"))
            except Exception:
                pass


screen custom_exception(fmt_short, fmt_full=None, traceback_fn=None):
    # modal True
    layer "master"
    zorder 0

    frame:
        style_group ""

        has side "t c b":
            spacing gui._scale(10)

        side "c r":
            xfill True
            label "An exception has occurred." text_size gui._scale(40)
            text "{size=-3}[config.version!q]\n[renpy.version_only!q]\n[renpy.platform!q]{/size}":
                textalign 1.0 yalign 0.5

        viewport:
            id "viewport"
            child_size (None, None)
            mousewheel True
            draggable True
            scrollbars "both"

            has vbox

            text "[renpy.game.exception_info!q]" size gui._scale(22)
            frame style '_trace':
                text fmt_short substitute False safe True

            if fmt_full:
                text "Full traceback:" size gui._scale(22)
                frame style '_trace':
                    text fmt_full substitute False safe True

        hbox:
            vbox:
                hbox:
                    spacing gui._scale(25)
                    box_wrap True
                    box_wrap_spacing gui._scale(5)

                    textbutton "Rollback":
                        action Rollback()
                        tooltip "Attempts a roll back to a prior time, allowing you to save or choose a different choice."

                    textbutton "Ignore":
                        action Return()
                        if _ignore_action:
                            tooltip "Ignores the exception, allowing you to continue."
                        else:
                            tooltip "Ignores the exception, allowing you to continue. This often leads to additional errors."

                    if config.developer and not renpy.mobile:
                        if _errorhandling.reload:
                            textbutton "Reload":
                                action None
                                tooltip "Reloads the game from disk, saving and restoring game state if possible."

                        if _errorhandling.console:
                            textbutton "Console":
                                action None
                                tooltip "Opens a console to allow debugging the problem."
                    
                    if traceback_fn:
                        if not any([renpy.ios, renpy.emscripten]):
                            textbutton "Open":
                                action CustomEditFile(traceback_fn)
                                tooltip "Opens the traceback.txt file in a text editor."

                        textbutton "Copy BBCode":
                            action CustomCopyFile(traceback_fn, u"[code]\n{}[/code]\n")
                            tooltip "Copies the traceback.txt file to the clipboard as BBcode for forums like https://lemmasoft.renai.us/."

                        textbutton "Copy Markdown":
                            action CustomCopyFile(traceback_fn, u"```\n{}```\n")
                            tooltip "Copies the traceback.txt file to the clipboard as Markdown for Discord."

                $ tooltip = GetTooltip()
                
                text "[tooltip if tooltip else '']"

            vbox:
                xfill True

                textbutton "Quit":
                    xalign 1.0
                    action custom_error_quit()
                    tooltip "Quits the game."
