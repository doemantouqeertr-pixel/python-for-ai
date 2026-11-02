
# UNDERSTANDING DATES AND TIMES IN PYTHON


from datetime import datetime,timedelta
today = datetime.now() 
#datetime represents a date/time
print(today) # 2026-09-21 18:49:29.023667


print(timedelta(days=7)) # 7 days, 0:00:00
week_ago = today - timedelta(days=7)
print(week_ago) #2026-09-14 18:49:29.023667
#timedelta represents a duration eg: 7 days, 0:00:00
print (today - timedelta(days=7))




# ---------------------------------------------------



start_date = week_ago.strftime("%Y-%d-%m")
print(start_date) # 2026-14-09
#or
start_date = week_ago.strftime("%Y-%m-%d")
print(start_date) # 2026-09-14
#or
start_date = week_ago.strftime("%m-%d-%Y")
print(start_date) # 09-14-2026
'''
we use strftime() bcz python datetime object might look 
like: 2026-09-14 15:36:42 but api wants 2026-09-14, so
strftime() means turn this datetime object into a string 
in the format we want.

'''


#---------------------------------------------------
# API → JSON → dictionary 

# API is a way for two applications to communicate with each other.
# JSON is a format for data exchange between applications.

# Is API work just extracting info from URLs?
''' Extracting data is only one of four main actions you can take. 
    Web APIs work using different HTTP methods to perform actions:
    1- GET (Fetch): Ask for data without changing anything
       (e.g., getting weather forecasts, reading profile info).
    2- POST (Create): Send new data to the server (e.g., posting
       a comment, uploading a photo, logging in).
    3- PUT / PATCH (Update): Modify existing data (e.g., changing 
       your status, updating your email).
    4- DELETE (Remove): Tell the server to delete something 
       (e.g., deleting a post or canceling a booking).
'''

latitude = 48.85
longitude = 2.35

url = f"https://api.open-meteo.com/...?latitude={latitude}&longitude={longitude}"

# How to know if a URL returns JSON
# 1- Paste the URL into your web browser: If the page
#    displays plain structured text wrapped in curly 
#    braces {} and quotes, it’s JSON
# 2- Check the API Documentation
# 3- Inspect the headers in Python by :
#    print(response.headers.get('Content-Type'))
#    If it contains 'application/json', it's JSON!

import requests

response = requests.get(url)
data = response.json()






















import csv
from datetime import datetime
import requests

# 1. Fetch the data (Replace with your actual API URL and Key)
# Using a placeholder weather API url for demonstration
API_URL = "https://weatherapi.com"
response = requests.get(API_URL)
weather_data = response.json()

# 2. Extract the exact data points you need (The "Working with Data" part)
# Note: Adjust these dictionary keys based on your specific weather API provider
city = weather_data["location"]["name"]
country = weather_data["location"]["country"]
temp_c = weather_data["current"]["temp_c"]
humidity = weather_data["current"]["humidity"]
condition = weather_data["current"]["condition"]["text"]
fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Arrange the extracted variables into a single row (list)
new_row = [fetched_at, city, country, temp_c, humidity, condition]

# 3. Save it to a .csv file
csv_filename = "weather_history.csv"
headers = [
    "Timestamp",
    "City",
    "Country",
    "Temperature (C)",
    "Humidity (%)",
    "Condition",
]

# We use 'a' (append mode) so it adds a new row every time you run the script
# instead of deleting your old weather data.
try:
    # Check if the file already exists to decide if we need headers
    with open(csv_filename, "r") as f:
        file_exists = True
except FileNotFoundError:
    file_exists = False

with open(csv_filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write headers only if creating the file for the very first time
    if not file_exists:
        writer.writerow(headers)

    # Append the new weather data row
    writer.writerow(new_row)

print(f"🎉 Success! Weather data appended to {csv_filename}")
