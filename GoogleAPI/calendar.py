# -*- coding: utf-8 -*-

from . import *
import datetime
import dateutil.parser

API_NAME = 'calendar'
API_VERSION = 'v3'

class Event:
	def __init__(self, startdate, starttime, endtime, summary):
		self.startdate = startdate
		self.starttime = starttime
		self.endtime = endtime
		self.summary = summary
	def __str__(self):
		return ' '.join(self.toTuple())
	def toTuple(self):
		return self.summary, self.starttime.strftime('%H:%M'), self.endtime.strftime('%H:%M'), self.startdate.strftime('%d/%m/%Y')
	@staticmethod
	def fromApiDict(dictionary):
		startdate_string = dictionary['start'].get('dateTime', dictionary['start'].get('date'))
		enddate_string = dictionary['end'].get('dateTime', dictionary['end'].get('date'))
		startdate = dateutil.parser.parse(startdate_string)
		enddate = dateutil.parser.parse(enddate_string)
		summary = dictionary.get('summary', '[No title]')
		return Event(startdate.date(), startdate.time(), enddate.time(), summary)

def getEvents(count : int = 10000, timeMax : datetime.datetime = datetime.datetime.utcnow()+datetime.timedelta(days=3650)):
	service = authorize(API_NAME, API_VERSION)
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	timeMax_string = timeMax.isoformat() + 'Z'
	eventsResult = service.events().list(calendarId='primary', timeMin=now, timeMax=timeMax_string, maxResults=count, singleEvents=True, orderBy='startTime').execute()
	events = eventsResult.get('items', [])
	return list(map(Event.fromApiDict, events))
