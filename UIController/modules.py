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

		eventFont = 'Raleway/Raleway-SemiBold.ttf'
		eventTextSizeBig = int(size[1]//29.41)
		eventTextSizeSmall = int(size[1]//38.46)
		eventPadding = size[1]//50
		eventW = size[0]*8//10
		eventH = size[1]//8
		event = Rectangle(eventW, eventH, LIGHT_BLUE).render()
		events = []
		for ev in self.events:
			tmpEvent = event.copy()
			eventName = Text(ev, eventTextSizeBig, WHITE, eventFont).render()
			eventTime = Text('18:00-19:00', eventTextSizeSmall, WHITE).render()
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

		return background
class MeteoModule(UIModule):
	pass
