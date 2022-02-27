class Employee:

    incrementSalary = 1.5

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.incrementSalary = 1.6


arpan = Employee("Arpan", "Maheshwari", 440000)
adarsh = Employee("Adarsh","Pandey",450000)

print(Employee.__dict__)

print(arpan.__dict__)
arpan.increment = 9
print(arpan.__dict__)
