class Employee:
    no_of_leaves=8

    # Constructor:
    def __init__(self, ename, esalary, erole):
        self.name = ename
        self.salary = esalary
        self.role = erole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

harry=Employee("Harry",4555,"Programmer")
rohan=Employee("Rohan",4535,"Co-ordinator")

harry.change_leaves(3)
print(harry.no_of_leaves)
print(harry.printdetails())
rohan.change_leaves(35)
print(rohan.no_of_leaves)
print(rohan.printdetails())