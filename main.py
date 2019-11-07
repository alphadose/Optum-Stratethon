import download
import reformat
import normalise
import features
import model
import performance
import dataset

if __name__ == "__main__":
    # We begin by downloading the data. The data will be in the form of
    # "events" data: each datapoint for each patient will be a recorded event.
    X, Y = download.download()

    # The event data is reformatted. This is done by selecting the given
    # variables and  transforming time-dependent events to a path.
    X = reformat.reformat(X, static_variables=["Age", "Gender"],
                          dynamic_variables=["Creatinine", "Glucose"])


    # Now, we normalise the data.
    X = normalise.normalise(X)

    # We extract features from the input data.
    features = features.extract(X)

    # The dataset is now split into a training and testing set.
    features_train, Y_train, features_test, Y_test = dataset.split(features, Y, proportion=0.75)

    # We now train the model with the selected features.
    classifier = model.train(features_train, Y_train)

    # We evaluate performance of the model now.
    performance.evaluate(classifier, features_test, Y_test)
