from Imports import FaceAnalysis

def SetupDetector():
    App = FaceAnalysis(name="buffalo_l", allowed_modules=["detection"], providers=["CPUExecutionProvider"])
    App.prepare(ctx_id=-1, det_size=(640, 640))
    return (App)