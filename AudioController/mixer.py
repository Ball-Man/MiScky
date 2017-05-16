import queue as qq
import audiocontroller
from pygame import mixer
from threading import Thread

songs = qq.Queue()
current = ''
started = False
queue = False

def loop():
	global current
	
	while queue:
		if not songs.empty() and not audiocontroller.playing():
			current = songs.get()
			audiocontroller.playAudio(current)

def addToQueue(path):
	global songs
	
	songs.put(path)

def resetQueue():
	global songs
	
	while not songs.empty():
		songs.get()

def popFromQueue():
	global songs
	
	songs.get()

#call ONCE to start queuing(Extremely blocking)
def playQueue():
	global started
	global queue
	
	queue = True
	if not started:
		thread = Thread(target = loop)
		thread.start()
	
def stopQueue():
	global queue
	
	queue = False
	if audiocontroller.playing():
		audiocontroller.stop()

#execute on secondary thread(Extremely blocking)		
def playWithPriority(path):
	global queue
	
	queue = False
	
	audiocontroller.pauseNonPriority()
	audiocontroller.playAudio(path)
	while audiocontroller.playing:
		pass
	audiocontroller.unpauseNonPriority()
	
	queue = True
	
	
	
	