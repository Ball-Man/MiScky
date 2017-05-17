import UIController as uic
import pygame
import time

uic.init()

id1 = uic.addModule('Calendar', (500,500), (('fuffa', '14:00', '14:30', '10/11/2016'),('pippo', '18:00', '20:00', '10/11/2016'), ('roba', '16:00', '17:00', '12/11/2016'), ('altra robazza', '03:00', '04:00', '12/12/2016')), (0,0))
id2 = uic.addModule('Meteo', (200,200), (11, 'Thunderstorm'), (50, 50))
id3 = uic.addModule('Clock', (300,210), (), (800,800))

uic.refresh()

stop = False
while not stop:
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN:
			stop = True
			break
	time.sleep(0.1)

pygame.quit()
