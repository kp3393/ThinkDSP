'''Exercise 5.1 The Jupyter notebook for this chapter, chap05.ipynb, includes
an interaction that lets you compute autocorrelations for different lags. Use
this interaction to estimate the pitch of the vocal chirp for a few different
start times.'''

from __future__ import print_function, division

import thinkdsp
import thinkplot
import thinkstats2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def serial_corr(wave, lag=1):
    N = len(wave)
    y1 = wave.ys[lag:]
    y2 = wave.ys[:N-lag]
    corr = np.corrcoef(y1, y2, ddof=0)[0, 1]
    return corr

def autocorr(wave):
    """Computes and plots the autocorrelation function.

    wave: Wave
    """
    lags = range(len(wave.ys)//2)
    corrs = [serial_corr(wave, lag) for lag in lags]
    return lags, corrs

wave = thinkdsp.read_wave('28042__bcjordan__voicedownbew.wav')
wave.normalize()
wave.make_audio()

spectrum = wave.make_spectrum()
# spectrum.plot()
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# plt.savefig('01_Spectrum.png')
# plt.show()
spectro = wave.make_spectrogram(seg_length = 1024)
# spectro.plot(high = 4200)
# plt.xlabel('Time (Sec)')
# plt.ylabel('Frequency (Hz)')
# plt.savefig('02_Spectrogram.png')
# plt.show()

duration = 0.01
segment = wave.segment(start = 0.4, duration = duration)
# segment.plot()
# plt.xlabel('Time (sec)')
# plt.ylabel('Amplitude')
# plt.savefig('03_Segment.png')
# plt.show()
spectrum = segment.make_spectrum()
# spectrum.plot(high = 800)
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# plt.savefig('04_Segment_Spectrum.png')
# plt.show()

lags, corrs = autocorr(segment)
# thinkplot.plot(lags, corrs)
# plt.xlabel('Lag(Index)')
# plt.ylabel('Correlation')
# plt.savefig('05_Segment_Autocorr.png')
# plt.show()

low,high = 100, 150
lag = np.array(corrs[low:high]).argmax()+low
print(lag)

frequency = (segment.framerate)/((lag))
print(frequency)
