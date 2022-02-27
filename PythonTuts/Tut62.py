class ElectronicDevice:
    gen = 5

    def __init__(self, name, model, price, company):
        self.name = name
        self.model = model
        self.price = price
        self.company = company

    def details(self):
        return f"It is used to communicate to other person.\n\tGeneration : {self.gen}\n\tName       : {self.name} \n\tmodel      : {self.model} \n\tcompany    : {self.company} \n\tprice      : {self.price}"


tv = ElectronicDevice("Television", 435, 5600, "SONY")

import inspect
print("Attribute used in class Electronic Device are: ", inspect.getmembers(tv))
print("Object of class Electronic Device are : ", inspect.getfullargspec(ElectronicDevice))
print("Constructors are",inspect.getsource(tv.__init__))
print("Constructors are",inspect.getsource(tv.details))