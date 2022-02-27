# class Employee:
#     no_of_leaves=8
#
#     #Self:
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}."
#
# harry=Employee()
# rohan=Employee()
#
# harry.name="Harry"
# harry.salary=4555
# harry.role="Programmer"
#
# rohan.name="Rohan"
# rohan.salary=4535
# rohan.role="Co-ordinator"
#
# print(harry.printdetails())
# print(harry.no_of_leaves)
# print(rohan.printdetails())
# print(rohan.no_of_leaves)


class Employee:
    no_of_leaves=8

    #Constructor:
    def __init__(self, ename, esalary, erole):
        self.name= ename
        self.salary= esalary
        self.role= erole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}."

harry=Employee("Harry",4555,"Programmer")   # Employee(arguments) init constructor mei jayenge
rohan=Employee("Rohan",4535,"Co-ordinator")
print(harry.printdetails())
print(rohan.printdetails())