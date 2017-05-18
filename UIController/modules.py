from .types import *
from .colors import *

import math
import datetime as dt

class UIModule:
	_nextId = 0
	def __init__(self, size):
		self.size = size
		self.ID = UIModule._nextId
		UIModule._nextId += 1
	def render(self):
		name = type(self).__name__
		text = Text('{} with id {}'.format(name, self.ID), 20, WHITE)
class CalendarModule(UIModule):
	def __init__(self, size, events):
		super().__init__(size)
		self.events = events
	def render(self):
		size = self.size
		now = dt.datetime.now()

		headerH = size[1]//9
		headerPadding = size[1]//62.5
		headerTextSizeSmall = int(size[1]//38.46)
		headerTextSizeBig = int(size[1]//25)

		header = Rectangle(size[0], headerH, BLUE).render(0)
		todayWhite = Text(now.strftime('%a'), headerTextSizeSmall, WHITE).render()
		todayNumberAndMonth = Text(now.strftime('%d %B'), headerTextSizeBig, WHITE).render()
		header.blit(todayWhite, (headerPadding, headerPadding))
		header.blit(todayNumberAndMonth, (headerPadding, todayWhite.get_height()+headerPadding))

		dateNumberTextSize = headerTextSizeBig
		dateDayTextSize = headerTextSizeSmall
		dateNumberH = int(size[1]//25)

		eventFont = 'Raleway/Raleway-SemiBold.ttf'
		eventTextSizeBig = int(size[1]//29.41)
		eventTextSizeSmall = int(size[1]//38.46)
		eventPadding = size[1]//50
		eventW = size[0]*8//10
		eventH = size[1]//8
		event = Rectangle(eventW, eventH, LIGHT_BLUE).render()
		events = []
		datesNumber = []
		datesDays = []
		printdates = []
		lastDay = 0
		lastMonth = 0
		for ev in self.events:
			tmpEvent = event.copy()
			name = ev[0]
			start = ev[1]
			end = ev[2]
			dateKappa = ev[3].split('/')
			date = dt.datetime(int(dateKappa[2]), int(dateKappa[1]), int(dateKappa[0]), 0, 0, 0)
			
			printdate = 0

			if lastDay != date.day or lastMonth != date.month:
				lastDay = date.day
				lastMonth = date.month
				printdate = 1

			if printdate:
				datesNumber.append(Text(str(date.day), dateNumberTextSize, BLACK).render())
				datesDays.append(Text(date.strftime('%a'), dateDayTextSize, BLACK).render())
				printdates.append(1)
			else:
				datesNumber.append('empty')
				datesDays.append('empty')
				printdates.append(0)


			eventName = Text(name, eventTextSizeBig, WHITE, eventFont).render()
			eventTime = Text(start + '-' + end, eventTextSizeSmall, WHITE).render()
			eventTimeRect = eventTime.get_rect()
			eventTimeRect.bottomleft = (eventPadding, eventH - eventPadding)
			tmpEvent.blit(eventName, (eventPadding, eventPadding))
			tmpEvent.blit(eventTime, eventTimeRect)
			events.append(tmpEvent)

		eventIndent = size[0]//6.25
		eventMargin = size[1]//50
		background = Rectangle(size[0], size[1], WHITE).render()
		background.blit(header, (0,0))
		for i in range(len(events)):
			ev = events[i]
			background.blit(ev, (eventIndent, headerH+i*(eventH+eventMargin)+eventMargin))
			if printdates[i]:
				dateNumber = datesNumber[i]
				dateDay = datesDays[i]
				background.blit(dateNumber, (eventMargin, headerH+i*(eventH+eventMargin)+eventMargin))
				background.blit(dateDay, (eventMargin, headerH+i*(eventH+eventMargin)+eventMargin+dateNumberH))
				

		return background
class MeteoModule(UIModule):
	def __init__(self, size, events):
		assert(type(size) is tuple and len(size) == 2 and size[0] == size[1])
		assert(type(events[0]) is int)
		assert(type(events[1]) is str)
		super().__init__(size)
		self.temperature = events[0]
		self.meteo = events[1]
	def render(self):
		size = self.size
		meteo = self.meteo
		
		fontFile = 'Digital/DS-DIGI.TTF'
		meteoFolder = 'Weather/light/png/'

		imageN = '25'
		if meteo == 'Clear':
			imageN = '36'
		elif meteo == 'Rain':
			imageN = '40'
		elif meteo == 'Fog':
			imageN = '20'
		elif meteo == 'Clouds':
			imageN = '26'
		elif meteo == 'Thunderstorm':
			imageN = '35'
		elif meteo == 'Snow':
			imageN = '14'
		elif meteo == 'FewClouds':
			imageN = '28'
		imageN += '.png'
		imagePath = meteoFolder + imageN
		scaleFactor = math.sqrt(size[0]*size[0] + size[1]*size[1])
		tempSize = int(scaleFactor/3.5)
		meteoSize = int(scaleFactor/2)
		meteoX = int(float(size[0])/4)
		meteoY = int(float(size[1])/3.2)

		temp = str(self.temperature) + ' C'
		tempSurf = Text(temp, tempSize, METEO_BLUE, fontFile).render()
		
		meteoSurf = Image((meteoSize,meteoSize), imagePath).render()

		background = Rectangle(size[0], size[1], BLACK).render()
		background.blit(meteoSurf, (meteoX, meteoY))
		background.blit(tempSurf, (0,0))

		return background
class ClockModule(UIModule):
	def __init__(self, size):
		super().__init__(size)
	def render(self):
		size = self.size
		now = dt.datetime.now()
		firstText = now.strftime('%H:%M')
		secondText = now.strftime('%d %a %b %Y')
		scaleFactor = math.sqrt(size[0]*size[0] + size[1]*size[1])
		firstSize = int(scaleFactor // 2.44)
		secondSize = int(scaleFactor // 12.2)
		fontFile = 'Digital/DS-DIGI.TTF'
	
		hour = Text(firstText, firstSize, WHITE, fontFile).render()
		second = Text(secondText, secondSize, WHITE).render()
		
		background = Rectangle(size[0], size[1], BLACK).render()
		background.blit(hour, (0,0))
		background.blit(second, (0,size[1]/1.4))
		return background
