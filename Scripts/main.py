from Imports import cv2, FaceAnalysis, Setups, MainLoop, Cleanup

def Main():
    cam, app = Setups()
    MainLoop(cam, app)
    Cleanup(cam)

if __name__ == "__main__":
    Main()