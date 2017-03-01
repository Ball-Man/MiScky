#!/usr/bin/python

import pygame
import os.path
import time
import threading

import renderer

'''
import Xlib
Xlib.InitThreads()
'''

pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

def startPrintTextDiffuse(text, coordinates, timeDiffuse):
    thread = threading.Thread(target=printTextDiffuse, args=(text, coordinates, timeDiffuse))
    thread.deamon = True
    thread.start()
    return thread

def printTextDiffuse(text, coordinates, timeDiffuse):
    if type(text) is not pygame.Surface:
        raise TypeError("The text is not a pygame.Surface!")
    if type(coordinates) is not tuple:
        raise TypeError("The coordinates are not a tuple!")
    if len(coordinates) != 2:
        raise ValueError("The coordinates are not 2!")
    if type(timeDiffuse) is not int and type(timeDiffuse) is not float:
        raise TypeError("The timeDiffuse is not an integer or a float!")

    background = pygame.Surface((text.get_width(), text.get_height()))
    background.fill((0,0,0))
    background = background.convert()
    background.blit(text, (0,0))

    #text = text.convert()
    atomTime = timeDiffuse / 255
    
    for alpha in range(1, 256):
        background.set_alpha(alpha)
        screen.blit(background, coordinates)
        pygame.display.flip()
        time.sleep(atomTime)
    
def startPrintTextRunning(text, fontFile, size, timeRunning, coordinates, color = (255,255,255), antiAliasing = True):
    thread = threading.Thread(target=printTextRunning, args=(text, fontFile, size, timeRunning, coordinates, color, antiAliasing))
    thread.deamon = True
    thread.start()
    return thread

def printTextRunning(text, fontFile, size, timeRunning, coordinates, color = (255,255,255), antiAliasing = True):
    if type(text) is not str:
        raise TypeError("The text is not a string!")
    if type(coordinates) is not tuple:
        raise TypeError("The coordinates are not a tuple!")
    if len(coordinates) != 2:
        raise ValueError("The coordinates are not 2!")
    if type(timeRunning) is not int and type(timeRunning) is not float:
        raise TypeError("The timeRunning is not an integer or a float!")

    atomTime = timeRunning / len(text)
    textProg = ""
    for a in range(0, len(text)):
        textProg = textProg + text[a]
        surface = renderer.getTextSurface(textProg, fontFile, size, color, antiAliasing)
        screen.blit(surface, coordinates)
        pygame.display.flip()
        time.sleep(atomTime)





text1 = renderer.getTextSurface("Ciao", "Raleway/Raleway-Thin.ttf", 50)
text2 = renderer.getTextSurface("come stai?", "Raleway/Raleway-Thin.ttf", 50)

#screen.blit(text, (100,100))
#pygame.display.flip()

thread = startPrintTextDiffuse(text1, (100,100), 1)
thread.join()
thread = startPrintTextRunning("come stai?", "Raleway/Raleway-Thin.ttf", 50, 5, (200,200))
thread.join()

time.sleep(5)
pygame.quit()
