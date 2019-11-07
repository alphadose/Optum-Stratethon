import numpy as np


def features_point(x):
    '''
    Extracts hand-crafted features from a datapoint.
    '''

    static, path = x
    maximums = np.max(path, axis=0)
    minimums = np.min(path, axis=0)
    last_observation = path[-1]

    return np.concatenate([static, maximums, minimums, last_observation])


def extract(X):
    '''
    Extracts hand-crafted features from a datapoint.
    '''

    print("Extracting features...")
    return list(map(features_point, X))
