import os
import cv2
from scipy.io import loadmat

def get_fps(path):
  cap = cv2.VideoCapture(path)
  return int(cap.get(cv2.CAP_PROP_FPS))

def get_fcount(path):
  cap = cv2.VideoCapture(path)
  return int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

summe_anno_path = "../Datasets/SumMe/GT/"

annots = loadmat(summe_anno_path + "Air_Force_One.mat")
"""
KEYS:
all_userIDs
segments
nFrames
video_duration
FPS
gt_score
user_score
"""
print(annots["user_score"].shape)
print(get_fcount("../Datasets/SumMe/videos/Air_Force_One.mp4"))