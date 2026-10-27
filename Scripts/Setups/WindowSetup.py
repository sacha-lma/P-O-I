from Imports import cv2

def SetupWindow(Cam):
    Width = int(Cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    Height = int(Cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.namedWindow("camera", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow("camera", Width, Height)