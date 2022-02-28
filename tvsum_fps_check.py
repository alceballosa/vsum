import pandas as pd
import cv2

def describe_video(path):
    cap = cv2.VideoCapture(path)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frameRate = int(cap.get(cv2.CAP_PROP_FPS))
    return frameRate, frameHeight, frameWidth, frameCount
    #print(f"Framerate: {frameRate}\nHeightxWidth: {frameHeight}x{frameWidth}\nN_frames: {frameCount}")

tvsum_anno = pd.read_csv("../Datasets/tvsum50_ver_1_1/ydata-tvsum50-v1_1/data/ydata-tvsum50-anno.tsv", sep="\t")
anno_1 = tvsum_anno.iloc[0, 2]
anno_1 = anno_1.split(",")
print(len(anno_1))

_,_,_, framecount = describe_video("../Datasets/tvsum50_ver_1_1/ydata-tvsum50-v1_1/ydata-tvsum50-video/video/AwmHb44_ouw.mp4")
print(framecount)