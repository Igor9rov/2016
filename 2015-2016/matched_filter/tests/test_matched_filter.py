import unittest

import numpy
import scipy.io
import os
import matplotlib
import matplotlib.pyplot


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        print(os.path.abspath('../../mfilter.mat'))

        all_variables = scipy.io.loadmat('../../mfilter.mat')

        pyt = all_variables['w']
        print(type(pyt))
        print(pyt.shape)
        print(pyt)

        matplotlib.pyplot.plot(pyt.reshape((100,)))
        matplotlib.pyplot.show()




if __name__ == '__main__':
    unittest.main()