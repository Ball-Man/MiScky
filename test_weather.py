import WeatherAPI

WeatherAPI.init('Cesena')
print(WeatherAPI.todayWeather().status, '\n', WeatherAPI.tomorrowWeather().description)
