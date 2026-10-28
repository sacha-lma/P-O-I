from Imports import cv2, FaceInfo

def DefineBoxColor(FaceInfos):
    if FaceInfos.acuracy >= 0.9:
        return (0, 255, 0)
    elif FaceInfos.acuracy >= 0.7:
        return (0, 255, 255)
    else:
        return (0, 0, 255)

def DrawBox(Frame, FaceInfos):
    X1, Y1, X2, Y2 = FaceInfos.bbox
    cv2.rectangle(Frame, (X1, Y1), (X2, Y2), DefineBoxColor(FaceInfos), 2)

def DrawLabel(Frame, FaceInfos):
    X1, Y1, X2, _ = FaceInfos.bbox
    Label = f"{FaceInfos.gender} : {FaceInfos.age}"
    Scale = max(0.4, (X2 - X1) / 150) / 2
    cv2.putText(Frame, Label, (X1, Y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, Scale, (36, 255, 12), 2)

def DrawFaces(Frame, FaceInfos):
        DrawBox(Frame, FaceInfos)
        DrawLabel(Frame, FaceInfos)