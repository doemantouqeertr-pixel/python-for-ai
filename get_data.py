






# --------------GET 7 DAYS OF WEATHER - REQUESTS----------

import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

# outcome:
'''
{'latitude': 48.84, 
 'longitude': 2.3599997, 
 'generationtime_ms': 0.04565715789794922, 
 'utc_offset_seconds': 0, 
 'timezone': 'GMT', 
 'timezone_abbreviation': 'GMT', 
 'elevation': 46.0, 
 'daily_units': {'time': 'iso8601',
                 'temperature_2m_max': '°C', 
                 'temperature_2m_min': '°C'},
 'daily': {'time': ['2026-09-12',
                    '2026-09-13', 
                    '2026-09-14', 
                    '2026-09-15', 
                    '2026-09-16', 
                    '2026-09-17', 
                    '2026-09-18', 
                    '2026-09-19'], 
           'temperature_2m_max': [25.7,
                                  27.1,
                                  28.9, 
                                  32.8, 
                                  22.0, 
                                  21.9, 
                                  21.8, 
                                  24.4], 
           'temperature_2m_min': [15.2, 
                                  17.5, 
                                  18.2, 
                                  17.9, 
                                  14.8, 
                                  13.8, 
                                  13.0, 
                                  14.0]

            }

}
'''











# --------------------Load into pandas-----------------

import pandas as pd

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)



# outcome:
'''
  date          max_temp  min_temp
0 2026-09-12      25.7      15.2
1 2026-09-13      27.1      17.5
2 2026-09-14      28.9      18.2
3 2026-09-15      32.8      17.9
4 2026-09-16      22.0      14.8
5 2026-09-17      21.9      13.8
6 2026-09-18      21.8      13.0
7 2026-09-19      24.4      14.0
'''










#-----------------Visualize the data--------------------
import matplotlib.pyplot as plt

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('PARIS Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()























# Save the plot
plt.savefig('weather_chart.png')
plt.show()

# create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# save to CSV
df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")





#      PRACTICAL PYTHON 
'''
Building real programs with proper structure
> Set up a project - Create organized folder structure
> Understand paths - Learn how Python finds you files
> Work with data - Read CSV files and save as JSON
> Organize code - Split code into reusable fuctions

'''



