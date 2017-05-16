import audiocontroller
import mixer
import tts
import threading
import time

audiocontroller.init()

mixer.addToQueue('output.WAV')

mixer.playQueue()

time.sleep(0.5)
while audiocontroller.playing():
	print('Doing things')