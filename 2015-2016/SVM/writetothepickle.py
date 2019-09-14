import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import svm, datasets
import pickle

def gettingsvm():
    i = 0
    npb = []
    npc = np.array([])
    infile = open('train.csv', 'r')
    for row in csv.reader(infile, delimiter = ","):
        i = i+1
        if i == 1:
            break
    i=0
    for row in csv.reader(infile, delimiter = ","):
        b = row
        b = b[1:]
        converted_array = np.asarray(b, dtype = np.int32)
        npb.append(converted_array)
        c = int(row[0])
        npc = np.append(npc,c)

    C = 1.0
    svc = svm.SVC(kernel='poly', degree=2, C=C).fit(npb, npc)
    return svc
svc = gettingsvm()

output = open('svctoallfile.pkl', 'wb')
pickle.dump(svc, output, 2)
output.close()