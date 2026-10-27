from Imports import StopChecks, Display

def MainLoop(cam, app):
    while True:
        ok, frame = cam.read()
        if not ok:
            break
        Display(app, frame)
        if StopChecks():
            break