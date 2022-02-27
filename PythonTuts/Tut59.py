#metaclass->agar hum kisi bhi class ko ABCMeta class se inherit karenge to wo class apne child classes ko ye aadesh de sakti hai ki aapko abstract method ko implement kara hi padega
#hum abstract class/function ke objects nhi bna sakte hai

from abc import ABCMeta,abstractmethod
class Shape(metaclass=ABCMeta):
    # abstract methods can not be inherit isiliye hume jo bhi abstract method bna rahe hai kisi bhi class mei or wo class inherit ho rhi hai to wo abstract method inherit nhi hoga.
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1=Rectangle()
print(rect1.printarea())
      #or
# Ye method version 3.4 se above mei hi kaam karega

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0
#
# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#     def __init__(self):
#         self.length = 6
#         self.breadth = 7
#
#     def printarea(self):
#         return self.length * self.breadth
#
# rect1=Rectangle()
# print(rect1.printarea())