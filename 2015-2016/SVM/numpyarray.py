import numpy as np
b = np.array([[  0, 1, 2, 3],
              [10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33],
              [40, 41, 42, 43]])
b = np.append(b,45)
b = b.reshape(3,7)
print(b)