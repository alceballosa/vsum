import os
import pandas as pd
from torch.utils.data import Dataset
import skvideo.io
import numpy as np

class VideoDataset(Dataset):
  def __init__(self, annotations_file, video_dir):
    self.annotations = pd.read_csv(annotations_file)
    self.video_dir = video_dir
  
  def __len__(self):
    return len(self.video_dir)
  
  def __getitem__(self, idx):
    video_path = os.path.join(self.video_dir)
    annotation_row = self.annotations.iloc[idx]
    videodata = ""
    return_dict = {
      "video_data": videodata,
      "annotations": annotation_row["ANNOTATIONS"],
      "video_path": video_path
    }
    return return_dict 

dataset = VideoDataset(annotations_file="./tvsum50_ver_1_1/data/ydata-tvsum50-anno-cleaned.csv", video_dir="C:/Users/david/Documents/DAP/python_zoo/ai_stuff/video_summarization/Datasets/tvsum50_ver_1_1/videos/")
