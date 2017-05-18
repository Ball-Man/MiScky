import pyowm
import datetime
NOW = datetime.datetime.now # Just for less writing

owm = None
forecaster = None
forecast = None
city = 'San Antonio'
last_update = datetime.datetime.fromtimestamp(0)

class WeatherForecast:
	def __init__(self, temperature, status, description):
		self.temperature = temperature
		self.status = status
		self.description = description
	def toTuple(self):
		return str(self.temperature), self.status
	@staticmethod
	def fromAPI(apiobj):
		return WeatherForecast(apiobj.get_temperature(unit='celsius'), apiobj.get_status(), apiobj.get_detailed_status())

def init(place):
	global owm
	global city
	
	city = place
	owm = pyowm.OWM('6e0f2f6957e138ca701f81f69abba865', language='it')
	refresh()
	
def todayWeather():
	refresh()
	return WeatherForecast.fromAPI(forecast.get_weathers()[0])

def tomorrowWeather():
	refresh()
	return WeatherForecast.fromAPI(forecast.get_weathers()[1])

def refresh():
	global forecaster
	global forecast
	global last_update

	if (NOW() - last_update).total_seconds() > 3600: # If we updated more than 1 hour ago
		forecaster = owm.daily_forecast(city)
		forecast = forecaster.get_forecast()
		last_update = NOW()
