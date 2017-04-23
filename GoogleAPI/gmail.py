# -*- coding: utf-8 -*-

from . import *
import multiprocessing

API_NAME = 'gmail'
API_VERSION = 'v1'
base_service = None
user_id = 'me'

def _get_subj(email):
	return next(filter(lambda x: x['name'] == 'Subject', email['payload']['headers']))['value']

def get_email_data(email_id):
		email_fields = 'payload/headers'
		email_format = 'metadata'
		email = base_service.get(userId=user_id, id=email_id['id'], fields=email_fields, format=email_format).execute()
		return email


def get_unread(count : int):
	global base_service
	service = authorize(API_NAME, API_VERSION)
	base_service = service.users().messages()

	query = 'is:unread'
	email_ids = base_service.list(userId=user_id, q=query, maxResults=count).execute()['messages']

	emails = list(map(get_email_data, email_ids))
	subjects = list(map(_get_subj, emails))
	return subjects
