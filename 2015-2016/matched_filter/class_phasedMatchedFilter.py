class phasedMatchedFilter:
    def __init__(self):
        self.CoefficientsSource = 'Property'
        self.Coefficients = [1, 1]
        self.SpectrumWindow = 'None'
        self.CustomSpectrumWindow = 'hamming'
        self.SpectrumRange = [0, 1e5]
        self.SampleRate = 1e6
        self.SidelobeAttenuation = 30
        self.Beta = 0.5
        self.Nbar = 4
        self.GainOutputPort = 'false'

    def step(self):
        pass
    def autocorrelate(self):
        self.autocorr = numpy.correlate(x, x, mode='full')




