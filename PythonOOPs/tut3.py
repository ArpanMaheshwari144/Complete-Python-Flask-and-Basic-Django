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


arpan = Employee("Arpan", "Maheshwari", 440000)
adarsh = Employee("Adarsh","Pandey",450000)

print(arpan.salary)
arpan.increaseSalary()
print(arpan.salary)

print(adarsh.salary)
adarsh.increaseSalary()
print(adarsh.salary)

