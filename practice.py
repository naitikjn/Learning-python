# # # else_if_elif
# # # var1 = 8
# # # var2 = 45
# # #
# # # var3 = int(input())
# # # if var3>var2:
# # #     print("greater")
# # #
# # # elif var3==var2:
# # #     print("equal")
# # #
# # # else:
# # #    print("lesser")
# # # #sets
# # # sst = (1,2,3,4)
# # # print(s_from_ = set()
# # # print(type(s))
# # # s_from_lilist)
# # # print(type(s_from_list))
# # # l = [1,3,5,7,9]
# # # s = set(l)
# # # print(s)
# # # s.add(8)
# # # s.add(5)
# # # print(s)
# # # s.remove(8)
# # # print(s)
# # #
# # # #types python
# # # print(str(var1) + str(var2))
# # # print(100* "hello world \n")
# # # print("enter your number")
# # # abcd = input()
# # #
# # # print("you entered", int(abcd) + 1)
# # #
# # # import sys
# # # print( sys.path)
# # #
# # # # There are two methods to use functions or variables after importing:
# # # # The first one is to import using an object. For this, we usually import the whole module by using a simple import statement. When we use only the import keyword, we will import the resource directly, like this:
# # # # import sklearn
# # # # When we use the second syntax, we will import the resource from another package or module. Here is an example:
# # # # from flask import Flask
# # # # We can also choose to rename an imported resource, like this:
# # # # import pandas as pd
# # # from sklearn.ensemble import RandomForestClassifier
# # #
# # # print(RandomForestClassifier())
# # #
# # # import file2
# # #
# # # print(file2.a)
# # #
# # # file2.printjoke("This is me")
# # # a = 7
# # #
# # #
# # # def printjoke(str):
# # # #     print(f"this function is a joke {str}")
# # #
# # #
# # # import if__name
# # # print(if__name.add (15,25))
# # import random  # For generating random numbers
# # import sys  # To exit the program
# # import pygame  # pip install pygame
# # from pygame.locals import *
# #
# # # Global Variables for the game
# # FPS = 32
# # SCREENWIDTH = 289
# # SCREENHEIGHT = 511
# # SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
# # GROUNDY = SCREENHEIGHT * 0.8
# # GAME_SPRITES = {}
# # GAME_SOUNDS = {}
# # PLAYER = 'gallery/sprites/bird.png'
# # BACKGROUND = 'gallery/sprites/background.png'
# # PIPE = 'gallery/sprites/pipe.png'
# #
# #
# # def welcomeScreen():
# #     playerx = int(SCREENWIDTH / 5)
# #     playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
# #     messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
# #     messagey = int(SCREENHEIGHT * 0.13)
# #     basex = 0
# #     while True:
# #         for event in pygame.event.get():
# #             # if user clicks on cross button, close the game
# #             if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
# #                 pygame.quit()
# #                 sys.exit()
# #
# #             # If the user presses space or up key, start the game for them
# #             elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
# #                 return
# #             else:
# #                 SCREEN.blit(GAME_SPRITES['background'], (0, 0))
# #                 SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
# #                 SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
# #                 SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
# #                 pygame.display.update()
# #                 FPSCLOCK.tick(FPS)
# #
# #
# # def mainGame():
# #     score = 0
# #     playerx = int(SCREENWIDTH / 5)
# #     playery = int(SCREENWIDTH / 2)
# #     basex = 0
# #
# #     # Create 2 pipes for blitting on the screen
# #     newPipe1 = getRandomPipe()
# #     newPipe2 = getRandomPipe()
# #
# #     # List of upper pipes
# #     upperPipes = [
# #         {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
# #         {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
# #     ]
# #     # List of lower pipes
# #     lowerPipes = [
# #         {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
# #         {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
# #     ]
# #
# #     pipeVelX = -4
# #
# #     playerVelY = -9
# #     playerMaxVelY = 10
# #     playerMinVelY = -8
# #     playerAccY = 1
# #
# #     playerFlapAccv = -8  # velocity while flapping
# #     playerFlapped = False  # It is true only when the bird is flapping
# #
# #     while True:
# #         for event in pygame.event.get():
# #             if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
# #                 pygame.quit()
# #                 sys.exit()
# #             if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
# #                 if playery > 0:
# #                     playerVelY = playerFlapAccv
# #                     playerFlapped = True
# #                     GAME_SOUNDS['wing'].play()
# #
# #         crashTest = isCollide(playerx, playery, upperPipes,
# #                               lowerPipes)  # This function will return true if the player is crashed
# #         if crashTest:
# #             return
# #
# #             # check for score
# #         playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
# #         for pipe in upperPipes:
# #             pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
# #             if pipeMidPos <= playerMidPos < pipeMidPos + 4:
# #                 score += 1
# #                 print(f"Your score is {score}")
# #                 GAME_SOUNDS['point'].play()
# #
# #         if playerVelY < playerMaxVelY and not playerFlapped:
# #             playerVelY += playerAccY
# #
# #         if playerFlapped:
# #             playerFlapped = False
# #         playerHeight = GAME_SPRITES['player'].get_height()
# #         playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)
# #
# #         # Moving Pipes
# #         for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
# #             upperPipe['x'] += pipeVelX
# #             lowerPipe['x'] += pipeVelX
# #
# #         # Adding Pipes
# #         if 0 < upperPipes[0]['x'] < 5:
# #             newpipe = getRandomPipe()
# #             upperPipes.append(newpipe[0])
# #             lowerPipes.append(newpipe[1])
# #
# #         # Removing Pipes
# #         if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
# #             upperPipes.pop(0)
# #             lowerPipes.pop(0)
# #
# #         # Blitting The Sprites
# #         SCREEN.blit(GAME_SPRITES['background'], (0, 0))
# #         for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
# #             SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
# #             SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
# #
# #         SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
# #         SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
# #         myDigits = [int(x) for x in list(str(score))]
# #         width = 0
# #         for digit in myDigits:
# #             width += GAME_SPRITES['numbers'][digit].get_width()
# #         Xoffset = (SCREENWIDTH - width) / 2
# #
# #         for digit in myDigits:
# #             SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.12))
# #             Xoffset += GAME_SPRITES['numbers'][digit].get_width()
# #         pygame.display.update()
# #         FPSCLOCK.tick(FPS)
# #
# #
# # def isCollide(playerx, playery, upperPipes, lowerPipes):
# #     if playery > GROUNDY - 25 or playery < 0:
# #         GAME_SOUNDS['hit'].play()
# #         return True
# #
# #     for pipe in upperPipes:
# #         pipeHeight = GAME_SPRITES['pipe'][0].get_height()
# #         if (playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
# #             GAME_SOUNDS['hit'].play()
# #             return True
# #
# #     for pipe in lowerPipes:
# #         if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < \
# #                 GAME_SPRITES['pipe'][0].get_width():
# #             GAME_SOUNDS['hit'].play()
# #             return True
# #
# #     return False
# #
# #
# # def getRandomPipe():
# #     pipeHeight = GAME_SPRITES['pipe'][0].get_height()
# #     offset = SCREENHEIGHT / 3
# #     y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
# #     pipeX = SCREENWIDTH + 10
# #     y1 = pipeHeight - y2 + offset
# #     pipe = [
# #         {'x': pipeX, 'y': -y1},  # upper Pipe
# #         {'x': pipeX, 'y': y2}  # lower Pipe
# #     ]
# #     return pipe
# #
# #
# # if __name__ == "__main__":
# #     # This will be the main point from where our game will start
# #     pygame.init()  # Initialize all pygame's modules
# #     FPSCLOCK = pygame.time.Clock()
# #     pygame.display.set_caption('Flappy Bird by CodeWithHarry')
# #     GAME_SPRITES['numbers'] = (
# #         pygame.image.load('gallery/sprites/0.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/1.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/2.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/3.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/4.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/5.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/6.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/7.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/8.png').convert_alpha(),
# #         pygame.image.load('gallery/sprites/9.png').convert_alpha(),
# #     )
# #
# #     GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
# #     GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
# #     GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
# #                             pygame.image.load(PIPE).convert_alpha()
# #                             )
# #
# #     # Game sounds
# #     GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
# #     GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
# #     GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
# #     GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
# #     GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
# #
# #     GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
# #     GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
# #
# #     while True:
# #         welcomeScreen()
# #         mainGame()
# #
# # # If __name__==__main__ usage & necessity
# # if __name__ == '__main__':
# #   def printhar(str) :
# #     str = "sahab"
# #     return f"yeh string mujhe dede thakur {str}"
# #     print(printhar(str))
# #
# # if __name__ == '__main__':
# #     def add(num1, num2):
# #      return num1 + num2 +5
# #     o = add(4, 6)
# # print(o)
# #
# # # o = "num1"
# # # o = int(input("Enter the number: "))
# # # p = 'num2'
# #
# # # p = int(input("Enter the number: "))
# # # print(o+p)
# # #
# #
# # # def function1():
# # #     print("Subscribe now")
# # #
# # # func2 = function1
# # # del function1
# # # func2()
# #
# # # def funcret(num):
# # #     if num==0:
# # #         return print
# # #     if num==1:
# # #         return sum
# # #
# # # a = funcret(1)
# # # print(a)
# #
# # # def executor(func):
# # #     func("this")
# # #
# # #
# # # executor(print)
# #
# # def dec1(func1):
# #     def nowexec():
# #         print("Executing now")
# #         func1()
# #         print("Executed")
# #
# #     return nowexec
# #
# #
# # @dec1
# # def who_is_harry():
# #     print("Harry is a good boy")
# #
# #
# # # who_is_harry = dec1(who_is_harry)
# #
# # who_is_harry()
# #
# # # Recursions VS Iteration
# # # import random
# # #
# # #
# # # def  print2(str):
# # #     print("this is",str)
# # # print2("harry")
# # #
# # #
# # # # n! = n * n-1 * n-2 * n-3.......1
# # # # n! = n * (n-1)!
# # # def factorial_iterative(n):
# # #     """
# # #         :param n: Integer
# # #         :return: n * n-1 * n-2 * n-3.......1
# # #     """
# # #     fac = 1
# # #     for i in range(n):
# # #         fac = fac * (i + 1)
# # #     return fac
# # #
# # #
# # # def factorial_recursive(n):
# # #     """
# # #         :param n: Integer
# # #         :return: n * n-1 * n-2 * n-3.......1
# # #     """
# # #     if n == 1:
# # #         return 1
# # #     else:
# # #         return n * factorial_recursive(n - 1)
# # #     # 5 * factorial_recursive(4)
# # #     # 5 * 4 * factorial_recursive(3)
# # #     # 5 * 4 * 3 * factorial_recursive(2)
# # #     # 5 * 4 * 3 * 2 * factorial_recursive(1)
# # #     # 5 * 4 * 3 * 2 * 1 = 120
# # #
# # #
# # # # 0 1 1 2 3 5 8 13
# # # def fibonacci(n):
# # #     if n == 1:
# # #         return 0
# # #     elif n == 2:
# # #         return 1
# # #     else:
# # #         return fibonacci(n - 1) + fibonacci(n - 2)
# # #
# # #
# # # number = int(input("Enter then number"))
# # # # print("Factorial Using Iterative Method", factorial_iterative(number))
# # # # print("Factorial Using Recursive Method", factorial_recursive(number))
# # # print(fibonacci(number))
# # #
# # import random
# # options=["s","w","g"]
# # print("Welcome to snake water and gun game")
# # humanpoints=0
# # computerpoints=0
# # chance=10
# # noofchance=0
# # print("Type\ns for snake\nw for water\ng for gun\n")
# # while noofchance<10:
# #     userinput=input("\t\nSnake,Water,Gun:")
# #     computerinput=random.choice(options)
# #     #if tie
# #     if userinput == computerinput:
# #         print("#Tied by both .Because both choose same thing And no point given to anyone")
# #         print("#Your point is", humanpoints)
# #         print("#Computer point is", computerpoints)
# #         noofchance = noofchance + 1
# #
# #     else:
# #         print("")
# #     #if user enter s:
# #     if userinput=="s" and computerinput=="w":
# #         print("Snake drank the water\nAnd 1 point added in side of human")
# #         humanpoints=humanpoints+1
# #         print("#Your point is",humanpoints)
# #         print("#Computer point is", computerpoints)
# #         noofchance = noofchance + 1
# #
# #     elif userinput=="s" and computerinput=="g":
# #         print("Snake killed by Gun\n And 1 point added in side of Computer")
# #         computerpoints=computerpoints+1
# #         print("#Your point is", humanpoints)
# #         print("#Computer point is", computerpoints)
# #         noofchance = noofchance + 1
# #
# #
# #     #if user enter w:
# #     elif userinput=="w" and computerinput=="g":
# #         print("Water Screwed up the Gun And 1 point added in side of Human")
# #         humanpoints=humanpoints+1
# #         print("#Your point is", humanpoints)
# #         print("#Computer point is", computerpoints)
# #         noofchance = noofchance + 1
# #
# #     elif userinput=="w" and computerinput=="s":
# #         print("Snake drank the water And 1 point added in side of Computer")
# #         computerpoints=computerpoints+1
# #         print("#Your point is", humanpoints)
# #         print("#Computer point is",computerpoints)
# #         noofchance = noofchance + 1
# #
# #
# #     #if user enter g:
# #     elif userinput=="g" and computerinput=="s":
# #         print("Gun killed the Snake And 1 point added in side of human")
# #         humanpoints=humanpoints+1
# #         print("#Your point is", humanpoints)
# #         print("#Computer point is", computerpoints)
# #         noofchance = noofchance + 1
# #
# #     elif userinput=="g" and computerinput=="w":
# #          print("Water Screwed up the Gun And 1 point added in side of Computer")
# #          computerpoints=computerpoints+1
# #          print("#Your point is",humanpoints)
# #          print("#Computer point is", computerpoints)
# #          noofchance = noofchance + 1
# #     else:
# #         print("")
# # print(humanpoints)
# # print(computerpoints)
# # if humanpoints>computerpoints:
# #     print("Human points are more than Computer .So Human wins")
# # if humanpoints<computerpoints:
# #     print("Computer points is more than Human points .So Computer wins")
# # print("Your point is",humanpoints,"And computer points is",computerpoints)
# # if noofchance==chance:
# #     print("GAME OVER ^_~")
# #     if noofchance==10:
# #         quit()
# #
# #         list1 = ['harry', 1], ['larry', 2], ['karan', 3], ['prakash', 4]
# #         # print(list1[0],list1[1])
# #         for item, lollypop in list1:
# #             print(item, "and lolly is", lollypop)
# #
# #             var1 = "Hell" \
# #                    "o "
# #             var2 = "Trendy tech"
# #         # types python
# #         print(str(var1) + str(var2))
# #         print(100 * "hello world \n")
# #         print("enter your number")
# #         abcd = input()
# #
# #         print("you entered", int(abcd) + 1)
# #
# #         # While loops in python
# #         i = 0
# #         while (i < 45):
# #             print(i)
# #
# #             i = i + 1
# #
# #         i = 10
# #         while (i < 50):
# #             pass
# #
# #         harry = Student()
# #         larry = Student()
# #
# #         harry.name = "Harry"
# #         harry.std = 12
# #         harry.section = 1
# #         larry.std = 9
# #         larry.subjects = ["hindi", "physics"]
# #         print(harry.section, larry.subjects)
# #
# #
# #         class Employee:
# #             no_of_leaves = 8
# #             pass
# #
# #
# #         harry = Employee()
# #         rohan = Employee()
# #
# #         harry.name = "Harry"
# #         harry.salary = 455
# #         harry.role = "Instructor"
# #
# #         rohan.name = "Rohan"
# #         rohan.salary = 4554
# #         rohan.role = "Student"
# #
# #         print(Employee.no_of_leaves)
# #         print(Employee.__dict__)
# #         Employee.no_of_leaves = 9
# #         print(Employee.__dict__)
# #         print(Employee.no_of_leaves)
# #
# #         # Strings are immutable
# #         a = "!!!Harry!! !!!!!!!!! Harry"
# #         print(len(a))
# #         print(a)
# #         print(a.upper())
# #         print(a.lower())
# #         print(a.rstrip("!"))
# #         print(a.replace("Harry", "John"))
# #         print(a.split(" "))
# #         blogHeading = "introduction tO jS"
# #         print(blogHeading.capitalize())
# #
# #         str1 = "Welcome to the Console!!!"
# #         print(len(str1))
# #         print(len(str1.center(50)))
# #         print(a.count("Harry"))
# #
# #         str1 = "Welcome to the Console !!!"
# #         print(str1.endswith("!!!"))
# #
# #         str1 = "Welcome to the Console !!!"
# #         print(str1.endswith("to", 4, 10))
# #
# #         str1 = "He's name is Dan. He is an honest man."
# #         print(str1.find("ishh"))
# #         # print(str1.index("ishh"))
# #
# #         str1 = "WelcomeToTheConsole"
# #         print(str1.isalnum())
# #         str1 = "Welcome"
# #         print(str1.isalpha())
# #
# #         str1 = "hello world"
# #         print(str1.islower())
# #
# #         str1 = "We wish you a Merry Christmas\n"
# #         print(str1.isprintable())
# #         str1 = "         "  # using Spacebar
# #         print(str1.isspace())
# #         str2 = "  "  # using Tab
# #         print(str2.isspace())
# #
# # # If __name__==__main__ usage & necessity
# # if __name__ == '__main__':
# #   def printhar(str) :
# #     str = "sahab"
# #     return f"yeh string mujhe dede thakur {str}"
# #     print(printhar(str))
# #
# # if __name__ == '__main__':
# #     def add(num1, num2):
# #      return num1 + num2 +5
# #     o = add(4, 6)
# # print(o)
# #
# # # o = "num1"
# # # o = int(input("Enter the number: "))
# # # p = 'num2'
# # # p = int(input("Enter the number: "))
# # # print(o+p)
# # #
# #
# # # a = 5             # Global
# # # def function1(x):
# # #     a
# # #     m = 5         # Local
# # #     print(a,m)
# # #     print(x,"this is me")
# # #
# # # function1("I have printed")
# # # print(a)
# # a = 10
# # def function1(x):
# #
# #     m = 5         # Local
# #     global a
# #     a = a + 10
# #     print(a,m)
# #     print(x,"this is me")
# #
# # function1("I have printed")
# # print(a)
# #
# #
# # # def function1():
# # #     print("Subscribe now")
# # #
# # # func2 = function1
# # # del function1
# # # func2()
# #
# # # def funcret(num):
# # #     if num==0:
# # #         return print
# # #     if num==1:
# # #         return sum
# # #
# # # a = funcret(1)
# # # print(a)
# #
# # # def executor(func):
# # #     func("this")
# # #
# # #
# # # executor(print)
# #
# # def dec1(func1):
# #     def nowexec():
# #         print("Executing now")
# #         func1()
# #         print("Executed")
# #
# #     return nowexec
# #
# #
# # @dec1
# # def who_is_harry():
# #     print("Harry is a good boy")
# #
# #
# # # who_is_harry = dec1(who_is_harry)
# #
# # who_is_harry()
# #
# # #
# # # def main():
# # #     print("Hello ")
# # #
# # #
# # #
# # # if __name__ == '__main__':
# # #     main()
# #
# # # pip install pyaudio
# #
# # import pyttsx3 #pip install pyttsx3
# # import speech_recognition as sr #pip install speechRecognition
# # import datetime
# # import wikipedia #pip install wikipedia
# # import webbrowser
# # import os
# # import smtplib
# #
# # engine = pyttsx3.init('sapi5')
# # voices = engine.getProperty('voices')
# # # print(voices[1].id)
# # engine.setProperty('voice', voices[0].id)
# #
# #
# # def speak(audio):
# #     engine.say(audio)
# #     engine.runAndWait()
# #
# #
# # def wishMe():
# #     hour = int(datetime.datetime.now().hour)
# #     if hour>=0 and hour<12:
# #         speak("Good Morning!")
# #
# #     elif hour>=12 and hour<18:
# #         speak("Good Afternoon!")
# #
# #     else:
# #         speak("Good Evening!")
# #
# #     speak("I am Jarvis Sir. Please tell me how may I help you")
# #
# # def takeCommand():
# #     #It takes microphone input from the user and returns string output
# #
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Listening...")
# #         r.pause_threshold = 1
# #         audio = r.listen(source)
# #
# #     try:
# #         print("Recognizing...")
# #         query = r.recognize_google(audio, language='en-in')
# #         print(f"User said: {query}\n")
# #
# #     except Exception as e:
# #         # print(e)
# #         print("Say that again please...")
# #         return "None"
# #     return query
# #
# # def sendEmail(to, content):
# #     server = smtplib.SMTP('smtp.gmail.com', 587)
# #     server.ehlo()
# #     server.starttls()
# #     server.login('youremail@gmail.com', 'your-password')
# #     server.sendmail('youremail@gmail.com', to, content)
# #     server.close()
# #
# # if __name__ == "__main__":
# #     wishMe()
# #     while True:
# #     # if 1:
# #         query = takeCommand().lower()
# #
# #         # Logic for executing tasks based on query
# #         if 'wikipedia' in query:
# #             speak('Searching Wikipedia...')
# #             query = query.replace("wikipedia", "")
# #             results = wikipedia.summary(query, sentences=2)
# #             speak("According to Wikipedia")
# #             print(results)
# #             speak(results)
# #
# #         elif 'open youtube' in query:
# #             webbrowser.open("youtube.com")
# #
# #         elif 'open google' in query:
# #             webbrowser.open("google.com")
# #
# #         elif 'open stackoverflow' in query:
# #             webbrowser.open("stackoverflow.com")
# #
# #
# #         elif 'play music' in query:
# #             music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
# #             songs = os.listdir(music_dir)
# #             print(songs)
# #             os.startfile(os.path.join(music_dir, songs[0]))
# #
# #         elif 'the time' in query:
# #             strTime = datetime.datetime.now().strftime("%H:%M:%S")
# #             speak(f"Sir, the time is {strTime}")
# #
# #         elif 'open code' in query:
# #             codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
# #             os.startfile(codePath)
# #
# #         elif 'email to harry' in query:
# #             try:
# #                 speak("What should I say?")
# #                 content = takeCommand()
# #                 to = "harryyourEmail@gmail.com"
# #                 sendEmail(to, content)
# #                 speak("Email has been sent!")
# #             except Exception as e:
# #                 print(e)
# #                 speak("Sorry my friend harry bhai. I am not able to send this email")
# #         else:
# #             print("No query matched"
# #
# #
# # def sendEmail(to, content):
# #     server = smtplib.SMTP('smtp.gmail.com', 587)
# #     server.ehlo()
# #     server.starttls()
# #     server.login('youremail@gmail.com', 'your-password')
# #     server.sendmail('youremail@gmail.com', to, content)
# #     server.close()
# #
# # if __name__ == "__main__":
# #     wishMe()
# #     while True:
# #     # if 1:
# #         query = takeCommand().lower()
# #
# #         # Logic for executing tasks based on query
# #         if 'wikipedia' in query:
# #             speak('Searching Wikipedia...')
# #             query = query.replace("wikipedia", "")
# #             results = wikipedia.summary(query, sentences=2)
# #             speak("According to Wikipedia")
# #             print(results)
# #             speak(results)
# #
# #         elif 'open youtube' in query:
# #             webbrowser.open("youtube.com")
# #
# #         elif 'open google' in query:
# #             webbrowser.open("google.com")
# #
# #         elif 'open stackoverflow' in query:
# #             webbrowser.open("stackoverflow.com")
# #
# #
# #         elif 'play music' in query:
# #             music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
# #             songs = os.listdir(music_dir)
# #             print(songs)
# #             os.startfile(os.path.join(music_dir, songs[0]))
# #
# #         elif 'the time' in query:
# #             strTime = datetime.datetime.now().strftime("%H:%M:%S")
# #             speak(f"Sir, the time is {strTime}")
# #
# #         elif 'open code' in query:
# #             codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
# #             os.startfile(codePath)
# #
# #         elif 'email to harry' in query:
# #             try:
# #                 speak("What should I say?")
# #                 content = takeCommand()
# #                 to = "harryyourEmail@gmail.com"
# #                 sendEmail(to, content)
# #                 speak("Email has been sent!")
# #             except Exception as e:
# #                 print(e)
# #                 speak("Sorry my friend harry bhai. I am not able to send this email")
# #         else:
# #             print("No query matched"
# #
# #
# # class Student:
# #     pass
# #
# #
# # harry = Student()
# # larry = Student()
# #
# # harry.name = "Harry"
# # harry.std = 12
# # harry.section = 1
# # larry.std = 9
# # larry.subjects = ["hindi", "physics"]
# # print(harry.section, larry.subjects)
# #
# #
# # class Employee:
# #     no_of_leaves = 8
# #     pass
# #
# # harry = Employee()
# # rohan = Employee()
# #
# # harry.name = "Harry"
# # harry.salary = 455
# # harry.role = "Instructor"
# #
# # rohan.name = "Rohan"
# # rohan.salary = 4554
# # rohan.role = "Student"
# #
# # print(Employee.no_of_leaves)
# # print(Employee.__dict__)
# # Employee.no_of_leaves = 9
# # print(Employee.__dict__)
# # print(Employee.no_of_leaves)
# #
# #
# #
# #
#
# name = input("Enter the name: ")
# print(name)
# b_g = input('boy or girl: ')
# print(b_g)
#
# age = int(input("Enter your age"))
#
# if age>=18:
#     print("you are eligible to vote, quickly make your voter card")
# else:
#     print("you are not eligible for vote,wait for some time")
#
#
# # If __name__==__main__ usage & necessity
# if __name__ == '__main__':
#   def printhar(str) :
#     str = "sahab"
#     return f"yeh string mujhe dede thakur {str}"
#     print(printhar(str))
#
# if __name__ == '__main__':
#     def add(num1, num2):
#      return num1 + num2 +5
#     o = add(4, 6)
# print(o)
#
# # o = "num1"
# # o = int(input("Enter the number: "))
# # p = 'num2'
# # p = int(input("Enter the number: "))
# # print(o+p)
# #
#
#
# class Student:
#     pass
#
#
# harry = Student()
# larry = Student()
#
# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)
#
#
# class Employee:
#     no_of_leaves = 8
#     pass
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#
# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)
#
#
#
#
#
# # class Employee:
# #     no_of_leaves = 8
# #     pass
# #
# # harry = Employee()
# # rohan = Employee()
# #
# # harry.name = "Harry"
# # harry.salary = 455
# # harry.role = "Instructor"
# #
# # rohan.name = "Rohan"
# # rohan.salary = 4554
# # rohan.role = "Student"
# #
# # print(Employee.no_of_leaves)
# # print(Employee.__dict__)
# # Employee.no_of_leaves = 9
# # print(Employee.__dict__)
# # print(Employee.no_of_leaves)
# #
# #
# #
# #
#
# name = input("Enter the name: ")
# print(name)
# b_g = input('boy or girl: ')
# print(b_g)
#
# age = int(input("Enter your age"))
#
# if age>=18:
#     print("you are eligible to vote, quickly make your voter card")
# else:
#     print("you are not eligible for vote,wait for some time")
#
#
# # If __name__==__main__ usage & necessity
# if __name__ == '__main__':
#   def printhar(str) :
#     str = "sahab"
#     return f"yeh string mujhe dede thakur {str}"
#     print(printhar(str))
#
# if __name__ == '__main__':
#     def add(num1, num2):
#      return num1 + num2 +5
#     o = add(4, 6)
# print(o)
#
# # o = "num1"
# # o = int(input("Enter the number: "))
# # p = 'num2'
# # p = int(input("Enter the number: "))
# # print(o+p)
# #
#
#
# class Student:
#     pass
#
#
# harry = Student()
# larry = Student()
#
# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)
#
#
# class Employee:
#     no_of_leaves = 8
#     pass
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#
# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves
# # #
# # # var3 = int(input())
# # # if var3>var2:
# # #     print("greater")
# # #
# # # elif var3==var2:
# # #     print("equal")
# # #
# # # else:
# # #    print("lesser")
# # # #sets
# # # sst = (1,2,3,4)
# # # print(s_from_ = set()
# # # print(type(s))
# # # s_from_lilist)
# # # print(type(s_from_list))
# # # l = [1,3,5,7,9]
# # # s = set(l)
# # # print(s)
# # # s.add(8)
# # # s.add(5)
# # # print(s)
# # # s.remove(8)
# # # print(s)
# # #
# # # #types python
# # # print(str(var1) + str(var2))
# # # print(100* "hello world \n")
# # # print("enter your number")
# # # abcd = input()
# # #
# # # print("you entered", int(abcd) + 1)
# # #
# # # import sys
# # # print( sys.path)
# # #
# # # # There are two methods to use functions or variables after importing:
# # # # The first one is to import using an object. For this, we usually import the whole module by using a simple import statement. When we use only the import keyword, we will import the resource directly, like this:
# # # # import sklearn
# # # # When we use the second syntax, we will import the resource from another package or module. Here is an example:
# # # # from flask import Flask
# # # # We can also choose to rename an imported resource, like this:
# # # # import pandas as pd
# # # from sklearn.ensemble import RandomForestClassifier
# # #
# # # print(RandomForestClassifier())
# # #
# # # import file2
# # #
# # # print(file2.a)
# # #
# # # file2.printjoke("This is me")
# # # a = 7
# # #
# # #
# # # def printjoke(str):
# # # #     print(f"this function is a joke {str}")
# # #
# # #
# # # import if__name
# # # print(if__name.add (15,25))
# # import random  # For generating random numbers
# # import sys  # To exit the program
# # import pygame  # pip install pygame
# # from pygame.locals import *
# #
# # # Global Variables for the game
# # FPS = 32
# # SCREENWIDTH = 289
# # SCREENHEIGHT = 511
# # SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
# # GROUNDY = SCREENHEIGHT * 0.8
# # GAME_SPRITES = {}
# # GAME_SOUNDS = {}
# # PLAYER = 'gallery/sprites/bird.png'
# # BACKGROUND = 'gallery/sprites/background.png'
# # PIPE = 'gallery/sprites/pipe.png'
# #
# #
# # def welcomeScreen():
# #     playerx = int(SCREENWIDTH / 5)
# #     playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
# #     messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
# #     messagey = int(SCREENHEIGHT * 0.13)
# #     basex = 0
# #     while True:
# #         for event in pygame.event.get():
# #             # if user clicks on cross button, close the game
# #             if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
# #                 pygame.quit()
# #                 sys.exit()
# #
# #             # If the user presses space or up key, start the game for them
# #             elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
# #                 return
# #             else:
# #                 SCREEN.blit(GAME_SPRITES['background'], (0, 0))
# #                 SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
# #                 SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
# #                 SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
# #                 pygame.display.update()
# #                 FPSCLOCK.tick(FPS)
# #
# #
# # def mainGame():
# #     score = 0
# #     playerx = int(SCREENWIDTH / 5)
# #     playery = int(SCREENWIDTH / 2)
# #     basex = 0
# #
# #     # Create 2 pipes for blitting on the screen
# #     newPipe1 = getRandomPipe()
# #     newPipe2 = getRandomPipe()
# #
# #     # List of upper pipes
# #     upperPipes = [
# #         {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
# #         {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
# #     ]
# #     # List of lower pipes
# #     lowerPipes = [
# #         {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
# #         {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
# #     ]
# #
# #     pipeVelX = -4
# #
# #     playerVelY = -9
# #     playerMaxVelY = 10
# #     playerMinVelY = -8
# #     playerAccY = 1
# #
# #     playerFlapAccv = -8  # velocity while flapping
# #     playerFlapped = False  # It is true only when the bird is flapping
# #
# #     while True:
# #         for event in pygame.event.get():
# #             if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
# #                 pygame.quit()
# #                 sys.exit()
# #             if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
# #                 if playery > 0:
# #                     playerVelY = playerFlapAccv
# #                     playerFlapped = True
# #                     GAME_SOUNDS['wing'].play()
# #
# #         crashTest = isCollide(playerx, playery, upperPipes,
# #                               lowerPipes)  # This function will return true if the player is crashed
# #         if crashTest:
# #             return
# #
# #             # check for score
# #         playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
# #         for pipe in upperPipes:
# #             pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
# #             if pipeMidPos <= playerMidPos < pipeMidPos + 4:
# #                 score += 1
# #                 print(f"Your score is {score}")
# #                 GAME_SOUNDS['point'].play()
# #
# #         if playerVelY < playerMaxVelY and not playerFlapped:
# #             playerVelY += playerAccY
# #
# #         if playerFlapped:
# #             playerFlapped = False
# #         playerHeight = GAME_SPRITES['player'].get_height()
# #         playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)
# #
# #         # Moving Pipes
# #         for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
# #             upperPipe['x'] += pipeVelX
# #             lowerPipe['x'] += pipeVelX
# #
# #         # Adding Pipes
#
#
#         r.pause_threshold = 1
#         audio = r.listen(source)
#
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")
#
#     except Exception as e:
#         # print(e)
#         print("Say that again please...")
#         return "None"
#     return query
#
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()
#
# if __name__ == "__main__":
#     wishMe()
#     while True:
#     # if 1:
#         query = takeCommand().lower()
#
#         # Logic for executing tasks based on query
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)
#
#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")
#
#         elif 'open google' in query:
#             webbrowser.open("google.com")
#
#         elif 'open stackoverflow' in query:
#             webbrowser.open("stackoverflow.com")
#
#
#         elif 'play music' in query:
#             music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#             songs = os.listdir(music_dir)
#             print(songs)
#             os.startfile(os.path.join(music_dir, songs[0]))
#
#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"Sir, the time is {strTime}")
#
#         elif 'open code' in query:
#             codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#             os.startfile(codePath)
#
#         elif 'email to harry' in query:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to = "harryyourEmail@gmail.com"
#                 sendEmail(to, content)
#                 speak("Email has been sent!")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry my friend harry bhai. I am not able to send this email")
#         else:
#             print("No query matched")
# >>>>>>> 66b585c (hello)
#
# # var1 = "Hello "
# # var2 = "Trendy tech"
# # var3 = 56
# # var4 = 14
# #
# # print(str(var1) + str(var2))
# # print(100* "hello world \n")
# # print("enter your number")
# # abcd = input()
# #
# # print("you entered", int(abcd) + 10)
# #
# # print("Enter the number")
# # n1 = input()
# # print("Enter the number")
# # n2 = input()
# # print("Sum of these numbers: ", int(n1) + int(n2))
# #
# # # Data types
# # """
# # 1. int()
# # 2. float()
# # 3. str()
#
# # variables & data types
# a =1
#
#
#
# # If __name__==__main__ usage & necessity
# if __name__ == '__main__':
#   def printhar(str) :
#     str = "sahab"
#     return f"yeh string mujhe dede thakur {str}"
#     print(printhar(str))
#
# if __name__ == '__main__':
#     def add(num1, num2):
#      return num1 + num2 +5
#     o = add(4, 6)
# print(o)
#
# # o = "num1"
# # o = int(input("Enter the number: "))
# # p = 'num2'
# # p = int(input("Enter the number: "))
# # print(o+p)
# #
#
#
# # a = 5             # Global
# # def function1(x):
# #     a
# #     m = 5         # Local
# #     print(a,m)
# #     print(x,"this is me")
# #
# # function1("I have printed")
# # print(a)
# a = 10
# def function1(x):
#
#     m = 5         # Local
#     global a
#     a = a + 10
#     print(a,m)
#     print(x,"this is me")
#
# function1("I have printed")
# print(a)
#
#
# # a = 5             # Global
# # def function1(x):
# #     a
# #     m = 5         # Local
# #     print(a,m)
# #     print(x,"this is me")
# #
# # function1("I have printed")
# # print(a)
# a = 10
# def function1(x):
#
#     m = 5         # Local
#     global a
#     a = a + 10
#     print(a,m)
#     print(x,"this is me")
#
# function1("I have printed")
# print(a)
#
#
# # a = 5             # Global
# # def function1(x):
# #     a
# #     m = 5         # Local
# #     print(a,m)
# #     print(x,"this is me")
# #
# # function1("I have printed")
# # print(a)
# a = 10
# def function1(x):
#     x = int(input("Enter the value of x: "))
#     # x is the variable to match
#     match x:
#         # if x is 0
#         case 0:
#             print("x is zero")
#         # case with if-condition
#         case 4:
#             print("case is 4")
#
#         case _ if x != 90:
#             print(x, "is not 90")
#         case _ if x != 80:
#             print(x, "is not 80")
#         case _:
#             print(x)
#     m = 5         # Local
#     global a
#     a = a + 10
#     print(a,m)
#     print(x,"this is me")
#
# function1("I have printed")
# print(a)
#    a
# #     m = 5         # Local
# #     print(a,m)
# #     print(x,"this is me")
# #
# # function1("I have printed")
# # print(a)
# a = 10
# def function1(x):
#     x = int(input("Enter the value of x: "))
#     # x is the variable to match
#     match x:
#         # if x is 0
#         case 0:
#             print("x is zero")
#         # case with if-condition
#         case 4:
#             print("case is 4")
#
#         case _ if x != 90:
#             print(x, "is not 90")
#         case _ if x != 80:
#             print(x, "is not 80")
#         case _:
#             print(x)
#     m = 5         # Local
#     global a
#     a = a + 10
#     print(a,m)
#     print(x,"this is me")
#
# function1("I have printed")
# print(a)

#     pass
#
#
# harry = Student()
# larry = Student()
#
# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)
#
#
# class Employee:
#     no_of_leaves = 8
#     pass
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#
# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)
#
#
#
#
#
# class Student:
#     pass
#
#
# harry = Student()
# larry = Student()
#
# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)
#
#
# class Employee:
#     no_of_leaves = 8
#     pass
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#
# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)




for pygame import mixer
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

if __name__ == '__main__':
    musiconloop("water.mp3","stop")

# class Student:
#     pass
#
#
# harry = Student()
# larry = Student()
#
# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)
#
#
# class Employee:
#     no_of_leaves = 8
#     pass
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#
# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)
#
#
#
#
#
# class Student:
#     pass
#
#
# harry = Student()
# larry = Student()
#
# harry.name = "Harry"
# harry.std = 12
# harry.section = 1
# larry.std = 9
# larry.subjects = ["hindi", "physics"]
# print(harry.section, larry.subjects)
#
#
# class Employee:
#     no_of_leaves = 8
#     pass
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#
# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)




for pygame import mixer
def musiconloop(file,stopper
#     no_of_leaves = 8
#     pass
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#
# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)

    for


pygame
import mixer


def musiconloop(file, stopper