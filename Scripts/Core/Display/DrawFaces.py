from Imports import cv2

def DrawFaces(App, Frame):
    for Face in App.get(Frame):
        X1, Y1, X2, Y2 = Face.bbox.astype(int)
        cv2.rectangle(Frame, (X1, Y1), (X2, Y2), (0, 255, 0), 2)