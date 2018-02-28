# from sklearn.externals import joblib
# clf = joblib.load('model.pkl')
# strs = raw_input('Init array number:')
# numbers = strs.split(' ')
# numbers = [int(x) for x in numbers]
# while (True):
#     dataTest = []
#     print numbers[:11]
#     dataTest.append(numbers[:11])
#     y_predicted = clf.predict(dataTest)
#     print y_predicted
#     _next = raw_input("Next number: ")
#     number_next = int(_next)
#     numbers.insert(0,number_next)

import pickle
def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

label_kind = load_obj('label_kind')
probably = load_obj('probably')

def calculate_probalbly(result, data, color):
    keys = []
    for i in range(0,len(data)):
        key = ''
        if data[i] ==0:
            key = 'g' + '|' + str(color) + '(' + str(i) + ')'
        if data[i]> 0 and data[i] <= 7:
            key = 'r' + '|' + str(color) + '(' + str(i) + ')'
        if data[i] > 7 and data[i] <= 14:
            key = 'b' + '|' + str(color) + '(' + str(i) + ')'
        keys.append(key)
data = [14, 13, 12]

