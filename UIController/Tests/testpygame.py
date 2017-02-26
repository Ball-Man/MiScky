#!/usr/bin/python
import pygame
import os.path
import time

pygame.display.init()
pygame.font.init()

fontfile = os.path.dirname(os.path.realpath(__file__)) + "/Fonts/Raleway/Raleway-Thin.ttf"
imagefile = os.path.dirname(os.path.realpath(__file__)) + "/Images/image.gif"


size = (1080,1920)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

fontSize = 50

sti = pygame.Surface((600, 600))

font = pygame.font.Font(fontfile, fontSize)
image = pygame.image.load(imagefile)
image = pygame.transform.scale(image, (100,200))



text1 = font.render(str(screen.get_size()), 1, (255,255,255))
text2 = font.render('Ciao a tutti', 0, (255,255,255))

sti.blit(text1, (0,0))
sti.blit(image, (100,100))


'''
screen.blit(text1, (960-text1.get_width()/2,540-text1.get_height()/2-150))
screen.blit(text2, (0,0))
screen.blit(image, (0,0))
'''


screen.blit(sti, (400,400))

pygame.display.flip()

time.sleep(5)
pygame.quit()
