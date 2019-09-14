import unittest
import numpy
import scipy.io
import os
import matplotlib
import matplotlib.pyplot

all_variables = scipy.io.loadmat('../../matchedfilter2.mat')
x = all_variables['x']
Coeff = all_variables['Coeff']
y = all_variables['y']

x = x.reshape((200,))
Coeff = Coeff.reshape((100,))
y = y.reshape((200,))

class phasedMatchedFilter:
    def __init__(self):
        self.x = x
        self.Coeff = Coeff

    def GetMatchedFilter(self):
        filter = numpy.convolve(self.x, self.Coeff, mode = 'full')
        filter = filter[numpy.nonzero(filter != 0)]
        return filter

y = numpy.resize(y,(199,))
PF = phasedMatchedFilter()
Fr = PF.GetMatchedFilter()
matplotlib.pyplot.plot(Fr.real)
matplotlib.pyplot.show()

numpy.testing.assert_array_almost_equal(Fr,y)