import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft

def plot_sound_period(filename):
    sr, data = wavfile.read(filename)
    
    # using frames 150 to 300
    plt.plot([150/sr + x/sr for x in range(150,300)], data[150:300])
    plt.show()

def plot_sound_waveform(filename, start, end):
    # Read the audio file
    sr, data = wavfile.read(filename)
    
    
    data = data[int(start*44100):int(end*44100)]
    time = [x/sr for x in range(int(start*sr), int(start*sr) + len(data))]
    
    # Plot the waveform
    plt.plot(time, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Sound Waveform')
    plt.grid(True)
    plt.show()

def plot_fft(filename):
    # Read the audio file
    sample_rate, data = wavfile.read(filename)
    
    # Compute the FFT
    fft_output = fft(data)
    fft_magnitude = np.abs(fft_output)
    freqs = np.fft.fftfreq(len(data), 1/sample_rate)
    
    # Plot the FFT
    plt.figure(figsize=(12, 6))
    plt.plot(freqs[:len(data)//15], fft_magnitude[:len(data)//15])  # Plot only positive frequencies
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Fast Fourier Transform (FFT)')
    plt.grid(True)
    plt.show()

# Specify the filename of the sound file
filename = '06_received_sound.wav'  # Replace 'example.wav' with the filename of your sound file
# filename = '06_received_sound.wav'  # Replace 'example.wav' with the filename of your sound file

# Zoomed in plot of the frequency
plot_sound_period(filename)

# Plot the sound waveform
# Start and end of required waveform to be specified
plot_sound_waveform(filename, start=7.2, end=12.0)

# Plot the FFT graph
plot_fft(filename)