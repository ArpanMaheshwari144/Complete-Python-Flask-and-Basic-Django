class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set.Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting now....")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

emp1=Employee("Arpan","Maheshwari")
print(emp1.email)
# print(dir(emp1))

#Object IntroSpection:
# print(type(emp1))
# print(id(emp1))
# print(type("This is a string"))
# print(id("This is a string"))
# print(id("Arpan"))
# print(type(34))
# print(id(34))

# o="This is a String"
# print(dir(o))

import inspect
print(inspect.getmembers(emp1))