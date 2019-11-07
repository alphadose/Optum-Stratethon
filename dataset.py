import numpy as np


def split(X, Y, proportion=0.75):
    '''
    Splits dataset into a training and testing set
    '''

    print("Splitting the dataset...")
    idx = int(len(X)*proportion)
    print("Dataset split in a training set of %s and testing set of %s patients."%(idx, len(X)-idx))

    return X[:idx], Y[:idx], X[idx:], Y[idx:]
