class phasedLinearFMWaveform:

    def __init__(self, SampleRate, PulseWidth, PRF, SweepBandwidth, NumSamples, NumPulses):
        self.SampleRate = SampleRate
        self.PulseWidth = PulseWidth
        self.PFR = PFR
        self.SweepBandwidth = SweepBandwidth
        self.NumPulses = NumPulses

    def step(self):
        T = []
        Sig = []
        for i in range(0, self.SampleRate * self.PFR/10, self.SampleRate)
            T.append(i)
            Sig.append(math.exp(j * math.pi * (self.SweepBandwidth / self.PulseWidth) * t * t))
            i+1
        return Sig


