from Imports import DrawFaces, cv2

def Display(App, Frame):
    DrawFaces(App, Frame)
    cv2.imshow("camera", Frame)