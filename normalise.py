import numpy as np


def normalise_point(x):
    '''
    We normalise each datapoint by dividing time by 2 (the number of
    minimum days that patients stayed in ICU).
    '''
    static, path = x

    path[:, 0] /= 2.

    return [static, path]

def normalise(X):
    '''
    Normalises the dataset.
    '''
    print("Normalising the data...")
    return list(map(normalise_point, X))
