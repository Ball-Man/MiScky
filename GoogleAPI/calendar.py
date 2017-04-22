# -*- coding: utf-8 -*-

from . import *
import datetime
import dateutil.parser

API_NAME = 'calendar'
API_VERSION = 'v3'

class Event:
	def __init__(self, startdate, summary):
		self.startdate = startdate
		self.summary = summary
	def __str__(self):
		return '[{}] {}'.format(self.startdate, self.summary)
	@staticmethod
	def from_api_dict(dictionary):
		date_string = dictionary['start'].get('dateTime', dictionary['start'].get('date'))
		date = dateutil.parser.parse(date_string)
		summary = dictionary.get('summary', '[No title]')
		return Event(date, summary)

def get_events(count : int = 10000, timeMax : datetime.datetime = datetime.datetime.utcnow()+datetime.timedelta(days=3650)):
	service = authorize(API_NAME, API_VERSION)
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	timeMax_string = timeMax.isoformat() + 'Z'
	eventsResult = service.events().list(calendarId='primary', timeMin=now, timeMax=timeMax_string, maxResults=count, singleEvents=True, orderBy='startTime').execute()
	events = eventsResult.get('items', [])
	return list(map(Event.from_api_dict, events))
