import argparse
from pathlib import Path

import numpy as np
import torch
import wandb
from box import Box

# from tensorboardX import SummaryWriter
# from torch import nn
from torch.backends import cudnn

# from torch.nn import DataParallel
from torch.utils.data import DataLoader
from tqdm import tqdm

from data import tvsum_dataset
from utils import helpers



def train(cfg):
    cudnn.benchmark = True
    cudnn.enabled = True
    cfg = Box(helpers.parse_dict(cfg))

    if torch.cuda.is_available():
        device = torch.device(f"cuda:{cfg.TRAIN.gpu_id}")
        print(f"Using GPU {cfg.TRAIN.gpu_id}...")
    else:
        device = torch.device("cpu")
        print("Using CPU...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model for video summarization."
    )
    parser.add_argument(
        "--cfg", help="The config file with the required parameters.", type=Path
    )
    args = parser.parse_args()
    path_cfg = Path(args.cfg)
    cfg = helpers.read_config_file(path_cfg)._sections
    path_model_cfg = path_cfg.parent / f'{cfg["TRAIN"]["model_name"]}.cfg'
    cfg_model = helpers.read_config_file(path_model_cfg)._sections
    cfg.update(cfg_model)
    train(cfg)
