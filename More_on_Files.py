f = open("NJ.py")
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(10)
f.close()