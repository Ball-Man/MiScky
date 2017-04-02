import UIController as uic
from UIController.types import Text, Rectangle
import UIController.colors as colors
from UIController.modules import *
import pygame

import time

uic.init()

uic.screen.fill(colors.BLACK)
surf = CalendarModule((500,500), events=('fuffa','pippo')).render() 
uic.screen.blit(surf, (100, 100))
pygame.display.flip()

stop = False
while not stop:
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN:
			stop = True
			break
	time.sleep(0.1)
pygame.quit()
