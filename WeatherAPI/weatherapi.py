import pyowm

owm = None
forecaster = None
forecast = None
city = 'San Antonio'

def init(place):
	global owm
	global city
	
	city = place
	owm = pyowm.OWM('6e0f2f6957e138ca701f81f69abba865')
	refresh()
	
def todayWeather():
	return forecast.get_weathers()[0]

def tomorrowWeather():
	return forecast.get_weathers()[1]

def refresh():
	global forecaster
	global forecast
	
	forecaster = owm.daily_forecast(city)
	forecast = forecaster.get_forecast()