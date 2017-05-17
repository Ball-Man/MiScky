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

def init():
    global screen
    global modules
    modules = []
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

def addModule(moduleType, dimensions, events, position):
	mod = UIModule(dimensions)
	if moduleType == 'Calendar':
		mod = CalendarModule(dimensions, events)
	elif moduleType == 'Meteo':
		mod = MeteoModule(dimensions, events)
	elif moduleType == 'Mail':
		mod = MailModule(dimensions, events)
	elif moduleType == 'Clock':
		mod = ClockModule(dimensions, events)
	else:
		mod = UIModule(dimensions)
		
	modules.append((mod, position))
	return mod.ID

def removeModule(ID):
	modulesTmp = []
	for mod in modules:
		if mod[0].ID != ID:
			modulesTmp.append(mod)
	modules = modulesTmp

def refresh():
	screen.fill(BLACK)
	for mod in modules:
		screen.blit(mod[0].render(), mod[1])
	pygame.display.flip()

def standby():
	screen.fill(BLACK)
	pygame.display.flip()
