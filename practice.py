var1 = "Hello "
var2 = "Inspiron 3000"
var3 = 56
var4 = 14

print(str(var1) + str(var2))
print(100* "hello world \n")


Numbers = [2,5,4,9,7]
Numbers.sort()
Numbers.reverse()
print(max(Numbers))
print(min(Numbers))
Numbers.append(5)
print(Numbers)


print("Hello world",end= " ")
print("next line")
print("C:\\naitik")
print("naitik \n is \n good \n boy \t  ")      # Escape sequence
print("miss hill \b school")

abc = 'Python is a programming language'
print(abc.find("is"))                                  # String methods and its functions
print(abc.endswith("language"))
print(abc.count("p"))
print(abc.capitalize())
print(abc.upper())
print(abc.replace("programming" , "Python"))
Numbers = []
Numbers.append(25)
Numbers.append(15)
Numbers.append(26)
#Numbers.sort()
#Numbers.reverse()
Numbers.insert(2 ,5)
Numbers.remove(5)


print("Enter the number")
n1 = input()
print("Enter the number")
n2 = input()
print("Sum of these numbers: ", int(n1) + int(n2))

mystr="Naitik is a good boy"
print(mystr)
print(len(mystr))            # length of String
print(mystr[-8:-5])          # Indexing in String
print(mystr[-10])
abc = 'Python is a programming language'
print(abc.find("is"))


Numbers.insert(2 ,5)
Numbers.remove(5)
#Numbers.pop()
Numbers[2] = 2
print(Numbers)
# Mutable = can change
# Immutable = can not change
# Tuple
tp = (1,2,3)
print(tp)
a = 1
b = 8
temp = a
a = b
temp = b
print(a,b)
groceries = ["Nescafe","Horlicks","No.1","fena","Wheel"]
print(groceries)
print("exit code")


list1 = [["HRM",301], ["statistics",302], ["income tax and practices",303],["e-commerce",304],["management principles",305]]
print(list1)
for item in list1:
    print(item)
dict1 = dict(list1)
for item in dict1:
    print(item)
list2 = (["kurkure",5],["fritts",10],["cheese balls",20])
for item in dict1.items():
    print(item)
for item,price in list2:
    print(item,"@",price)
subjects = ["maths", "moral_science","general_knowledge","english", "hindi", "sanskrit", 10, 20, 40, 50, 70, 80, 100 ]
for item in subjects:
    if str(item).isnumeric() and item>=30:
        print(item)
for item in subjects:
    if str(item).isalpha():
        print(item)
print(5)

#while loops
i = 1

while (True):
    i = i+1
    if (i + 1 <10):
         print (i + 1)

         while (i == 100):
             i = i + 1
             print(i + 1, end="  ")
             if (i > 44):
                 i = i + 1
             print(i + 1, end="  ")
             break
             if (i < 48):
                 i = i + 2
                 break

a = True
b = False
print(5 is not 5)
print(5 or 8)
print(5 and 5)

#Membership operator
List = [5 , 55 , 65 , 48 , 14 , 25 , 47 , 65 , 32 , 24 , 15 , 20 , 10 , 85]
print(32 or 14 in List)
print(85 and 20 in List)
print(48 is not List)

a = int(input("enter num a :\n"))
b = int(input("enter num b :\n"))

if a<b: print("b is greator than a")
elif a==b: print("same hai")


#sets
s = set()
print(type(s))
s_from_list = (1,2,3,4)
print(s_from_list)
print(type(s_from_list))
l = [1,3,5,7,9]
s = set(l)
print(s)
s.add(8)
s.add(8)
print(s)
s.remove(8)
print(s)
s1 = (0,8,6,4,2)
print(s.isdisjoint(s1))
print(max(s))
print(min(s1))
s2 = s.intersection({11,12,13})
s3 = s.union({90,60,30})
print(s,s3)


