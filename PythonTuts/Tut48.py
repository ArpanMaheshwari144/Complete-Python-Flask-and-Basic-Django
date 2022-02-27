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

karan=Employee.from_dash("Karan-4678-Student")

# print(karan.printdetails())
# print(karan.name)
# print(karan.salary)
# print(karan.role)
# print(karan.no_of_leaves)
# karan.printgood("Karan")

Employee.printgood("Arpan")
Employee.printgood("Harry")
Employee.printgood("Rohan")
