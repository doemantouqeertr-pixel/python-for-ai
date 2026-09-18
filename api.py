

#------WEATHER DATA USING A FREE WEATHER API-----

import requests

# We need coordinates to get weather data
latitude = 33.60   # Rwp latitude
longitude = 73.06   # Rwp longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

# simply,
print(data)

# outcome in python dictionary form:
'''
{'latitude': 33.56766,
 'longitude': 73.048325, 
 'generationtime_ms': 0.02384185791015625, 
 'utc_offset_seconds': 0, 
 'timezone': 'GMT', 
 'timezone_abbreviation': 'GMT', 
 'elevation': 505.0, 
 'current_units': {'time': 'iso8601',
                   'interval': 'seconds',
                   'temperature_2m': '°C'}, 
 'current': {'time': '2026-09-18T13:00',
             'interval': 900, 
             'temperature_2m': 27.7}} '''

# actual temperature
temperature = data["current"]["temperature_2m"]

# Get the current temperature which is nested inside current,
print(data["current"]["temperature_2m"])

# we can also use the get() method to access the temperature
temperature = data.get("current", {}).get("temperature_2m")
print(temperature)

# or a printing statement to display the temperature
print(f"The current temperature of Rwp, is: {temperature}°C")




#------------------METHOD 2----------------------

import requests
def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data["current"]["temperature_2m"]

NYC_temp = get_weather(40.7 , -73.9)  
LOS_ANGELES_temp = get_weather(34.0522, -118.2437)  
CHICAGO_temp = get_weather(41.8781, -87.6298)  

print(f"The current temperature in NYC is: {NYC_temp}°C")
print(f"The current temperature in Los Angeles is: {LOS_ANGELES_temp}°C")
print(f"The current temperature in Chicago is: {CHICAGO_temp}°C")