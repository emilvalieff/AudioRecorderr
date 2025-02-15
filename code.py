# Getting started
# First import the required libraries

# import required libraries

import sounddevice as sd
from scipy.ip.wavfile import write
import wavio as wv

# Now, before starting the recorder. we have to devlare a few variables / The first one is the sampling frequency of the audio ( in most cases this will be 44100 or 48900 frames per second
# And the second is recording duration. We have to specfy the duration in seconds so that is stops recording after that duration 

# So let's declare them too.

# SAMPLING FREQUENCY.
freq = 44100

#Recording duration 
duration = 5


# Now we are done with recording the audio. So let's save it. To save the audo file. we can either use the scipy module or the wavio module
# USING SCIPY:

# This will conver the NumPy array to an audio
# file with given the sampling frequency
write("recording0.wav", freq, recording)

#Using wavio:
# WE can also use the write function from the wavio library
# Convert the NumPy array to audio file.
wv.write("MyRecord.wav",freq recording)

###########

import sounddevice as sd
from scipy.io wavfile import write
freq = 44100

duration = 5
recording = sd.rec(duration * freq), samplerate=freq, channels=1

sd.wait()

write("myRecord.wav", freq, recording)
