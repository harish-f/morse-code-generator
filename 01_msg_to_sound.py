import wave
import numpy as np
from math import sin
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np


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


msg = input("what is your message: ")
filename = "02_sound.wav"

transmittingString = ""

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


# EDITABLE PARAMETERS
freq = 1760
sampleRate = 44100
pulseDur = 0.1

samplesPerPulse = int(pulseDur*sampleRate)


transmitWav = []


def write_wav(samples):
    write(filename, sampleRate, samples.astype(np.int16))

def createPulse(isHigh):
    if isHigh:
        res = []
        for i in range(samplesPerPulse):
            res.append(int(sin(i*2*np.pi*freq/sampleRate) * 2**16/2))
        return res
    else:
        return [0] * samplesPerPulse


for i in transmittingString:
    transmitWav += createPulse(int(i))

transmitWav = np.array(transmitWav)

plt.plot(transmitWav)
plt.show()


write_wav(transmitWav)