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
		if audiocontroller.paused:
			audiocontroller.unpauseChannel()
		if not songs.empty() and not audiocontroller.playingChannel():
			current = songs.get()
			audiocontroller.playChannel(getRawFromFile(current))

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

#call ONCE to start queuing
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
	if audiocontroller.playingChannel():
		audiocontroller.pauseChannel()

def playPriority(path):
	audiocontroller.playOver(getRawFromFile(path))

def getRawFromFile(path):
	with open(path, 'rb') as f:
		return f.read()
	
	
