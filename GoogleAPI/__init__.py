# -*- coding: utf-8 -*-

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

CLIENT_SECRET_FILE = 'client_secret.json'

def get_credentials():
	"""Gets valid user credentials from storage.

	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.

	Returns:
		Credentials, the obtained credential.
	"""
	home_dir = os.path.dirname(__file__)
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	credential_path = os.path.join(credential_dir, 'google_api.json')

	store = Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		credentials = None
	return credentials

def authorize(api_name : str, api_version : str):
	credentials = get_credentials()
	if credentials is None:
		return None
	http = credentials.authorize(httplib2.Http())
	service = discovery.build(api_name, api_version, http=http)
	return service
