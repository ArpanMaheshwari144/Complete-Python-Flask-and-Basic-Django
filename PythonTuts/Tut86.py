class area:

    pi=3.14

    def __init__(self,length,breath,diameter):
        self.length=length
        self.breath=breath
        self.diameter=diameter

    def triangle(self):
        Area=(self.breath*self.length)*.5
        return Area
    def square(self):
        Area=self.length*self.length
        return Area
    def Circle(self):
        Area=area.pi*self.diameter**2
        return Area

class volume(area):
    def __init__(self,length,breath,diameter,height):
        area.__init__(self,length,breath,diameter)
        self.height=height

    def V_triangle(self):
        vol=area.Circle(self)*self.height
        return vol



obj=volume(4,5,6,7)
print(obj.V_triangle())