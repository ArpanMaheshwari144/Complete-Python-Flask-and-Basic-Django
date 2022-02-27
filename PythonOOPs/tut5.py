class Employee:

    noOfEmployees = 0

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.noOfEmployees += 1


print(Employee.noOfEmployees)

arpan = Employee("Arpan", "Maheshwari", 440000)
adarsh = Employee("Adarsh","Pandey",450000)

print(Employee.noOfEmployees)
