import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import *

# plot a small sample of the audio file
def plot_sound_period(filename):
    sr, data = wavfile.read(filename)
    
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude / arbitrary units')
    plt.title('Sound Waveform')
    
    # using frames 150 to 300 to ignore any possible static at the start due to recording issues
    plt.plot([150/sr + x/sr for x in range(150,300)], data[150:300])
    plt.show()

# plot a specific portion of the file, with specified start and end timings
# used to decode the morse code based on high and low pulses
def plot_sound_envelope(filename, start, end):
    # Read the audio file
    sr, data = wavfile.read(filename)
    
    
    data = data[int(start*44100):int(end*44100)] # taking out specifically the samples of audio file that are required, based on start and end values
    time = [x/sr for x in range(int(start*sr), int(start*sr) + len(data))]
    
    plt.plot(time, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude / arbitrary units')
    plt.title('Sound Envelope')
    plt.grid(True)
    plt.show()


# plot the fft graph of the audio file
def plot_fft(filename):
    # Read the audio file
    sr, data = wavfile.read(filename)
    
    # Compute FFT
    fft_output = fft(data)
    fft_magnitude = np.abs(fft_output)
    freqs = fftfreq(len(fft_magnitude), 1/sr)
    
    # Plot the FFT graph
    plt.figure(figsize=(12, 6))
    plt.plot([x for x in freqs[:len(fft_magnitude)//15]], fft_magnitude[:len(fft_magnitude)//15])  # Plot only positive frequencies
    print(freqs)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude / arbitrary units')
    plt.title('Fast Fourier Transform (FFT)')
    plt.grid(True)
    plt.show()

# Comment out the unused file
# if analysing 02_sound.wav, comment out 'filename = '06_received_sound.wav'
filename = '02_sound.wav'
filename = '06_received_sound.wav'

# comment out functions if they aren't needed
plot_sound_period(filename) # plot a small group of samples, just to analyse the sine wave of the signal
plot_fft(filename) # plot the fft graph of the signal

# modify start and end values as needed
# Current values are for obtaining 1st word of our received file
plot_sound_envelope(filename, start=3, end=6.5) # plot the overall sound envelope, used to decode morse message
