import UIController as uic
from UIController.modules import * 
import pygame
import time
import datetime as dt

import GoogleAPI.calendar as gcal
import GoogleAPI.gmail as gmail
import WeatherAPI as wapi

uic.init()
wapi.init('Cesena')

modules = []

cmod = CalendarModule((500,500), (0,0), 50, gcal.getEvents)
cmod.update()
#cmod.events = (('fuffa', '14:00', '14:30', '10/11/2016'),('pippo', '18:00', '20:00', '10/11/2016'), ('roba', '16:00', '17:00', '12/11/2016'), ('altra robazza', '03:00', '04:00', '12/12/2016'))
uic.addModule(cmod)
modules.append(cmod)

weathermod = WeatherModule((300,300), (600,0), 50, wapi.todayWeather)
#weathermod.temperature = 11
#weathermod.meteo = 'Thunderstorm'
weathermod.update()
uic.addModule(weathermod)
modules.append(weathermod)

clockmod = ClockModule((300,210), (0, 600), 1)
clockmod.update()
uic.addModule(clockmod)
modules.append(clockmod)

emailmod = EmailModule((700,500), (600,400), 50, gmail.get_unread)
now = dt.datetime.now()
oneday = now - dt.timedelta(1)
#emailmod.emails = [('Mario rossi', 'prova1', now), ('Luigi Verdi', 'prova2', oneday), ('Mario rossi', 'prova1', oneday), ('Mario rossi', 'prova1', oneday), ('Mario rossi', 'prova1', oneday)]  
emailmod.update()
uic.addModule(emailmod)
modules.append(emailmod)

#id2 = uic.addModule('Meteo', (300,300), (11, 'Thunderstorm'), (700, 50))
#id3 = uic.addModule('Clock', (300,210), (), (800,800))

uic.refresh()

stop = False
while not stop:
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
			stop = True
			break
	time.sleep(1)
	for mod in modules:
		mod.update()
	uic.refresh()

pygame.quit()
