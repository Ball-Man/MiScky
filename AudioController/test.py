import audiocontroller
import mixer
import tts
import threading
import time

audiocontroller.init()

mixer.addToQueue('prova1.WAV')
mixer.addToQueue('prova2.WAV')
mixer.playQueue()

while True:
	print('PLAYINNNNG')
