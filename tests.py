import datetime

import GoogleAPI.calendar as cal
count = 10
events = cal.get_events(count=count, timeMax = datetime.datetime(2017, 5, 30))

print('Your next {} events are:'.format(count))
for e in events:
	print('\t' + str(e))
