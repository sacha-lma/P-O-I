# EXTERNAL IMPORTS

import cv2
from insightface.app import FaceAnalysis
from dataclasses import dataclass

# DATACLASS DEFINITIONS

@dataclass
class FaceInfo:
    bbox: list
    age: int
    gender: int
    accuracy: float

# INTERNAL IMPORTS (order matters: each module must come after the ones it imports)

# SETUPS

from Setups.WindowSetup import SetupWindow
from Setups.CameraSetup import SetupCamera
from Setups.DetectorSetup import SetupDetector
from Setups.Setups import Setups

# CLEANUPS

from Cleanups.Cleanup import Cleanup

# CORE

# DISPLAY

from Core.Display.DrawFaces import DrawFaces

# ANALYSIS

from Core.Analysis.GetInfos import GetFaceInfos
from Core.Analysis.Loop import AnalysisLoop

# DISPLAY (after ANALYSIS: Display imports AnalysisLoop)

from Core.Display.Display import Display

# CHECKS

from Core.Checks.StopChecks import StopChecks

from Core.MainLoop import MainLoop