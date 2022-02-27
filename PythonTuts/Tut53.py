#Public->access from anywhere
#Protected->apni class se or subclasses(inherited) se hi access hoga
#Private->usi class se access hoga jisme private bna rakha hai

class Employee:
    _protected=9
    __private=10

    def __init__(self,name):
        self.name=name

    def printdetails(self):
        return f"The name is {self.name}"

emp=Employee("Arpan")
print(emp.printdetails())
print(emp._protected)
print(emp._Employee__private)