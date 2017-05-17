import WeatherAPI

WeatherAPI.init('Cesena')
print(WeatherAPI.todayWeather().get_detailed_status(), '\n', WeatherAPI.tomorrowWeather().get_detailed_status())
