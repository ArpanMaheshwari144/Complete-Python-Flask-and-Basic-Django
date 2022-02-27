class Employee:

    incrementSalary = 1.5

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


    @classmethod # decorator
    def change_increment(cls,amount):
        cls.incrementSalary = amount


arpan = Employee("Arpan", "Maheshwari", 440000)
adarsh = Employee("Adarsh","Pandey",450000)

print(arpan.salary)
Employee.change_increment(2)
arpan.increaseSalary()
print(arpan.salary)