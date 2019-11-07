from sklearn.ensemble import RandomForestClassifier

def train(features, Y):
    '''
    Trains a random forest classifier
    '''

    print("Training the model...")

    classifier = RandomForestClassifier()
    classifier.fit(features, Y)

    return classifier
