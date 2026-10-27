from Imports import DrawFaces, cv2

def Display(app, frame):
    DrawFaces(app, frame)
    cv2.imshow("camera", frame)