from Imports import cv2

def Cleanup(cam):
    cam.release()
    cv2.destroyAllWindows()