import weatherapi

weatherapi.init('Cesena')
print(weatherapi.todayWeather(), weatherapi.tomorrowWeather())