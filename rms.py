import pyaudio
import numpy as np 
import wave
import struct
import time
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import cv2
import time 
matplotlib.use('TkAgg')
Chunk = 256

p = pyaudio.PyAudio()
wf = wave.open('song.wav','rb')

stream = p.open(
    format = p.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True)
tmpArray = np.empty([], np.int8)
print (tmpArray.shape)
data = wf.readframes(Chunk)
i = 0
tmpList = []
finalList = []

#---Graphics---#

fig, ax = plt.subplots()
ax.plot(2,10)
#--------------#
img = np.zeros([200,100,1])


while data != '':
	stream.write(data)
	data = wf.readframes(Chunk)
	#dataInt = np.array(struct.unpack(str(4 * Chunk) + 'B', data), dtype = 'b')[::2] + 128
	d = np.frombuffer(data, np.int16).astype(np.float)
	d = np.sqrt((d*d).sum()/len(d))
	d = int(d/100)
	img[0:d,:,0] = 1
	cv2.imshow('image',img)
	cv2.waitKey(2)
	img = np.zeros([200,100,1])
		
	if d > 140:
		print (d)