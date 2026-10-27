from Imports import cv2, SetupWindow

def SetupCamera():
    Cam = cv2.VideoCapture(0)
    Cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
    Cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    Cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
    print(Cam.get(cv2.CAP_PROP_FRAME_WIDTH), Cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    SetupWindow(Cam)
    return (Cam)