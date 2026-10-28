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

# INTERNAL IMPORTS (order matters: each module must come after the ones it imports)

from Setups.WindowSetup import SetupWindow
from Setups.CameraSetup import SetupCamera
from Setups.DetectorSetup import SetupDetector
from Setups.Setups import Setups
from Cleanups.Cleanup import Cleanup
from Core.Display.DrawFaces import DrawFaces
from Core.Display.Display import Display
from Core.Checks.StopChecks import StopChecks
from Core.MainLoop import MainLoop