import pyowm

owm = pyowm.OWM('4c95726d2c1c8afdc31be707046ced59')  # You MUST provide a valid API key

# Will it be sunny tomorrow at this time in Milan (Italy) ?
#forecast = owm.daily_forecast("Milan,it")
#tomorrow = pyowm.timeutils.tomorrow()
#forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)


# Search for current weather in London (UK)
observation = owm.weather_at_place('Chattnooga,us')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}

humidity = w.get_humidity()              # 87
cTemp = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
fTemp = w.get_temperature('fahrenheit')

print "Relative Humidity is : %.2f %%" %humidity
print "Temperature in Celsius is : %.2f C" %cTemp
print "Temperature in Fahrenheit is : %.2f F" %fTemp

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)
