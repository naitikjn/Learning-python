f = open("practice.py")
content = f.read()
print(content)
#f.close()

f = open("practice.py")
content = f.read()
print(content)

for line in content:
    print(line)

for line in f:
    print(line)

for line in f:
    print(line, end="")