import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
print("WELCOME TO THE WEATHER APP!!!\n PRESS ENTER")
user = input()

CITY = input("Enter City name:\n")

API_KEY = "cf002751564a4c78f5f7ed479f1b9ba3"

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    main = data['main']

    temperature = main['temp']

    humidity = main['humidity']

    pressure = main['pressure']

    feelslike = main['feels_like']

    report = data['weather']

    print("CITY")
    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"feels like: {feelslike}")
    print(f"Weather Report: {report[0]['description']}")
else:
    print("Error in the HTTP request")
