import json
from pathlib import Path

import cv2
import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset
from torch.utils.data import random_split
from utils import helpers


def get_dataset():
    # ---------Paths-------- #
    path_root = helpers.get_project_root()
    ANNOTATIONS_FILE = path_root / "data/processed" / "ydata-tvsum50-anno-cleaned.csv"
    # TODO: replace by relative paths as per the script for downloading dataset
    FEATURES_DIR = Path(
        "/home/alberto/workspace/video-summarization/"
        + "datasets/tv-sum/extracted_features/i3d"
    )
    dataset = VideoDataset(annotations_file=ANNOTATIONS_FILE, features_dir=FEATURES_DIR)
    train_size = int(0.8 * len(dataset))
    test_size = len(dataset) - train_size
    train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
    return train_dataset, test_dataset


class VideoDataset(Dataset):
    def __init__(self, annotations_file: Path, features_dir: Path):
        self.annotations = pd.read_csv(annotations_file)
        self.features_dir = features_dir

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx: int) -> dict:
        path_features = self.features_dir
        annotation_row = self.annotations.iloc[idx]
        id_video = annotation_row["ID"]
        # annotations are saved as a string, turn them into a list of values
        annotations = annotation_row[" ANNOTATIONS"].replace("\n", "").split(",")
        annotations = np.array(list(map(int, annotations)))
        path_features = self.features_dir / (id_video + "_rgb.npy")
        X = np.load(path_features)
        # TODO: add path to actual videos for exploratory data analysis
        return_dict = {
            "X": torch.from_numpy(X),
            "y": torch.from_numpy(annotations),
            "features_path": str(path_features),
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
