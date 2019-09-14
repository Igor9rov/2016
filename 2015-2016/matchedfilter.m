clear;
% 23

% Specify the waveform.
hwav = phased.LinearFMWaveform('PulseWidth',1e-4,'PRF',5e3,...
    'SampleRate',1e6,'OutputFormat','Pulses','NumPulses',1,...
    'SweepBandwidth',1e5);
w = getMatchedFilter(hwav);

% Create a matched filter with no spectrum weighting, and a
% matched filter that uses a Taylor window for spectrum
% weighting.
hmf = phased.MatchedFilter('Coefficients',w);
hmf_taylor = phased.MatchedFilter('Coefficients',w,...
    'SpectrumWindow','Taylor');

% Create the signal and add noise.
sig = step(hwav);
rng(17)
x = sig+0.5*(randn(length(sig),1)+1j*randn(length(sig),1));

% Filter the noisy signal separately with each of the filters.
y = step(hmf,x);
y_taylor = step(hmf_taylor,x);

% Plot the real parts of the waveform and noisy signal.
t = linspace(0,numel(sig)/hwav.SampleRate,...
    hwav.SampleRate/hwav.PRF);
subplot(2,1,1);
plot(t,real(sig)); title('Input Signal');
xlim([0 max(t)]); grid on
ylabel('Amplitude');
subplot(2,1,2);
plot(t,real(x)); title('Input Signal + Noise');
xlim([0 max(t)]); grid on
xlabel('Seconds'); ylabel('Amplitude');

% Plot the magnitudes of the two matched filter outputs.
% figure;
% plot(t,abs(y),'b--');
% title('Matched Filter Output');
% xlim([0 max(t)]); grid on
% hold on;
% plot(t,abs(y_taylor),'r-');
% ylabel('Magnitude'); xlabel('Seconds');
% legend('No Spectrum Weighting','Taylor Window');
% hold off;

