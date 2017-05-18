import datetime

import GoogleAPI.calendar as cal
count = 10
events = cal.getEvents(count=count, timeMax = datetime.datetime(2017, 5, 30))

print('Your next {} events are:'.format(count))
for e in events:
	print('\t' + str(e))

import GoogleAPI.gmail as gm
count = 5
mails = gm.get_unread(count=count, query='is:starred')

print('First {} unread/starred emails:'.format(count))
for m in mails:
	print(m)
