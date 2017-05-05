import UIController as uic
from UIController.types import Text, Rectangle
import UIController.colors as colors
from UIController.modules import *
from UIController.renderer import *
import pygame

import time

uic.init()

uic.screen.fill(colors.BLACK)
surf = CalendarModule((500,500), events=(('fuffa', '14:00', '14:30', '10/11/2016'),('pippo', '18:00', '20:00', '10/11/2016'), ('roba', '16:00', '17:00', '12/11/2016'), ('altra robazza', '03:00', '04:00', '12/12/2016'))).render() 
meteo = MeteoModule((600,600), 11, 'sun').render()
uic.screen.blit(surf, (100, 100))
uic.screen.blit(meteo, (650,650))

pygame.display.flip()

stop = False
while not stop:
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN:
			stop = True
			break
	time.sleep(0.1)
pygame.quit()
