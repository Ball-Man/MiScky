from .types import *
from .colors import *

import datetime as dt

class UIModule:
	_nextId = 0
	def __init__(self, size):
		self.size = size
		self.modId = UIModule._nextId
		UIModule._nextId += 1
	def render(self):
		name = type(self).__name__
		text = Text('{} with id {}'.format(name, self.modId), 20, WHITE)
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
	def __init__(self, size, temperature, meteo):
		assert(type(size) is tuple and len(size) == 2 and size[0] == size[1])
		assert(type(temperature) is int)
		assert(type(meteo) is str)
		super().__init__(size)
		self.temperature = temperature
		self.meteo = meteo
	def render(self):
		size = self.size
		meteo = self.meteo
		
		meteoFolder = 'Weather/light/png/'

		imageN = '25'
		if meteo == 'sunny':
			imageN = '36'
		elif meteo == 'rainy':
			imageN = '40'
		elif meteo == 'foggy':
			imageN = '20'
		elif meteo == 'cloudy':
			imageN = '26'
		elif meteo == 'storm':
			imageN = '35'
		elif meteo == 'snowy':
			imageN = '14'
		elif meteo == 'halfSunny':
			imageN = '28'
		imageN += '.png'
		imagePath = meteoFolder + imageN

		tempSize = int(size[0]//6.25)
		meteoSize = int(size[0]//2.5)
		meteoX = size[0]//3.57
		meteoY = size[0]//10

		temp = str(self.temperature) + '°C'
		tempSurf = Text(temp, tempSize, METEO_BLUE).render()
		
		meteoSurf = Image((meteoSize,meteoSize), imagePath).render()

		background = Rectangle(size[0], size[1], BLACK).render()
		background.blit(meteoSurf, (meteoX, meteoY))
		background.blit(tempSurf, (0,0))

		return background
