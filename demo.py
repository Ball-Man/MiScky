import UIController as uic
import GoogleAPI.calendar as gcal
import WeatherAPI as wapi
import pygame
import time
import zerorpc
from threading import Thread

def waitForKey():
	stop = False
	while not stop:
		for e in pygame.event.get():
			if e.type == pygame.KEYDOWN:
				stop = True
				break
		time.sleep(0.1)

	pygame.quit()

def createCalendar():
	events = gcal.getEvents(count=5)

	moduleType = 'Calendar'
	size = (500,700)
	events = [x.toTuple() for x in events]
	position = (500,50)

	m1 = uic.addModule(moduleType, size, events, position)
	return m1

def createWeather():
	moduleType = 'Weather'
	size = (300,300)
	today = wapi.todayWeather().toTuple()
	position = (50,500)

	m2 = uic.addModule(moduleType, size, today, position)
	return m2

def createClock():
	moduleType = 'Clock'
	size = (300,210)
	events = ()
	position = (50,50)

	m3 = uic.addModule(moduleType, size, events, position)
	return m3


class RPCListener(object):
	def refresh(self):
		uic.refresh()
	
def main():
	uic.init()
	wapi.init('Cesena')
	rpc = zerorpc.Server(RPCListener())
	rpc.bind('tcp://0.0.0.0:1080')
	
	thread = new Thread(target = rpc.run)
	thread.start()
	
	modulesID = []

	stop = False
	while not stop:
		for modID in modulesID:
			uic.removeModule(modID)
		
		modulesID = []

		m1 = createCalendar()
		modulesID.append(m1)
		m2 = createWeather()
		modulesID.append(m2)
		m3 = createClock()
		modulesID.append(m3)
		uic.refresh()
		
		for e in pygame.event.get():
			if e.type == pygame.KEYDOWN:
				stop = True
				break
		time.sleep(5)

	pygame.quit()

main()
