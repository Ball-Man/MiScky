# -*- coding: utf-8 -*-

from . import *
import multiprocessing
import datetime

API_NAME = 'gmail'
API_VERSION = 'v1'
base_service = None
user_id = 'me'

class Email:
	def __init__(self, sentdate, subject, sender):
		self.sentdate = sentdate
		self.subject = subject
		self.sender = sender
	def __str__(self):
		return '[{}] ({}) from {}'.format(self.sentdate, self.subject, self.sender)
	def toTuple(self)
		return self.sender, self.subject, self.sentdate
	@staticmethod
	def from_api_dict(dictionary):
		sentdate = datetime.datetime.fromtimestamp(int(dictionary['internalDate'])//1000)
		headers = _get_headers(dictionary)
		return Email(sentdate, headers['Subject'], headers['From'])

def _get_headers(email):
	return {x['name'] : x['value'] for x in email['payload']['headers']}

def get_email_data(email_id):
		email_fields = 'payload/headers,internalDate'
		email_format = 'metadata'
		email = base_service.get(userId=user_id, id=email_id, fields=email_fields, format=email_format).execute()
		return email

def get_unread(count : int, query : str = 'is:unread'):
	global base_service
	service = authorize(API_NAME, API_VERSION)
	base_service = service.users().messages()

	email_ids = base_service.list(userId=user_id, q=query, maxResults=count).execute()
	email_ids = list(map(lambda x: x['id'], email_ids.get('messages', [])))

	emails = list(map(Email.from_api_dict, map(get_email_data, email_ids)))
	#subjects = list(map(_get_subj, emails))
	#return subjects
	return emails
