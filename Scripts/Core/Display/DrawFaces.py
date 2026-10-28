from Imports import cv2, FaceInfo

def DrawBox(Frame, FaceInfos):
    X1, Y1, X2, Y2 = FaceInfos.bbox
    cv2.rectangle(Frame, (X1, Y1), (X2, Y2), (0, 255, 0), 2)

def DrawLabel(Frame, FaceInfos):
    X1, Y1, X2, Y2 = FaceInfos.bbox
    Label = f"{FaceInfos.gender} : {FaceInfos.age}"
    Scale = max(0.4, (X2 - X1) / 150) / 2
    cv2.putText(Frame, Label, (X1, Y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, Scale, (36, 255, 12), 2)

def GetFaceInfos(Face, FaceInfos):
    FaceInfos.bbox = Face.bbox.astype(int)
    FaceInfos.age = Face.age
    FaceInfos.gender = "Male" if Face.gender == 1 else "Female"
    return FaceInfos

def DrawFaces(App, Frame):
    FaceInfos = FaceInfo
    for Face in App.get(Frame):
            GetFaceInfos(Face, FaceInfos)
            DrawBox(Frame, FaceInfos)
            DrawLabel(Frame, FaceInfos)