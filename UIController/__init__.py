#!/usr/bin/python

import pygame
import os.path
import time
import threading
import string

from .types import *

'''
import Xlib
Xlib.InitThreads()
'''

def init():
    global screen
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

def startPrintTextDiffuse(*args, **kwargs):
    thread = threading.Thread(target=printTextDiffuse, args=args, kwargs=kwargs)
    thread.deamon = True
    thread.start()
    return thread

def printTextDiffuse(text, coordinates, timeDiffuse):
    if type(text) is not Text:
        raise TypeError("The text is not a Text!")
    if type(coordinates) is not tuple:
        raise TypeError("The coordinates are not a tuple!")
    if len(coordinates) != 2:
        raise ValueError("The coordinates are not 2!")
    if type(timeDiffuse) is not int and type(timeDiffuse) is not float:
        raise TypeError("The timeDiffuse is not an integer or a float!")

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

def printTextRunning(text, timeRunning, coordinates):
    if type(text) is not Text:
        raise TypeError("The text is not a Text!")
    if type(coordinates) is not tuple:
        raise TypeError("The coordinates are not a tuple!")
    if len(coordinates) != 2:
        raise ValueError("The coordinates are not 2!")
    if type(timeRunning) is not int and type(timeRunning) is not float:
        raise TypeError("The timeRunning is not an integer or a float!")

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
