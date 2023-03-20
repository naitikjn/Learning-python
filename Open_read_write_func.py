f = open("practice.py")
content = f.read()
print(content)
f.close()

f = open("practice.py")
content = f.read()
print(content)

for line in content:
    print(line)

for line in f:
    print(line)

for line in f:
    print(line, end=""l
a = open("IO_Basics.py")
text =a.read()
print(text)
a.close()

t = open("IO_Basics.py",'a')
hello = t.write("hello,guys")
print(t)

t.close()

f = open('myfile.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)

f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()