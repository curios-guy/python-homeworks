import requests
import json

# important details
api_key = "ecf75ce803196f0d3322482cf531619c"
longtitude = 69.2
latitude = 41.3
base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longtitude}&appid={api_key}"
res = requests.get(base_url)

# saves the content in json file
with open("data.json", "w") as file:
    json.dump(res.json(), file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file)


# getting information in variables
min_temp = data['main']['temp_min']
max_temp = data['main']['temp_max']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
feels_like = data['main']['feels_like']
place_name = data['name']
country = data['sys']['country']

# prints out the output
if country == 'UZ':
    print("Welcome! About the weather in tashkent:")

print(f"\nYour location: {place_name}\nTemperature: {feels_like}\nMinimum temperature: {min_temp}\nMaximum temperature: {max_temp}\nHumidity: {humidity}\nPressure: {pressure}")