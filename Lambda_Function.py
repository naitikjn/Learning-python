# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))


a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x: x[1])
print(a)


def function_name ():
    result = lambda n1, n2, n3: n1 + n2 + n3;
    print("Sum of three values : ", result(10, 20, 25))
    list.sort(key=myFunc, reverse=True | False)