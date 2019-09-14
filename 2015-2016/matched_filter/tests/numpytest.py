import unittest
import numpy
import scipy.io
import os
import matplotlib
import matplotlib.pyplot
import math



class phasedLinearFMWaveform:
    def __init__(self, SampleRate, PulseWidth, PFR, SweepBandwidth):
        self.SampleRate = SampleRate
        self.PulseWidth = PulseWidth
        self.PFR = PFR
        self.SweepBandwidth = SweepBandwidth


    def step(self):
        T = []
        Sig = numpy.array([])
        A = self.SampleRate/self.PFR
        for i in range(0, int(A)):
            T.append(i / self.SampleRate)
            if T[i] <= self.PulseWidth :
                Sig = numpy.append(Sig, math.cos(math.pi * self.SweepBandwidth * (T[i] * T[i])/(self.PulseWidth))+1j*math.sin(math.pi * self.SweepBandwidth * (T[i] * T[i])/(self.PulseWidth)))
            else:
                Sig = numpy.append(Sig, 0)
            i+1
        return Sig


class phasedMatchedFilter:
    def __init__(self, Coeff):
        self.Coeff = Coeff

    def step(self, x):
        a = x.size
        filter = numpy.convolve(x, self.Coeff, mode = 'full')
        filter = numpy.resize(filter,(a,))
        return filter

all_variables = scipy.io.loadmat('../../matchedfilter2.mat')
x = all_variables['x']
Coeff = all_variables['Coeff']
y = all_variables['y']
PFR = 5e3
PulseWidth = 1e-4

x = x.reshape((200,))
Coeff = Coeff.reshape((100,))
y = y.reshape((200,))

WaveForm = phasedLinearFMWaveform(1e6, PulseWidth, PFR, 1e5)
Signal = WaveForm.step()
matplotlib.pyplot.plot(Signal.real)
matplotlib.pyplot.plot(x.real)


y = numpy.resize(y,(x.size,))
PF = phasedMatchedFilter(Coeff)
Fr = PF.step(x)
#matplotlib.pyplot.plot(Fr.real)
matplotlib.pyplot.show()

numpy.testing.assert_array_almost_equal(Fr,y)
numpy.testing.assert_array_almost_equal(Signal,x)