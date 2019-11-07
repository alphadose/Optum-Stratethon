import pandas as pd
import numpy as np
import urllib
from os import listdir
from os.path import isfile, join
import zipfile
import download
import copy

def to_path(df, dynamic_variables):
    '''
    Constructs a path from the given dynamic variables
    '''

    dim = len(dynamic_variables) + 1

    path = [[0.]*dim]

    for event in df.values:
        if event[1] in dynamic_variables:
            new_value = copy.deepcopy(path[-1])
            idx = 1 + dynamic_variables.index(event[1])
            new_value[idx] = event[2]

            hour, min = event[0].split(":")
            days = (float(hour) + float(min) / 60.)/24.

            new_value[0] = days

            path.append(new_value)

    path = np.array(path)
    # Now, for each time we only need one datapoint
    unique_times = np.unique(path[:, 0])
    idx = []
    for time in unique_times:
        last_idx = np.where(path[:, 0] == time)[0][-1]
        idx.append(last_idx)
    path = path[idx]

    return path

def static_features(df, static_variables):
    '''
    Retrieves the given static variables
    '''

    return df[df["Parameter"].isin(static_variables)]["Value"].values

def reformat(X, static_variables, dynamic_variables):
    '''
    Reformates a patient history
    '''

    print("Reformatting input data...")
    for i, x in enumerate(X):
        dynamic = to_path(x, dynamic_variables=dynamic_variables)
        static = static_features(x, static_variables=static_variables)
        X[i] = [static, dynamic]

    return X
