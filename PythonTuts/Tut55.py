# class A:
#     classvar1="I am in class A"
#
#     def __init__(self):
#         self.var1="I am inside class A's constructor"   #instance variable
#         self.classvar1="Instance variable in class A"   #instance variable
#
# class B(A):
#     classvar1="I am var1 in class B"
#
# a=A()
# b=B()
#
# print(b.classvar1)  #sabse phle instance variable ko search karega B class mei agar B class mei instance variable nhi mila to B class jaha se inherit ho rhi hai waha jayega i.e A class mei or class A mei search karega ki koi instance variable hai ya nhi

class A:
    classvar1="I am in class A"

    def __init__(self):
        self.var1="I am inside class A's constructor"   #instance variable
        self.classvar1="Instance variable in class A"   #instance variable
        self.special="Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super().__init__()  #agar humne ise A class or B class ke constructor se chalaya to A or B class Ke constructor call honge
        self.var1="I am inside class B's constructor"   #instance variable
        self.classvar1="Instance variable in class B"   #instance variable
        # super().__init__() #agar humne ise A class or B class ke constructor se chalaya to sirf A class Ka constructor call hoga
        # print(super().classvar1)
a=A()
b=B()
print(a.special, a.classvar1, a.var1,)
print(b.special, b.classvar1, b.var1,)

