# EXTERNAL IMPORTS

import cv2
from insightface.app import FaceAnalysis

# INTERNAL IMPORTS (order matters: each module must come after the ones it imports)

from Setups.WindowSetup import SetupWindow
from Setups.CameraSetup import SetupCamera
from Setups.DetectorSetup import SetupDetector
from Setups.Setups import Setups
from Cleanups.Cleanup import Cleanup