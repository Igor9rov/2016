import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import svm, datasets
i = 0
a = []
b = []
c = []
k = []
l = []
npb = np.array([])
npc = np.array([])
npk = np.array([])
realznach = np.array([])
infile = open('train.csv', 'r')
for row in csv.reader(infile, delimiter = ","):
    a = row
    i = i+1
    if i == 1:
        break
i=0
for row in csv.reader(infile, delimiter = ","):
    b = row
    b = b[1:]
    for j in range(0,784):
        b[j] = int(b[j])
    npb = np.append(npb, b)
    c = int(row[0])
    npc = np.append(npc,c)
    i = i+1
    if i == 1000:
        break
i=0
for row in csv.reader(infile, delimiter = ","):
    k = row
    k = k[1:]
    for j in range(0,784):
        k[j]=int(k[j])
    npk = np.append(npk, k)
    l = int(row[0])
    realznach = np.append(realznach,l)
    i = i+1
    if i == 1000:
        break
infile.close()

npb = npb.reshape(1000,784)
npk = npk.reshape(1000,784)

C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(npb, npc)
z = svc.predict(np.c_[npk])
np.testing.assert_array_almost_equal(z,realznach)


