import numpy as np                   # Essential scientific library.
from esig import tosig               # Computes signatures of streams of data.
from tqdm import tqdm                # To show load bars
from multiprocessing import Pool     # To allow multicore computation
from functools import partial        # To avoid lambda and allow pickleable functions
import pickle                        # Serialises Python objects
import os                            # OS tools

def st2si(order, stream):
    '''
    Computes the signature of a stream.

    Arguments:
        X (iterable): Iterable of numpy arrays.
        order (int): Order of the signature.
    '''
    if order > 1:
        return(tosig.stream2sig(stream , order))
    else:
        if order == 1:
            return np.concatenate((np.array([1]), stream[-1] - stream[0]), axis = 0)
        else:
            return np.array([1]);


def compute(X, order=2):
    '''
    Computes the signatures of a given dataset of streams of data.

    Arguments:
        X (iterable): Iterable of numpy arrays.
        order (int): Order of the signature.
    '''
    func = partial(st2si,order)
    pool = Pool()
    n_samples = len(X)
    signatures = []
    try:
        signatures = np.array(list(tqdm(pool.imap(func, X), total=n_samples)))
    except Exception as e:
        print('Failed to compute signatures: ' + repr(e))
        signatures = []
    return signatures
