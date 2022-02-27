# def function1():
#     print("This is me")
# function2=function1
# function2()

# def function1():
#     print("This is me")
# function2=function1
# del function1
# function2()

# def funcreturn(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=funcreturn(0)
# print(a)

# def executor(func):
#     func("Arpan")
# executor(print)

def dec1(func1):
    def nowexecuted():
        print("Executing now")
        func1()
        print("Executed")
    return nowexecuted
def name():
    print("Arpan")
name=dec1(name)
name()
 #or
# @dec1
# def name():
#     print("Arpan")
# name()
