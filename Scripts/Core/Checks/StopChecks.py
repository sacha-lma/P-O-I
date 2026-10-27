from Imports import cv2

def StopChecks():
    if cv2.waitKey(1) == ord("q") or cv2.getWindowProperty("camera", cv2.WND_PROP_VISIBLE) < 1:
        return (True)
    return (False)