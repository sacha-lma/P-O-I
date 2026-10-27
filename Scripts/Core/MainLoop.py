from Imports import StopChecks, Display

def MainLoop(Cam, App):
    while True:
        Ok, Frame = Cam.read()
        if not Ok:
            break
        Display(App, Frame)
        if StopChecks():
            break