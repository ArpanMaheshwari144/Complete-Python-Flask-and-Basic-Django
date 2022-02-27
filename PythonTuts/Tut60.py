# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#
#     def explain(self):
#         return f"This Employee is {self.fname} {self.lname}"
#
#     def printemail(self):
#         return f"{self.fname}.{self.lname}@gmail.com"
#
# emp1=Employee("Arpan","Maheshwari")
#
# print(emp1.printemail())
# emp1.fname="Gola"
# print(emp1.printemail())


# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#
#     def explain(self):
#         return f"This Employee is {self.fname} {self.lname}"
#
#     @property
#     def printemail(self):
#         return f"{self.fname}.{self.lname}@gmail.com"
#
# emp1=Employee("Arpan","Maheshwari")
#
# print(emp1.printemail)
# emp1.fname="Gola"
# print(emp1.printemail)

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
emp1.fname="Gola"
print(emp1.email)

emp1.email="Lana.Rhodes@gmail.com"
print(emp1.fname)
print(emp1.lname)
print(emp1.email)

del emp1.email
print(emp1.email)

emp1.email="Verma.Patra@gmail.com"
print(emp1.email)