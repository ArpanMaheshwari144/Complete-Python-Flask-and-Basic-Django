class Employee:
    var=8
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

class Player:
    var=9
    no_of_games:4

    def __init__(self, plname, plgame):
        self.name=plname
        self.game=plgame

    def printplay(self):
        return f"The Name is {self.name}. Game is {self.game}."

#Multiple Inheritance
class coolProgrammer(Player, Employee):
    # var=10
    language="C++"
    def printlanguage(self):
        print(self.language)

patra=coolProgrammer("Patra",["Cricket"])
print(patra.printplay())
patra.printlanguage()
print(patra.var)

#Multiple Inheritance
class coolProgrammer(Employee, Player):
    # var=10
    language="C++"
    def printlanguage(self):
        print(self.language)

karan=coolProgrammer("Karan",7676,"CoolProgrammer")
print(karan.printdetails())
karan.printlanguage()
karan.printgood("Karan")
print(karan.var)

arpan=Player("Arpan","Cricket")
adarsh=Player("Adarsh","Hockey")
print(arpan.printplay())
print(adarsh.printplay())

# harry = Employee("Harry", 4555, "Instructor")
# rohan = Employee("Rohan", 4535, "Student")
# verma = Employee.from_dash("Verma-4567-Student")
# print(harry.printdetails())
# print(rohan.printdetails())
# print(verma.printdetails())
# harry.printgood("Harry")
# rohan.printgood("Rohan")
# verma.printgood("Verma")









