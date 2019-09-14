import scipy.io
import numpy
import numpy.testing

import unittest


class MatchedFilter:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def step(self, x):
        return None

class MatchedFilterTest(unittest.TestCase):
    def test_matched_filter(self):
        in_data = scipy.io.loadmat("new.mat")

        x_data = in_data["x"]
        coeffs = in_data["coeffs"]

        y_data_matlab = in_data["y"]

        mega_matched_filter = MatchedFilter(coeffs)

        y_data_python = mega_matched_filter.step(x_data)

        print(y_data_python)
        print(y_data_matlab)

        numpy.testing.assert_allclose(y_data_python, y_data_matlab)

if __name__ == '__main__':
    unittest.main()