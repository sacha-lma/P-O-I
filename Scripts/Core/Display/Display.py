from Imports import cv2, AnalysisLoop

def Display(App, Frame):
    AnalysisLoop(App, Frame)
    cv2.imshow("camera", Frame)