import WeatherAPI as wapi

wapi.init('Cesena')
td = wapi.todayWeather()
tm = wapi.tomorrowWeather()

print(td.toTuple())
print(tm.toTuple())
