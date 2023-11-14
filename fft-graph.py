# plotting an audio file in both time-domain and frequency-domain
# oliver thurley, november 2023

# requires scipy, numpy, matplotlib libraried

# python v. 3.1.2


import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
from scipy.io import wavfile as wav
from scipy.fft import fft, fftfreq, rfft, rfftfreq
import numpy as np

###
### SET YOUR AUDIO FILE PATH HERE:
###
filename = 'path/to/audio-file.wav' #change this to your audio file

############

rate, wavData = wav.read(filename)
mono = wavData[:, 0] #only the data from channel 0, we only want one channel
fftClip = mono[0:int(rate/2)] # lets just fourier the first 0.5 seconds

duration = round(len(fftClip) / rate, 2) # convert samples to duration in secs

print("file = "+ str(filename))
print("duration = "+ str(duration) + " seconds")

yf = rfft(fftClip) # calculate the transform
xf = rfftfreq(len(fftClip), 1 / rate) # find frequency in center of each bin in fft?

### do the plotting
fig = plt.figure() #create figure
ax, figft, spect = fig.subplots(3)

 #figft.plot(freqs, np.abs(fourier))
figft.plot(xf, np.abs(yf), color="m")

formatFreqs = EngFormatter(unit='Hz')
figft.xaxis.set_major_formatter(formatFreqs)
figft.set_xlabel('frequency (Hz)')
figft.set_ylabel('magnitude')
figft.tick_params(left=False, bottom=False)
figft.set_yscale('linear')
figft.set_yticks([])

timeSeq = np.linspace(0, duration, len(fftClip))
ax.plot(timeSeq, fftClip, color="m")
ax.set_xlabel('time (s)')
ax.set_ylabel('amplitude')
ax.set_title(filename)
ax.set_yticks([])

"""mag.magnitude_spectrum(fftClip, Fs=rate, scale='dB', color="m")
mag.set_xlabel('time (s)')
mag.set_ylabel('amplitude')
mag.set_title(filename)
mag.set_yticks([])"""

spect.specgram(fftClip, NFFT=1024, Fs=rate) # NFFT= length of windowing segments
spect.set_xlabel('time (s)')
spect.set_ylabel('frequency')
spect.set_yticks([])

plt.show()
