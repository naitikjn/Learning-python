# a = 5             # Global
# def function1(x):
#     a
#     m = 5         # Local
#     print(a,m)
#     print(x,"this is me")
#
# function1("I have printed")
# print(a)
a = 10
def function1(x):

    m = 5         # Local
    global a
    a = a + 10
    print(a,m)
    print(x,"this is me")

function1("I have printed")
print(a)