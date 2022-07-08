import json
from pathlib import Path

import cv2
import pandas as pd
import torch
from torch.utils.data import Dataset
from torch.utils.data import random_split


def get_dataset():
    # ---------Paths-------- #
    ANNOTATIONS_FILE = Path(
        "../../.", "data/processed", "ydata-tvsum50-anno-cleaned.csv"
    )
    VIDEO_DIR = Path("../../.", "data/raw")

    # --------Metadata File--------- #
    # NOTE: If this fails, try generating the file by running python metadata_check.py
    with open("../../references/tvsum_metadata.json", "r") as f:
        metadata = json.load(f)
    dataset = VideoDataset(annotations_file=ANNOTATIONS_FILE, video_dir=VIDEO_DIR)
    train_size = int(0.8 * len(dataset))
    test_size = len(dataset) - train_size
    train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
    return train_dataset, test_dataset


class VideoDataset(Dataset):
    def __init__(self, annotations_file, video_dir):
        self.annotations = pd.read_csv(annotations_file)
        self.video_dir = Path(video_dir)

    def __len__(self):
        return len(self.video_dir)

    def __getitem__(self, idx):
        video_path = list(VIDEO_DIR.iterdir())[idx]
        annotation_row = self.annotations.iloc[idx]
        videodata = self.video_to_frames(video_path, idx)
        return_dict = {
            "video_data": videodata,
            "annotations": annotation_row[2],
            "video_path": str(video_path),
        }
        return return_dict

    def video_to_frames(self, video_path, idx):
        cap = cv2.VideoCapture(video_path)
        count = 0
        zero_tensor = torch.zeros(
            (cap.shape[0], cap.shape[1], cap.shape[2], metadata[idx]["frameCount"])
        )
        while True:
            ret, img = cap.read()
            img = torch.from_numpy(img)
            zero_tensor[:, :, :, count] = img
            count += 1
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            key = cv2.waitKey(1)
            if key == ord("q"):
                break


#
