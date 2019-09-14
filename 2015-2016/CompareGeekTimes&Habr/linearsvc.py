import numpy as np
A = [{'jack': 4098, 'kek': 4139},
     {'jack': 46, 'spe': 49},
     {'jack': 40, 'stttape': 0},
     {'jyack': 8, 'stttape': 39}]

s = []
for i in A:

    for j in i:

        b = j in s
        if b == False:
            s.append(j)
            s.append(i[j])
            print(j)
            print(i[j])

print(s)

s = np.array(s)
print(s)
s = s.reshape((5,2))
print(s)
D = [{'jack': 4098, 'kek': 4139},
     {'jack': 46, 'spe': 49},
     {'jack': 40, 'stttape': 0},
     {'jyack': 8, 'stttape': 39}]

print(A+D)

