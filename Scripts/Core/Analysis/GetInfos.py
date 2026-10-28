def GetFaceInfos(Face, FaceInfos):
    FaceInfos.bbox = Face.bbox.astype(int)
    FaceInfos.age = Face.age
    FaceInfos.gender = "Male" if Face.gender == 1 else "Female"
    return FaceInfos