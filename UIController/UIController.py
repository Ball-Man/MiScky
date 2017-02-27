#!/usr/bin/python

import pygame
import os.path
import time

import renderer

pygame.display.init()
pygame.font.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

text = renderer.getTextSurface("Ciao", "Raleway/Raleway-Thin.ttf", 50)

screen.blit(text, (100,100))

pygame.display.flip()
time.sleep(5)
pygame.quit()
