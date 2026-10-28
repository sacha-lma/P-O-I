from Imports import FaceInfo, DrawFaces, GetFaceInfos


def AnalysisLoop(App, Frame):
    FaceInfos = FaceInfo
    for Face in App.get(Frame):
        GetFaceInfos(Face, FaceInfos)
        DrawFaces(Frame, FaceInfos)