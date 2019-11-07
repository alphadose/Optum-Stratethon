import urllib3
import pandas as pd
import numpy as np
import zipfile
from os import listdir
from os.path import isfile, join


def get_inputs():
    '''
    Downloads input data.
    '''

    print("Downloading input data from physionet.org...")
    url = "http://physionet.org/challenge/2012/set-a.zip"
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)

    with open('data/input.zip', 'wb') as out:
        while True:
            data = r.read()
            if not data:
                break
            out.write(data)

    r.release_conn()

    print("Extracting input data...")
    zip_ref = zipfile.ZipFile("data/input.zip", 'r')
    zip_ref.extractall("data/")
    zip_ref.close()

    data = {}
    list_files = [f for f in listdir("data/set-a") if isfile(join("data/set-a", f))]

    for f in list_files:
        df = pd.read_csv(join("data/set-a", f))
        patient_id = int(df.values[0, 2])
        data[patient_id] = df

    return data


def get_outputs():
    '''
    Downloads output data
    '''

    print("Downloading output data from physionet.org...")
    url = "https://physionet.org/challenge/2012/Outcomes-a.txt"
    data_df = pd.read_csv(url)

    print("Extracting output data...")
    data = {}

    for patient in data_df.values:
        patient_id = int(patient[0])
        data[patient_id] = patient[-1]

    return data

def download():
    X_dict, Y_dict = get_inputs(), get_outputs()

    X = []
    Y = []
    for patient_id in X_dict:
        X.append(X_dict[patient_id])
        Y.append(Y_dict[patient_id])

    print("Data for %s patients downloaded."%len(X))

    return X, Y
