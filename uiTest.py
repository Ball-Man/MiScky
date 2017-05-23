import UIController as uic
from UIController.modules import * 
import pygame
import time
import datetime as dt

import GoogleAPI.calendar as gcal

uic.init()

cmod = CalendarModule((500,500), (0,0), 5)
cmod.update(gcal.getEvents)
#cmod.events = (('fuffa', '14:00', '14:30', '10/11/2016'),('pippo', '18:00', '20:00', '10/11/2016'), ('roba', '16:00', '17:00', '12/11/2016'), ('altra robazza', '03:00', '04:00', '12/12/2016'))
uic.addModule(cmod)

weathermod = WeatherModule((300,300), (600,0), 5)
weathermod.temperature = 11
weathermod.meteo = 'Thunderstorm'
uic.addModule(weathermod)

clockmod = ClockModule((300,210), (0, 600), 1)
uic.addModule(clockmod)

emailmod = EmailModule((300,500), (600,400), 5)
now = dt.datetime.now()
emailmod.emails = [('Mario rossi', 'prova1', now), ('Luigi Verdi', 'prova2', now), ('Mario rossi', 'prova1', now), ('Mario rossi', 'prova1', now), ('Mario rossi', 'prova1', now)]  
uic.addModule(emailmod)

#id2 = uic.addModule('Meteo', (300,300), (11, 'Thunderstorm'), (700, 50))
#id3 = uic.addModule('Clock', (300,210), (), (800,800))

uic.refresh()

stop = False
while not stop:
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
			stop = True
			break
	time.sleep(0.1)

pygame.quit()
