from pygame import mixer
import time

channel = None
paused = False 

stop_timer = 0.15

def init():
	global channel

	mixer.init(16000, -16, 1, 2048)
	channel = mixer.Channel(1)

def playChannel(raw):
	channel.set_volume(0)
	channel.play(mixer.Sound(raw))
	time.sleep(stop_timer)
	channel.set_volume(1)
	
def stopChannel():
	channel.stop()
	
def playingChannel():
	return channel.get_busy()

def stop():
	return mixer.stop()

def playing():
	return mixer.get_busy()

def pauseChannel():
	global paused

	paused = True
	channel.pause()

def unpauseChannel():
	global paused

	paused = False
	channel.unpause()

def setChannelVolume(volume):
	channel.set_volume(volume)

def getChannelVolume():
	return channel.get_volume()

def playOver(raw):
	sound = mixer.Sound(raw)
	sound.set_volume(0)
	sound.play()
	time.sleep(stop_timer)
	sound.set_volume(1)
