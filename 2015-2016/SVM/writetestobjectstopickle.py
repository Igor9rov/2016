import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import svm, datasets
import pickle

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

infile = open('test.csv', 'r')
for row in csv.reader(infile, delimiter = ","):
        i = i+1
        if i == 1:
            break
i=0
for row in csv.reader(infile, delimiter = ","):
    a = row
    converted_array = np.asarray(a, dtype = np.int32)
    npk.append(converted_array)

output = open('test.pkl', 'wb')
pickle.dump(npk, output, 2)
output.close()
