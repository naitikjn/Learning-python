# #Functions or Docstring
#
# a = 9
# b = 8
# c = sum((a,b))
# print(c)
#
# def function1(a,b):
#     print("Hello you are in function1",a+b)
#
#
# function1()
# function1()
# function1()
# function1()
#
# def function2(a,b):
#     average =(a+b)/2
#     print(average)
# function2(56,67)
#
#
# num1 = input("1")
# print(num1)
#
# a = 10
# b = 10
# gmean = (a*b)/(a+b)
# print(gmean)
#
# def isgreator(a,b):
#     if (a>b):
#         print("A is greator")
#     else:
#         print("B is greator")
#
#
#
# a = 10
# b = 10
# gmean = (a*b)/(a+b)
# print(gmean)

# def isgreator(a,b):
#     if (a>b):
#         print("A is greator")
#     else:
#         print("B is greator")
# print(("FUNCTION IN PYTHON").center(50))
# def SUM(a,b):
#     add = a + b
# a = 75
# b = 80
# if (a>b):
#     print("A is greator and B is smaller")
# else:
#     print("A is smaller and B is greator")
# SUM(a,b)
#
# def function(a = 4, b = 6):
#     # sum = (a + b)/2
#     print("the values of a and b is ",(a + b)/2)
# function(2,4)

def table():
    print("***** TABLEs.com *****".center(50))
    print("HEllo User".center(50))
    num = int(input("Enter the number whose table you want to print :"))
    i = 0
    for i in range(1,11):
        print(num," x ", i , '=',num * i)
table()

print("THANKS FOR USING TABLEs.com ")
