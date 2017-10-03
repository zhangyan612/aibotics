# OpenCV Track Object Movement
# computer vision

# import the necessary packages
from collections import deque
import numpy as np
import argparse
# import imutils
# import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
                help="max buffer size")
args = vars(ap.parse_args())
