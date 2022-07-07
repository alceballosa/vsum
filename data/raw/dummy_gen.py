import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import random

from torch.utils.data import Dataset, DataLoader
import torch.nn.utils.rnn as rnn_utils

lstm = nn.LSTM(3, 3)
inputs = [torch.randn(1, 3) for _ in range(5)]

hidden = (torch.randn(1, 1, 3),
          torch.randn(1, 1, 3))

for i in inputs:
    out, hidden = lstm(i.view(1, 1, -1), hidden)

inputs = torch.cat(inputs).view(len(inputs), 1, -1)

hidden = (torch.randn(1, 1, 3), torch.randn(1, 1, 3))
out, hidden = lstm(inputs, hidden)
print(out)
print(hidden)


class DummyDataset(Dataset):
    def __init__(self, train_x):
        self.train_x = train_x

    def __len__(self):
        return len(self.train_x)

    def __getitem__(self, item):
        return self.train_x[item]


def collate_fn(train_data):
    train_data.sort(key=lambda data: len(data), reverse=True)
    data_length = [len(data) for data in train_data]
    train_data = rnn_utils.pad_sequence(
        train_data, batch_first=True, padding_value=0)
    return train_data, data_length


def generate_dummy_dataset(dataset_size):
    return [torch.randn(random.randint(20, 50), 1024) for _ in range(dataset_size)]


if __name__ == '__main__':
    dataset_size = 1000
    batch_size = 32
    train_data = generate_dummy_dataset(dataset_size)
    X_train = DummyDataset(train_x=train_data)
    train_dataloader = DataLoader(
        X_train, batch_size=batch_size, collate_fn=collate_fn)

    for data, length in train_dataloader:
        print(data.shape)
        # print(length)
