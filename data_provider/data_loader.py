import os
import numpy as np
import pandas as pd
import os
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
from utils.timefeatures import time_features
import warnings

warnings.filterwarnings('ignore')

class Multi_Station_Dataset(Dataset):
    def __init__(self, root_path, flag='train', size=None, data_path='river_train.npy', freq='h'):
        # size = (seq_len, label_len, pred_len)
        self.seq_len = size[0]
        self.label_len = size[1]
        self.pred_len = size[2]
        # init
        self.flag = flag
        self.freq = freq

        self.root_path = root_path
        self.data_path = data_path
        self.__read_data__()

    def __read_data__(self):
        self.raw_data = np.load(os.path.join(self.root_path, self.flag + ".npy"), allow_pickle=True)
        self.raw_time = np.load(os.path.join(self.root_path, "data_time_" + self.flag + ".npy"), allow_pickle=True)
        raw_data = self.raw_data
        raw_time = self.raw_time
        print(self.raw_data.shape)
        print("==== " + self.flag + " data sorted load finished ====")

        data_len, station, feat = raw_data.shape
        raw_data = raw_data.reshape(data_len, station * feat) 
        data = raw_data.astype(np.float)

        df_stamp = raw_time
        df_stamp = pd.to_datetime(df_stamp)
        data_stamp = time_features(pd.to_datetime(df_stamp), freq=self.freq)
        data_stamp = data_stamp.transpose(1, 0)

        self.data_x = data
        self.data_y = data
        self.data_stamp = data_stamp

    def __getitem__(self, index):
        s_begin = index
        s_end = s_begin + self.seq_len
        r_begin = s_end - self.label_len
        r_end = r_begin + self.label_len + self.pred_len

        x = self.data_x[s_begin:s_end]
        y = self.data_y[r_begin:r_end]
        x_t = self.data_stamp[s_begin:s_end]
        y_t = self.data_stamp[r_begin:r_end]

        return x, y, x_t, y_t

    def __len__(self):
        return len(self.data_x) - self.seq_len - self.pred_len + 1

class Single_Station_Dataset(Dataset):
    def __init__(self, root_path, flag='train', size=None, data_path='river_train.npy', freq='h'):
        # size = (seq_len, label_len, pred_len)
        self.seq_len = size[0]
        self.label_len = size[1]
        self.pred_len = size[2]
        # init
        self.flag = flag
        self.freq = freq

        self.root_path = root_path
        self.data_path = data_path
        self.__read_data__()

    def __read_data__(self):
        self.raw_data = np.load(os.path.join(self.root_path, "river_" + self.flag + ".npy"), allow_pickle=True)  # (17519, 34040, 3)
        self.raw_time = np.load(os.path.join(self.root_path, "data_time_" + self.flag + ".npy"), allow_pickle=True)  # (17519)
        raw_data = self.raw_data
        raw_time = self.raw_time
        print(self.raw_data.shape)
        print("==== " + self.flag + " data sorted load finished ====")

        data_len, station, feat = raw_data.shape
        raw_data = raw_data.reshape(data_len, station * feat)  # (17519, 34040*3)
        data = raw_data.astype(np.float)

        df_stamp = raw_time
        df_stamp = pd.to_datetime(df_stamp)
        data_stamp = time_features(pd.to_datetime(df_stamp), freq=self.freq)
        data_stamp = data_stamp.transpose(1, 0)

        self.data_x = data
        self.data_y = data
        self.data_stamp = data_stamp

    def __getitem__(self, index):
        s_begin = index
        s_end = s_begin + self.seq_len
        r_begin = s_end - self.label_len
        r_end = r_begin + self.label_len + self.pred_len

        x = self.data_x[s_begin:s_end]
        y = self.data_y[r_begin:r_end]
        x_t = self.data_stamp[s_begin:s_end]
        y_t = self.data_stamp[r_begin:r_end]

        return x, y, x_t, y_t

    def __len__(self):
        return len(self.data_x) - self.seq_len - self.pred_len + 1