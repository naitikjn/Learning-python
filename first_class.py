
# #
# # rohan.name = "Rohan"
# # rohan.salary = 4554
# # rohan.role = "Student"
# #
# # print(Employee.no_of_leaves)
# # print(Employee.__dict__)
# # Employee.no_of_leaves = 9
# # print(Employee.__dict__)
# # print(Employee.no_of_leaves)
# #
# #
# #
# #
# #
# # class Student:
# #     pass
# #
# #
# # harry = Student()
# # larry = Student()
# #
# # harry.name = "Harry"
# # harry.std = 12
# # harry.section = 1
# # larry.std = 9
# # larry.subjects = ["hindi", "physics"]
# # print(harry.section, larry.subjects)
# #
# #
# # class Employee:
# #     no_of_leaves = 8
# #     pass
# #
# # harry = Employee()
# # rohan = Employee()
# #
# # harry.name = "Harry"
# # harry.salary = 455
# # harry.role = "Instructor"
# #
# # rohan.name = "Rohan"
# # rohan.salary = 4554
# # rohan.role = "Student"
# #
# # print(Employee.no_of_leaves)
# # print(Employee.__dict__)
# # Employee.no_of_leaves = 9
# # print(Employee.__dict__)
# # print(Employee.no_of_leaves)
# string = input("Enter a string :")
# count = 3
# while True:
#     if string[0] == 'a':
#         string=string [2:]
#     elif string [-1] == 'b':
#         string = string [:2]
#     else:
#         count+=1
#         break
# print(string)
# print(count)

# s = "CBSE digital india"
# for i in range(len(s)-1,0,-1):
#         print(s[i].lower(),end='')
#     elif i%2==0:
#         if s[i].islower():
#             print(s[i].upper(),end='')
#     else:
#         print("@" ,end='')
# a = "EXAM2021"
# b = " "
# i = 0
# while i<len(a):
#     if a[i]>="A" and a[i]<= 'M':
#         b =b + a[i+1]
#     elif a[i] >= "0" and a[i] <= '9':
#         b =b + a[i-1]
#
#     else:
#         b = b + '*'
#     i = i + 1
# print(b)