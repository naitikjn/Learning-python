#Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# secret = (input("Enter Your Message:"))
# s = list(secret)
# print(s)
#
# print("Your Message Is Converted Into Secret Code")
#
# print("LOADING")
# if (len(secret)>=3):
#     secret.append(len(secret[0]))
#     secret.pop(0)
#     h= "hjv"
#     secret.append(h)
#     j = "woi"
#     secret.insert(j[0])
#     print(secret)
# else:
#     print(secret.reverse())
#
import requests


def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == "404":
        print("Invalid location. Please try again.")
        return

    city = data["name"]
    temperature = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature} K")
    print(f"Description: {weather_desc}")


# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
api_key = 'YOUR_API_KEY'
location = input("Enter a city name: ")
get_weather(api_key, location)
