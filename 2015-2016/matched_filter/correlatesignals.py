import numpy
import scipy.io
import os
import matplotlib
import matplotlib.pyplot

all_variables = scipy.io.loadmat('../matchedfilter2.mat')
x = all_variables['x']
y = all_variables['Coeff']
res = all_variables['y']

print(type(x))
print(x.shape)
print(x)

print(type(y))
print(y.shape)
print(y)



x = x.reshape((200,))
y = y.reshape((100,))

Filter = numpy.convolve(x, y, mode = 'full')
Filter = Filter[numpy.nonzero(Filter != 0)]
matplotlib.pyplot.plot(Filter.real)
matplotlib.pyplot.plot(res.real)
matplotlib.pyplot.show()

