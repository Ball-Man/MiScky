import UIController as uic
import GoogleAPI.calendar as gcal
import pygame
import time

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
	position = (800,50)

	m1 = uic.addModule(moduleType, size, events, position)
	return m1

def main():
	uic.init()
	m1 = createCalendar()
	uic.refresh()
	waitForKey()

main()

'''
moduleType = 'Weather'
size = (300,300)
temperature = 9
weather = 'Snow'
events = (temperature, weather)
position = (50,500)

m2 = uic.addModule(moduleType, size, events, position)
'''
'''
moduleType = 'Clock'
size = (300,210)
events = ()
position = (50,50)

m3 = uic.addModule(moduleType, size, events, position)

uic.refresh()
'''
