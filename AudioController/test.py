import audiocontroller
import mixer
import tts

audiocontroller.init()
mixer.addToQueue('output.mp3')
mixer.addToQueue('happy.mp3')
mixer.playQueue()

while audiocontroller.playing():
	print('Doing things')