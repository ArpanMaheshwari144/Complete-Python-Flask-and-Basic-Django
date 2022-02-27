# def function1(name, age, rollno):
#     print("The name of the student is", name, "and his age is", age, "and roll number is", rollno)
# function1("Arpan", 100, 22)


# *args/*vars
# def function2(*args):
#     print(type(args))
#     print("The name of the student is", args[0], "and his age is", args[1], "and roll number is", args[2])
# function2("Adarsh", 101, 10)
      #OR
# lis = ["Adarsh", 101, 10]
# function2(*lis)


# *args/*vars
# def listofnumbers(*numbers):
#     print(numbers)
# listofnumbers(1, 2, 3, 700, 800, 100)


# *args/*vars
# def listofnumbers(*numbers):
#     j = 0
#     for i in numbers:
#         j = i + j
#     print(f"Sum of all numbers is {j}")
# listofnumbers(1,2,3,700,800,100,390,32809,29380,23908,283703)


# **kwargs/**kvars
# def marks(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key, value)
# dictionary
# markslist = {"Arpan": 100, "Adarsh":99,"Verma":98}
# marks(**markslist)


# normal arguments,*args and **kwargs
# def master(normal, *args, **kwargs):
#     print(type(normal))
#     print(type(args))
#     print(type(kwargs))
#     print(normal)
#     for i in args:
#         print(i)
#     for key, value in kwargs.items():
#         print(key, value)
# lis = ["Adarsh", 101, 10]
# markslist = {"Arpan": 100, "Adarsh":99,"Verma":98}
# master("normal args", *lis, **markslist)


# **kwargs/**kvars
dic = {"red": "#f00",
"green": "#0f0",
"blue": "#00f",
"cyan": "#0ff",
"magenta": "#f0f",
"yellow": "#ff0",
"black": "#000",}
def dicitems(**dic):
    for color, colorcode in dic.items():
        print(f"Color code for {color} color is {colorcode}")
dicitems(**dic)