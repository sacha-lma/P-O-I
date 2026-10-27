from Imports import SetupCamera, SetupDetector

def Setups():
    cam = SetupCamera()
    app = SetupDetector()
    return (cam, app)