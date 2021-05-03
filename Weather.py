import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
print("WELCOME TO THE WEATHER APP!!!\n PRESS ENTER")
user = input()

CITY = input("Enter City name:\n")

# ZIPCODE = "30044"
# user = ZIPCODE
# LON = "33.7490"
# LAT = "84.3880"

API_KEY = "cf002751564a4c78f5f7ed479f1b9ba3"

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    main = data['main']

    temperature = main['temp']

    humidity = main['humidity']

    pressure = main['pressure']

    report = data['weather']

    # print("Enter City")
    print("CITY")
    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
"""
    elif user == 2:

        print("Enter Zipcode")
        user = input(ZIPCODE)
        print(user)
        print("ZIPCODE")
        print(f"{ZIPCODE:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")

    elif user == 3:
        print("Enter Longitude")
        user = input(LON)
        print("Enter Latitude")
        user = input(LAT)
        print(user)
        print("Longitude and Latitude")
        print(f"{LON:-^30}")
        print(f"{LAT:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
    elif user == 4:
        print("THANK YOU FOR USING THE WEATHER APP! \n GOODBYE")
    else:
        print("Error in the HTTP request")
"""
