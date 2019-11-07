import numpy as np
from sklearn.metrics import roc_auc_score, confusion_matrix

def evaluate(classifier, features, Y):
    '''
    Evaluates the performance of the model
    '''

    print("Evaluating performance...")

    THRESHOLD = .3
    
    predictions_proba = classifier.predict_proba(features)[:, 1]
    predictions = [1. if pred>THRESHOLD else 0. for pred in predictions_proba]
    cm = confusion_matrix(Y, predictions)

    Se = cm[1, 1] / float(cm[1, 1] + cm[1, 0])
    P = cm[1, 1] / float(cm[1, 1] + cm[0, 1])
    score = min(Se, P)

    print("Score of predictions: %s"%score)
