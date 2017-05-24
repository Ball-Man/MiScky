import pyowm
import datetime as dt
NOW = dt.datetime.now # Just for less writing

owm = None
forecaster = None
forecast = None
city = 'San Antonio'
last_update = dt.datetime.fromtimestamp(0)

class WeatherForecast:
	def __init__(self, temperature, status, description):
		self.temperature = temperature
		self.status = status
		self.description = description
	def toTuple(self):
		return self.temperature, self.status
	@staticmethod
	def fromAPI(apiobj):
		return WeatherForecast(int(apiobj.get_temperature(unit='celsius')['temp']), apiobj.get_status(), apiobj.get_detailed_status())

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
	tomorrow = dt.datetime.today() + dt.timedelta(days=1)
	return WeatherForecast.fromAPI(forecaster.get_weather_at(tomorrow))

def refresh():
	global forecaster
	global forecast
	global last_update

	if (NOW() - last_update).total_seconds() > 3600: # If we updated more than 1 hour ago
		forecaster = owm.three_hours_forecast(city)
		forecast = forecaster.get_forecast()
		last_update = NOW()
