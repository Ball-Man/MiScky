import GoogleAPI.calendar as cal
count = 5
events = cal.get_events(count=count)

print('Your next {} events are:'.format(count))
for e in events:
	print('\t' + str(e))
