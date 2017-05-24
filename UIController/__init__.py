#!/usr/bin/python

import pygame
import os.path
import time
import threading
import string

from .types import *
from .modules import *
from .renderer import *
from .colors import *

'''
import Xlib
Xlib.InitThreads()
'''

modules = None
stop_refreshing = False

def init():
	global screen
	global modules
	global stop_refreshing
	modules = []
	stop_refreshing = False
	pygame.display.init()
	pygame.font.init()
	screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

def startPrintTextDiffuse(*args, **kwargs):
	thread = threading.Thread(target=printTextDiffuse, args=args, kwargs=kwargs)
	thread.deamon = True
	thread.start()
	return thread

def printTextDiffuse(text, coordinates, timeDiffuse):
	assert(type(text) is Text)
	assert(type(coordinates) is tuple and len(coordinates) == 2 and all(map(lambda x: type(x) is int, coordinates)))
	assert(type(timeDiffuse) is int or type(timeDiffuse) is float)

	surface = text.render()
	background = pygame.Surface((surface.get_width(), surface.get_height()))
	background.fill((0,0,0))
	background = background.convert()
	background.blit(surface, (0,0))

	#surface = surface.convert()
	atomTime = timeDiffuse / 255
	
	for alpha in range(1, 256):
		background.set_alpha(alpha)
		screen.blit(background, coordinates)
		pygame.display.flip()
		time.sleep(atomTime)
	
def startPrintTextRunning(*args, **kwargs):
	thread = threading.Thread(target=printTextRunning, args=args, kwargs=kwargs)
	thread.deamon = True
	thread.start()
	return thread

def printTextRunning(text, coordinates, timeRunning): 
	assert(type(text) is Text)
	assert(type(coordinates) is tuple and len(coordinates) == 2 and all(map(lambda x: type(x) is int, coordinates)))
	assert(type(timeRunning) is int or type(timeRunning) is float)
		
	atomTime = timeRunning / len(text.text)
	tmpText = text.text
	text.text = ""
	for a in tmpText:
		text.text += a
		if a not in string.whitespace:
			surface = text.render()
			screen.blit(surface, coordinates)
			pygame.display.flip()
			surface.fill((0,0,0))
			screen.blit(surface, coordinates)
			time.sleep(atomTime)

def startAutoRefresh(seconds):
	global stop_refreshing
	async def autoRefresh(s):
		while not stop_refreshing:
			refresh()
			await asyncio.sleep(s)
		stop_refreshing = False
	autoRefresh()

def stopAutoRefresh():
	global stop_refreshing
	stop_refreshing = True

def addModule(module):
	global modules
	modules.append(module)

def removeModule(module):
	global modules
	modules.remove(module)

def refresh():
	screen.fill(BLACK)
	for mod in modules:
		mod.render(screen)
	pygame.display.flip()

def standby():
	screen.fill(BLACK)
	pygame.display.flip()