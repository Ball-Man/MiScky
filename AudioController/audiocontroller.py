from pygame import mixer

current = ''
paused = ''
paused_time = 0.0

def init():
	mixer.init()
	
def playAudio(path):
	global current
	
	if mixer.music.get_busy():
		return
	current = path
	mixer.music.load(path)
	mixer.music.play()
	
def stop():
	mixer.music.stop()
	
def playing():
	return mixer.music.get_busy()

def pauseNonPriority():
	global paused
	global paused_time
	
	paused_time = mixer.music.get_pos/1000
	paused = current
	mixer.music.fadeout(300)
	
def unpauseNonPriority():
	global paused
	global paused_time
	
	mixer.music.load(paused)
	mixer.music.set_volume(0.0)
	mixer.music.play(start=paused_time)
	
	tmp = 0.0
	while tmp < 1:
		tmp += 0.001
		mixer.music.set_volume(tmp)
	
	paused = ''
	paused_time = 0.0
	