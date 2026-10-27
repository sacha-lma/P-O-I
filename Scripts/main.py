from Imports import cv2, FaceAnalysis, Setups, MainLoop, Cleanup

def Main():
    Cam, App = Setups()
    MainLoop(Cam, App)
    Cleanup(Cam)

if __name__ == "__main__":
    Main()