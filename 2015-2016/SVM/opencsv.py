infile = open('mytable.csv', 'r')
import csv
table = []
for row in csv.reader(infile, delimiter = "\t"):

    print (row)
infile.close()

