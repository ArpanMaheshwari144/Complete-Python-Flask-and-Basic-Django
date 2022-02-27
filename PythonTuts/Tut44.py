class Employee:
    no_of_leaves=8

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=4555
harry.role="Programmer"

rohan.name="Rohan"
rohan.salary=4535
rohan.role="Co-ordinator"

# print(harry.name)
# print(harry.salary)
# print(harry.role)
# print(rohan.name)
# print(rohan.salary)
# print(rohan.role)

# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# print(harry.no_of_leaves)
# print(harry.__dict__)
# print(rohan.no_of_leaves)
# print(rohan.__dict__)

# Employee.no_of_leaves=9
# print(Employee.no_of_leaves)
# print(harry.no_of_leaves)
# print(rohan.no_of_leaves)

# rohan.no_of_leaves=9
# print(Employee.no_of_leaves)
# print(harry.no_of_leaves)
# print(rohan.no_of_leaves)
# print(rohan.__dict__)

harry.no_of_leaves=9
print(Employee.no_of_leaves)
print(rohan.no_of_leaves)
print(harry.no_of_leaves)
print(harry.__dict__)  #dict function class/functions/anything ke andar jitna bhi content hai usko return karta hai as a dictionary





