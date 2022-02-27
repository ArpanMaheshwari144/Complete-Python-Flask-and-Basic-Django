#Diamond Shape Problem

class A:
    def met(self):
        print("A")

class B(A):
    def met(self):
        print("B")

class C(A):
    def met(self):
        print("C")

class D(C,B):
    pass

a=A()
b=B()
c=C()
d=D()

a.met()
b.met()
c.met()
d.met()

