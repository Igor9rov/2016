import numpy as np
import csv

i = 0
infile = open('test.csv', 'r')
for row in csv.reader(infile, delimiter = ","):
    i = i+1
print(i)
infile.close()