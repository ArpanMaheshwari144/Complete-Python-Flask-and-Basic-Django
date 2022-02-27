class Employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary


    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname,lname,salary)


arpan = Employee("Arpan", "Maheshwari", 440000)
adarsh = Employee("Adarsh","Pandey",450000)
verma = Employee.from_str("Verma-Patra-77000")

print(verma.fname)
print(verma.lname)
print(verma.salary)


