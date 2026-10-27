from Imports import cv2

def Cleanup(Cam):
    Cam.release()
    cv2.destroyAllWindows()