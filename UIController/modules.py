from .types import *
from .colors import *

import math
import datetime as dt

class UIModule:
	_nextId = 0
	def __init__(self, size, position, updateSeconds, updateFunc):
		assert(type(size) is tuple and len(size) == 2 and all(map(lambda x: type(x) is int, size)))
		assert(type(position) is tuple and len(position) == 2 and all(map(lambda x: type(x) is int, position)))
		self.size = size
		self.position = position
		self.stop_updating = False
		self.updateSeconds = updateSeconds
		self.lastUpdate = dt.datetime.min
		self.updateFunc = updateFunc
		self.ID = UIModule._nextId
		UIModule._nextId += 1
	def render(self, screen):
		name = type(self).__name__
		text = Text('{} with id {}'.format(name, self.ID), 10, BLACK)
		back = Rect(self.size[0], self.size[1], WHITE)
		background = back.render()
		background.blit(text.render(), (0,0))
		screen.blit(background, self.position)
	def checkUpdate(self):
		now = dt.datetime.now()
		sec = (now - self.lastUpdate).total_seconds()
		res = False
		if sec >= self.updateSeconds:
			res = True
			self.lastUpdate = dt.datetime.now()
		return res
	def update(self, func):
		pass
	'''
	def startAutoUpdate(self, func, seconds):
		async def autoUpdate(foo, s):
			while not self.stop_updating:
				self.update(foo)
				await asyncio.sleep(s)
		self.stop_updating = False
		autoUpdate(func, seconds)
	def stopAutoUpdate(self):
		self.stop_updating = True
	'''
	def setSize(self, size):
		assert(type(size) is tuple and len(size) == 2 and all(map(lambda x: type(x) is int, size)))
		self.size = size
	def setPosition(self, position):
		assert(type(position) is tuple and len(position) == 2 and all(map(lambda x: type(x) is int, position)))
		self.position = position
class CalendarModule(UIModule):
	def __init__(self, size, position, updateSeconds, updateFunc):
		super().__init__(size, position, updateSeconds, updateFunc)
		self.events = []
	def update(self, func):
		if self.checkUpdate():
			evs = self.updateFunc()
			self.events = []
			for ev in evs:
				self.events.append(ev.toTuple())
	def render(self, screen):
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
				
		screen.blit(background, self.position)
class WeatherModule(UIModule):
	def __init__(self, size, position, updateSeconds, updateFunc):
		assert(type(size) is tuple and len(size) == 2 and size[0] == size[1])
		super().__init__(size, position, updateSeconds, updateFunc)
		self.temperature = None
		self.meteo = None
	def update(self):
		if self.checkUpdate():
			infos = self.updateFunc()
			t = infos.toTuple()
			self.temperature = t[0]
			self.meteo = t[1]
	def render(self, screen):
		size = self.size
		meteo = self.meteo
		
		fontFile = 'Digital/DS-DIGI.TTF'
		meteoFolder = 'Weather/light/png/'

		imageN = '25'
		if meteo == 'Clear':
			imageN = '36'
		elif meteo == 'Rain':
			imageN = '40'
		elif meteo == 'Atmosphere':
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

		screen.blit(background, self.position)
class ClockModule(UIModule):
	def __init__(self, size, position, updateSeconds):
		super().__init__(size, position, updateSeconds, 'No func!')
		self.points = True
	def update(self):
		if self.checkUpdate():
			self.points = not self.points
	def render(self, screen):
		size = self.size
		now = dt.datetime.now()
		s = ''
		if self.points:
			s = '%H:%M'
		else:
			s = '%H %M'
		firstText = now.strftime(s)
		secondText = now.strftime('%d %a %b %Y')
		scaleFactor = math.sqrt(size[0]*size[0] + size[1]*size[1])
		firstSize = int(scaleFactor // 3)
		secondSize = int(scaleFactor // 12.2)
		fontFile = 'Digital/DS-DIGI.TTF'
	
		hour = Text(firstText, firstSize, WHITE, fontFile).render()
		second = Text(secondText, secondSize, WHITE).render()
		
		background = Rectangle(size[0], size[1], BLACK).render()
		background.blit(hour, (0,0))
		background.blit(second, (0,size[1]/1.4))

		screen.blit(background, self.position)
class EmailModule(UIModule):
	def __init__(self, size, position, updateSeconds, updateFunc):
		super().__init__(size, position, updateSeconds, updateFunc)
		self.emails = []
	def update(self):
		if self.checkUpdate():
			ms = self.updateFunc()
			self.emails = []
			for m in ms:
				self.emails.append(m.toTuple())
	def render(self, screen):
		size = self.size
		emails = self.emails

		now = dt.datetime.now()

		headerH = size[1]//7
		headerPadding = size[1]//62.5
		headerTextSizeSmall = int(size[1]//38.46)
		headerTextSizeBig = int(size[1]//20)

		header = Rectangle(size[0], headerH, RED).render(0)
		pia = Text('Posta in arrivo', headerTextSizeBig, WHITE).render()
		header.blit(pia, (headerPadding, headerPadding))

		dateFont = 'Raleway/Raleway-SemiBold.ttf'
		dateTextSize = int(size[1]//38.46)
		dateTextPadding = int(size[0]//1.25)

		eventFont = 'Raleway/Raleway-SemiBold.ttf'
		eventTextSizeBig = int(size[1]//29.41)
		eventTextSizeSmall = int(size[1]//38.46)
		eventPadding = size[1]//50
		eventW = size[0]
		eventH = (size[1] - headerH)//5 - 1
		event = Rectangle(eventW, eventH, WHITE).render()
		events = []
		for m in self.emails:
			tmpEmail = event.copy()
			sender = Text(m[0], eventTextSizeBig, BLACK, eventFont).render()
			subject = Text('Oggetto: ' + m[1], eventTextSizeSmall, BLACK).render()
			if now.year == m[2].year and now.month == m[2].month and now.day == m[2].day:
				date = Text(m[2].strftime('%H:%M'), dateTextSize, BLUE, dateFont).render()
			else:
				date = Text(m[2].strftime('%d %b'), dateTextSize, BLUE, dateFont).render()
			subjectRect = subject.get_rect()
			subjectRect.bottomleft = (eventPadding, eventH - eventPadding)
			tmpEmail.blit(sender, (eventPadding, eventPadding))
			tmpEmail.blit(subject, subjectRect)
			tmpEmail.blit(date, (dateTextPadding, eventPadding))
			events.append(tmpEmail)

		eventMargin = 2
		background = Rectangle(size[0], size[1], GREY).render()
		background.blit(header, (0,0))
		for i in range(len(events)):
			ev = events[i]
			background.blit(ev, (0, headerH+i*(eventH+eventMargin)))

		screen.blit(background, self.position)
