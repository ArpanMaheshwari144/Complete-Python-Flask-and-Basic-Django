class Employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    @staticmethod
    def isOpen(day):
        if day == "Sunday":
            return False
        else:
            return True

# static method direct class name se bhi call ho sakta hai uske liye class ka object banane ki koi zarurat nhi hai or wo object name se bhi call ho sakta hai
print(Employee.isOpen("Sunday"))

arpan = Employee("Arpan", "Maheshwari", 440000)
print(arpan.isOpen("Sunday"))

