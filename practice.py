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
# import requests
#
#
# def get_weather(api_key, location):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
#     response = requests.get(url)
#     data = response.json()
#
#     if data["cod"] == "404":
#         print("Invalid location. Please try again.")
#         return
#
#     city = data["name"]
#     temperature = data["main"]["temp"]
#     weather_desc = data["weather"][0]["description"]
#
#     print(f"Weather in {city}:")
#     print(f"Temperature: {temperature} K")
#     print(f"Description: {weather_desc}")
#
#
# # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
# api_key = 'YOUR_API_KEY'
# location = input("Enter a city name: ")
# get_weather(api_key, location)
#
# print("Kaun Banega Crorepati".center(50))
# questions = [
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
#         "Php", "None", 4
#     ],
#     [
#         "Which language was used to create fb?", "Python", "French", "JavaScript",
# #         "Php", "None", 4
# #     ],
# # ]
# #
# # levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# # money = 0
# # for i in range(0, len(questions)):
# #
# #     question = questions[i]
# #     print(f"\n\nQuestion for Rs. {levels[i]}")
# #     print(f"a. {question[1]}          b. {question[2]} ")
# #     print(f"c. {question[3]}          d. {question[4]} ")
# #     reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
# #     if (reply == 0):
# #         money = levels[i - 1]
# #         break
# #     if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")
# print(marks[4])
# subjects = ["English","Hindi","Maths","Science","Social Studies"]
# print(subjects)
# marks.extend(subjects)
# print(marks)

# List comprehension
# numbers = [a * a for a in range(5)]
# # print(numbers)
# l1 = [23,45,19,77,10,22]
# l1.sort()
# print(l1)
# print(max(l1))
# print(min(l1))
# print(l1)
list2 = [15,12,13,14,15]
# list2.reverse()
# print(list2)
# list2.sort( reverse = True )
# print(list2)
