# name="Jack”
#
#  n="%s My name is %s” %name
#
# print(n)
#
#  Output: "My name is Jack."
# name=”Jack”
# class=5
# s=”%s is in class %d”%(name,class)
# print(s)str = "This article is written in {} "
#
# print (str.format("Python"))
# # F strings
# import math
#
# me = "Harry"
# a1 =3
# # a = "this is %s %s"%(me, a1)
# # a = "This is {1} {0}"
# # b = a.format(me, a1)
# # print(b)

# # time
# print(a)
#
#
# # me = "Harry"
# # a1 =3
# # # a = "this is %s %s"%(me, a1)
# # # a = "This is {1} {0}"
# # # b = a.format(me, a1)
# # # print(b)
# a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)
#
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))
