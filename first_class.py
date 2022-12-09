class Student:
    pass


harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.section, larry.subjects)


class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)





