#Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

secret = (input("Enter Your Message:"))
s = list(secret)
print(s)

print("Your Message Is Converted Into Secret Code")

print("LOADING")
if (len(secret)>=3):
    secret.append(len(secret[0]))
    secret.pop(0)
    h= "hjv"
    secret.append(h)
    j = "woi"
    secret.insert(j[0])
    print(secret)
else:
    print(secret.reverse())


