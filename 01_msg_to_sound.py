import numpy as np
from math import sin
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


morse = { 'A':'.-',
          'B':'-...',
          'C':'-.-.',
          'D':'-..',
          'E':'.',
          'F':'..-.',
          'G':'--.',
          'H':'....',
          'I':'..',
          'J':'.---',
          'K':'-.-',
          'L':'.-..',
          'M':'--',
          'N':'-.',
          'O':'---',
          'P':'.--.',
          'Q':'--.-',
          'R':'.-.',
          'S':'...',
          'T':'-',
          'U':'..-',
          'V':'...-',
          'W':'.--',
          'X':'-..-',
          'Y':'-.--',
          'Z':'--..',
          '0':'-----',
          '1':'.----',
          '2':'..---',
          '3':'...--',
          '4':'....-',
          '5':'.....',
          '6':'-....',
          '7':'--...',
          '8':'---..',
          '9':'----.'}

morse_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
morse_values = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
                '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']



# EDITABLE PARAMETERS
freq = 1760 # frequency of your morse code signal
sampleRate = 44100 # sample rate of your output sound file
pulseDur = 0.1 # length of each short pulse
filename = "02_sound.wav" # file to write morse code to


samplesPerPulse = int(pulseDur*sampleRate)


msg = input("what is your message: ")



transmittingString = ""

# representing morse code as 1 and 0 in transmitting string, to represent high and low signal respectively
# '.' becomes 1 | '-' becomes 111 | any spaces are 0
for char in msg.upper():
    if char == " ":
        transmittingString += "0000"
        continue
    for i in morse[char]:
        if i == ".": transmittingString += "10"
        elif i == "-": transmittingString += "1110"
    transmittingString = transmittingString.strip("0")
    transmittingString += "000"

transmittingString = transmittingString.strip("0")


# simple function to write samples to a wav file
def write_wav(samples):
    write(filename, sampleRate, samples.astype(np.int16))

# takes boolean parameter isHigh
# if isHigh is true, a short high audio pulse is created
# if isHigh is false, an empty array, or rather a low signal, is created
def createPulse(isHigh):
    if isHigh:
        res = []
        for i in range(samplesPerPulse):
            res.append(int(sin(i*2*np.pi*freq/sampleRate) * 2**16/2))
        return res
    else:
        return [0] * samplesPerPulse


# creating array of transmitted samples
transmitWav = []
for i in transmittingString:
    transmitWav += createPulse(int(i))

transmitWav = np.array(transmitWav)

write_wav(transmitWav)

# plots a graph of a small group of samples of the signal for analysis of waveform
# uncomment if not needed
plt.plot([x/44100 for x in range(len(transmitWav[0:300]))], [x/2 for x in transmitWav[0:300]])
plt.xlabel("time / s")
plt.ylabel("signal / arbitrary units")
plt.show()