from Imports import cv2

def DrawBox(Frame, X1, Y1, X2, Y2):
    cv2.rectangle(Frame, (X1, Y1), (X2, Y2), (0, 255, 0), 2)

def DrawLabel(Frame, X1, Y1, X2, Label):
    Scale = max(0.4, (X2 - X1) / 150)
    cv2.putText(Frame, Label, (X1, Y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, Scale, (36, 255, 12), 2)

def DrawFaces(App, Frame):
    for Face in App.get(Frame):
            X1, Y1, X2, Y2 = Face.bbox.astype(int)
            DrawBox(Frame, X1, Y1, X2, Y2)
            DrawLabel(Frame, X1, Y1, X2, "Face Detected")