class Employee:

    incrementSalary = 1.5
    noOfEmployees = 0

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.incrementSalary = 1.6

    def increaseSalary(self):
        # ye incrementSalary ko phle init function mei search krega or fir class mei search karega
        # self.salary = self.salary * self.incrementSalary

        # ye incrementSalary ko sirf or sirf class mei search karega
        self.salary = self.salary * Employee.incrementSalary


    @staticmethod
    def isOpen(day):
        if day == "Sunday":
            return False
        else:
            return True


class Programmer(Employee):
    def __init__(self,fname,lname,salary, programmerlanguage, exprience):
        super().__init__(fname,lname,salary)
        self.programmerlanguage=programmerlanguage
        self.exprience=exprience

    def increaseSalary(self):
        self.salary = int(self.salary * (self.incrementSalary+0.2))
        return self.salary


arpan = Programmer("Arpan", "Maheshwari", 44000, "Java", '4-years')
print(arpan.fname)
print(arpan.lname)
print(arpan.salary)
print(arpan.programmerlanguage)
print(arpan.exprience)
print(arpan.increaseSalary())
print(arpan.isOpen("Monday"))

