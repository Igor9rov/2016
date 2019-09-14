import csv
z = {3.0,4,5}
a = [str(int(item)) for item in z]
print(a[0])
print(a[1])
print(a)

writer = csv.writer(open('pr1.csv','w'),delimiter = ',',quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
for i in range(0,1):
    writer.writerow(['ImageId','Label'])
for i in range(1,9):
    writer.writerow([a[1],"Tek"])


