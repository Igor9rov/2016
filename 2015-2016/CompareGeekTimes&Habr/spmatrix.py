import numpy as np
import scipy as sp

import scipy.sparse

# Матрица:
# 0 1 2
# 3 0 4
# 5 6 0

n_rows = 3
n_cols = 3

indices = [1, 2, 0, 2, 0, 1]  # Номера непустых элементов в каждой строчке матрицы.
data = [1, 2, 3, 4, 5, 6]  # Значения, которые вписаны в непустые элементы в каждой строчки матрицы.

ind_ptr = [0, 2, 4, 6]
# Для каждой i-й строчки матрицы ind_ptr[i] -- это сколько непустых элементов было _до_ этой строчки.
# ind_ptr[i + 1] -- сколько непустых элементов было _после_ этой строчки.

sparse_array = sp.sparse.csr_matrix((data, indices, ind_ptr), dtype=np.float64)

print(sparse_array.toarray())

g = [[2,3,6],[67,87,43]]
print(6 in g[0])