# f = open("practice.py")
# content = f.read()
# print(content)
# f.close()
#
# f = open("practice.py")
# content = f.read()
# print(content)
#
# for line in content:
#     print(line)
#
# for line in f:
#     print(line)
#
# for line in f:
#     print(line, end=""l
a = open("IO_Basics.py")
text =a.read()
print(text)
a.close()

t = open("IO_Basics.py",'a')
hello = t.write("hello,guys")
print(t)

t.close()
