import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import svm, datasets
import pickle

def training():
    input = open('svctoallfile.pkl', 'rb')
    svc = pickle.load(input)
    input.close()
    return svc
def prediction():
    input = open('test.pkl', 'rb')
    npk = pickle.load(input)
    input.close()
    z = svc.predict(np.c_[npk])
    a = [str(int(item)) for item in z]
    return a
def writing():
    writer = csv.writer(open('predict.csv','w'),delimiter = ',',quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
    for i in range(0,1):
        writer.writerow(['ImageId',"Label"])
    for i in range(0,28000):
        writer.writerow([i+1,a[i]])

svc = training()
a = prediction()
writing()


