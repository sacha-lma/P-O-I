from Imports import cv2

def DrawFaces(app, frame):
    for f in app.get(frame):
        x1, y1, x2, y2 = f.bbox.astype(int)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)