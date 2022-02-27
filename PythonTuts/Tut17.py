a=9
b=7
c=sum((a,b))
print(c)

def function1():
    print("You are in function1")
function1()

def function2(a,b):
    print("You are in function2", a+b)
function2(5,3)

def function3(a,b):
    average=(a+b)/2
    print(average)
function3(5,5)

def function4(a,b):
    average=(a+b)/2
    return average
v=function4(5,5)
print(v)

def substraction(a,b):
    """This is a function which will calculate substraction of two numbers"""   #->this is a docstring
    sub=a-b
    return sub
print(substraction.__doc__)
x=substraction(5,3)
print(x)

