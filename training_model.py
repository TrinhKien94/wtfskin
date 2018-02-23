import csv


# Load data tu CSV file
def load_data(filename):
   lines = csv.reader(open(filename, "rb"), delimiter=',')
   dataset = list(lines)
   for i in range(len(dataset)):
       dataset[i] = [int(x) for x in dataset[i]]
   return dataset


def get_data_label(dataset):
    data = []
    label = []
    for x in dataset:
        data.append(x[1:])
        label.append(x[0])
    return data, label
trainingSet = load_data('training.csv')
dataTrain, labelTrain = get_data_label(trainingSet)
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(dataTrain, labelTrain)
from sklearn.externals import joblib
joblib.dump(clf, 'model.pkl', compress=9)
