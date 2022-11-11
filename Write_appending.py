# # f = open("NJ.py","w")
# f = open("NJ.py","a")
#
# a = f.write("Naitik bhai bahut achhe hai/n")
# print(a)
# f.close()

# Handle read and write both
f = open("NJ.py","r+")
print(f.read())
f.write("Thank you")