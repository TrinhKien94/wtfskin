import csv
from collections import OrderedDict
import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

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
label_kind = {}
for label in labelTrain:
    if label not in label_kind:
        label_kind[label]=1
    else:
        label_kind[label]+=1
print label_kind
labels = label_kind.keys()
lenL = len(labelTrain)
probably = OrderedDict()
len_feat = len(dataTrain[0])
count = 0
count2 = 0
for i in range(0, lenL):
    key = 0
    if dataTrain[i][0] > 0 and dataTrain[i][0] <= 7:
        key = 1
    if dataTrain[i][0] > 7 and dataTrain[i][0] <= 14:
        key = 2
    if dataTrain[i][0] ==0:
        key = 0
    if dataTrain[i][len_feat-1] == 1 and key == labelTrain[i]:
        count += 1
    if dataTrain[i][len_feat-1] == 1:
        count2 += 1
print float(count)/count2

#     for j in range(0, len_feat):
#         key = ''
#         if(j != len_feat-1):
#             if dataTrain[i][j] > 0 and dataTrain[i][j] <= 7:
#                 key = 'r' + '|' + str(labelTrain[i]) + '(' + str(j) + ')'
#             if dataTrain[i][j] > 7 and dataTrain[i][j] <= 14:
#                 key = 'b' + '|' + str(labelTrain[i]) + '(' + str(j) + ')'
#             if dataTrain[i][j] ==0:
#                 key = 'g' + '|' + str(labelTrain[i]) + '(' + str(j) + ')'
#         else :
#             key = str(dataTrain[i][j]) + '|' + str(labelTrain[i]) + '(' + str(j) + ')'
#         if key in probably:
#             probably[key] += 1
#         else:
#             probably[key] = 1
# for key,value in probably.items():
#     print key + ' ' + str(float(value)/label_kind[labelTrain[i]])
# save_obj(probably,'probably')
# save_obj(label_kind,'label_kind')

# from sklearn.naive_bayes import MultinomialNB
# clf = MultinomialNB()
# clf.fit(dataTrain, labelTrain)
# from sklearn.externals import joblib
# joblib.dump(clf, 'model.pkl', compress=9)
