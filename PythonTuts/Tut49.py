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
    def from_dash(cls, string):
        # params=string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
               #or
        return (cls(*string.split("-")))

    @staticmethod
    def printgood(string):
        print(f"{string} is good boy")

#Single Inheritance:

class Programmer(Employee):
    no_of_holidays=36
    def __init__(self, pname, psalary, prole, planguage):
        self.name=pname
        self.salary=psalary
        self.role=prole
        self.language=planguage

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary}. Role is {self.role} and language known is {self.language}"

harry=Employee("Harry",4555,"Instructor")
rohan=Employee("Rohan",4535,"Student")
verma=Employee.from_dash("Verma-4567-Student")

# print(harry.printdetails())
# print(rohan.printdetails())
# print(verma.printdetails())
# harry.printgood("Harry")
# rohan.printgood("Rohan")
# verma.printgood("Verma")

arpan=Programmer("Arpan",4567,"Programmer",["Java","Python"])
adarsh=Programmer("Adarsh",4578,"Programmer",["Kotlin","Python"])
vibhuti=Programmer.from_dash("Vibhuti-4545-Programmer-['Java','Kotlin']")

print(arpan.printprog())
print(arpan.printdetails())
print(arpan.no_of_holidays)
arpan.printgood("Arpan")
print(adarsh.printprog())
print(adarsh.printdetails())
print(adarsh.no_of_holidays)
adarsh.printgood("Adarsh")
print(vibhuti.printprog())
print(vibhuti.printdetails())
print(vibhuti.no_of_holidays)
vibhuti.printgood("Vibhuti")
