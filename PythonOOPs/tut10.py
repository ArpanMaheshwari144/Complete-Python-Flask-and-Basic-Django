class Employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee ({} {} {})'.format(self.fname,self.lname,self.salary)

    def __str__(self):
        return "The first name of the Employee is {}".format(self.fname)


arpan = Employee("Arpan", "Maheshwari", 440000)
adarsh = Employee("Adarsh","Pandey",450000)

print(arpan+adarsh)

print(repr(arpan))

print(str(arpan))



