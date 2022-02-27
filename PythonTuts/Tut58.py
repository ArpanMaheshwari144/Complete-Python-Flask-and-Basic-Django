#Dunder methods -> Those methods which have two underscore behind and as well as front like __init__

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 55, "Cleaner")

print(emp1+emp2)
print(emp1/emp2)

#agar str method nhi hai or hum use phir bhi call kar rahe hai to wo repr method ko call kar dega
print(repr(emp1))
print(str(emp1))

print(repr(emp2))
print(str(emp2))

