import UIController as uic
from UIController.modules import *
import GoogleAPI.calendar as gcal
import GoogleAPI.gmail as gmail
import WeatherAPI as wapi
import pygame
import time

SLEEP_TIME = 1
CITY = 'Cesena'

def checkKey():
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
			return True
	return False

def getModulePositions():
	pos = {'calendar': (500,600), 'email': (500,50), 'weather': (50,300), 'clock': (50,50)}
	return pos

def main():
	uic.init()
	wapi.init(CITY)

	modules = []

	# Modules creation
	pos = getModulePositions()
	modules.append(CalendarModule((500,500), pos['calendar'], 29, gcal.getEvents))
	uic.addModule(modules[-1])
	modules.append(EmailModule((500,500), pos['email'], 37, gmail.get_unread))
	uic.addModule(modules[-1])
	modules.append(WeatherModule((300,300), pos['weather'], 100, wapi.todayWeather))
	uic.addModule(modules[-1])
	modules.append(ClockModule((300,210), pos['clock'], 1))
	uic.addModule(modules[-1])

	while not checkKey():
		# Update all modules
		for m in modules:
			m.update()
		uic.refresh()
		time.sleep(SLEEP_TIME)

if __name__ == '__main__':
	main()