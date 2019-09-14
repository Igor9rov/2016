import numpy
import math
import matplotlib
import matplotlib.pyplot

Sig = numpy.array([])
for i in range(0, 10):

    Sig = numpy.append(Sig, i*i)
    i+1
Sig = Sig[::-1]
matplotlib.pyplot.plot(Sig.real)
matplotlib.pyplot.show()