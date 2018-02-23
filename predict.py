from sklearn.externals import joblib
clf = joblib.load('model.pkl')
strs = raw_input('Init array number:')
numbers = strs.split(' ')
numbers = [int(x) for x in numbers]
while (True):
    dataTest = []
    print numbers[-11:]
    dataTest.append(numbers[-11:])
    y_predicted = clf.predict(dataTest)
    print y_predicted
    _next = raw_input("Next number: ")
    number_next = int(_next)
    numbers.append(number_next)
