class Employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.incrementSalary = 1.6


arpan = Employee("Arpan", "Maheshwari", 440000)
adarsh = Employee("Adarsh","Pandey",450000)

print(arpan.fname)
print(arpan.lname)
print(arpan.salary)

print(adarsh.fname)
print(adarsh.lname)
print(adarsh.salary)

