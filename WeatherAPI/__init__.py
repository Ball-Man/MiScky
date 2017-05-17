import pyowm
import datetime
NOW = datetime.datetime.now # Just for less writing

owm = None
forecaster = None
forecast = None
city = 'San Antonio'
last_update = datetime.datetime.fromtimestamp(0)

def init(place):
	global owm
	global city
	
	city = place
	owm = pyowm.OWM('6e0f2f6957e138ca701f81f69abba865', language='it')
	refresh()
	
def todayWeather():
	refresh()
	return forecast.get_weathers()[0]

def tomorrowWeather():
	refresh()
	return forecast.get_weathers()[1]

def refresh():
	global forecaster
	global forecast
	global last_update

	if (NOW() - last_update).total_seconds() > 3600: # If we updated more than 1 hour ago
		forecaster = owm.daily_forecast(city)
		forecast = forecaster.get_forecast()
		last_update = NOW()
