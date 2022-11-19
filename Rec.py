# Recursions VS Iteration
# import random
#
#
# def  print2(str):
#     print("this is",str)
# print2("harry")
#
#
# # n! = n * n-1 * n-2 * n-3.......1
# # n! = n * (n-1)!
# def factorial_iterative(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
#
#
# def factorial_recursive(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
#     # 5 * factorial_recursive(4)
#     # 5 * 4 * factorial_recursive(3)
#     # 5 * 4 * 3 * factorial_recursive(2)
#     # 5 * 4 * 3 * 2 * factorial_recursive(1)
#     # 5 * 4 * 3 * 2 * 1 = 120
#
#
# # 0 1 1 2 3 5 8 13
# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# number = int(input("Enter then number"))
# # print("Factorial Using Iterative Method", factorial_iterative(number))
# # print("Factorial Using Recursive Method", factorial_recursive(number))
# print(fibonacci(number))
#
import random
options=["s","w","g"]
print("Welcome to snake water and gun game")
humanpoints=0
computerpoints=0
chance=10
noofchance=0
print("Type\ns for snake\nw for water\ng for gun\n")
while noofchance<10:
    userinput=input("\t\nSnake,Water,Gun:")
    computerinput=random.choice(options)
    #if tie
    if userinput == computerinput:
        print("#Tied by both .Because both choose same thing And no point given to anyone")
        print("#Your point is", humanpoints)
        print("#Computer point is", computerpoints)
        noofchance = noofchance + 1

    else:
        print("")
    #if user enter s:
    if userinput=="s" and computerinput=="w":
        print("Snake drank the water\nAnd 1 point added in side of human")
        humanpoints=humanpoints+1
        print("#Your point is",humanpoints)
        print("#Computer point is", computerpoints)
        noofchance = noofchance + 1

    elif userinput=="s" and computerinput=="g":
        print("Snake killed by Gun\n And 1 point added in side of Computer")
        computerpoints=computerpoints+1
        print("#Your point is", humanpoints)
        print("#Computer point is", computerpoints)
        noofchance = noofchance + 1


    #if user enter w:
    elif userinput=="w" and computerinput=="g":
        print("Water Screwed up the Gun And 1 point added in side of Human")
        humanpoints=humanpoints+1
        print("#Your point is", humanpoints)
        print("#Computer point is", computerpoints)
        noofchance = noofchance + 1

    elif userinput=="w" and computerinput=="s":
        print("Snake drank the water And 1 point added in side of Computer")
        computerpoints=computerpoints+1
        print("#Your point is", humanpoints)
        print("#Computer point is",computerpoints)
        noofchance = noofchance + 1


    #if user enter g:
    elif userinput=="g" and computerinput=="s":
        print("Gun killed the Snake And 1 point added in side of human")
        humanpoints=humanpoints+1
        print("#Your point is", humanpoints)
        print("#Computer point is", computerpoints)
        noofchance = noofchance + 1

    elif userinput=="g" and computerinput=="w":
         print("Water Screwed up the Gun And 1 point added in side of Computer")
         computerpoints=computerpoints+1
         print("#Your point is",humanpoints)
         print("#Computer point is", computerpoints)
         noofchance = noofchance + 1
    else:
        print("")
print(humanpoints)
print(computerpoints)
if humanpoints>computerpoints:
    print("Human points are more than Computer .So Human wins")
if humanpoints<computerpoints:
    print("Computer points is more than Human points .So Computer wins")
print("Your point is",humanpoints,"And computer points is",computerpoints)
if noofchance==chance:
    print("GAME OVER ^_~")
    if noofchance==10:
        quit()