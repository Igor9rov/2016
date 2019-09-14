import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import svm, datasets
import pickle

def main():
    i = 0
    b = []
    c = []
    k = []
    l = []
    converted_array = ()
    npb = []
    npc = np.array([])
    npk = []
    realznach = np.array([])
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
        i = i+1
        if i == 33600:
            break
    i=0
    for row in csv.reader(infile, delimiter = ","):
        k = row
        k = k[1:]
        converted_array = np.asarray(k, dtype = np.int32)
        npk.append(converted_array)
        l = int(row[0])
        realznach = np.append(realznach,l)
        i = i+1
        if i == 8400:
            break
        print(i)
    infile.close()
    print(k[2])

    #npb = npb.reshape(3000,784)
    #npk = npk.reshape(1000,784)

    C = 1.0
    svc = svm.SVC(kernel='poly', degree=3, C=C).fit(npb, npc)
    z = svc.predict(np.c_[npk])
    np.testing.assert_array_almost_equal(z,realznach)

if __name__ == '__main__':
    main()


