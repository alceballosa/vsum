from pydoc import describe
import ffmpeg
import os
import json
import cv2
from pathlib import Path

def describe_video(path):
    cap = cv2.VideoCapture(path)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frameRate = int(cap.get(cv2.CAP_PROP_FPS))
    return frameRate, frameHeight, frameWidth, frameCount
    #print(f"Framerate: {frameRate}\nHeightxWidth: {frameHeight}x{frameWidth}\nN_frames: {frameCount}")
video_dir = Path("../../.", "data/raw")
savefile_dir = Path("../../references/")
video_data = []

for tvsum_path in list(video_dir.iterdir()):
  metadata = ffmpeg.probe(tvsum_path)["streams"][0]
  frameRate, frameHeight, frameWidth, frameCount = describe_video(str(tvsum_path))
  data_dict = {"name": tvsum_path.name, "frameRate": frameRate, "frameCount": frameCount, "frameHeight": frameHeight, "frameWidth": frameWidth, "duration": metadata["duration"]}
  video_data.append(data_dict)

with open("../../references/tvsum_metadata.json", "w") as f:
  json.dump(video_data, f, indent=4)



"""
summe_path = "../Datasets/SumMe/videos"
summe_mp4_paths = ["../Datasets/SumMe/videos/" + path for path in os.listdir(summe_path) if ".mp4" in path]
video_data = []
video_data_opencv = []
for summe_mp4_path in summe_mp4_paths:
  metadata = ffmpeg.probe(summe_mp4_path)["streams"][0]
  data_dict = {"name": summe_mp4_path[25:], "framerate": metadata["avg_frame_rate"], "duration": metadata["duration"]}
  video_data.append(data_dict)
  frameRate, frameHeight, frameWidth, frameCount = describe_video(summe_mp4_path)
  data_dict = {"name": summe_mp4_path[25:], "framerate": frameRate, "duration": 0}
  video_data_opencv.append(data_dict)


with open("../fps_duration_SumMe.json", "w") as f:
  json.dump(video_data, f, indent=4)
"""
