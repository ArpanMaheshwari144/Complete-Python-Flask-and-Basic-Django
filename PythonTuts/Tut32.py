# *args keyword
# *args and **kwargs optional hote hai
# function mei phle normal arguments rakhne hai fir *args rakhna hai or fir **kwargs rakhna hai as an argument
# def funargs(number,name,*args):
#     # print(type(args))
#     # print(args[0])
#     for items in args:
#         print(items)
#     print(name)
#     print(number)
#
# list=["Harry","Larry","Carry","Arpan","Adarsh"]
# name="Lana Rhodes"
# number=34
# funargs(number,name,*list)

# **kwargs keyword
def funargs(number,name,*args,**kwargs):
    print(type(kwargs))
    for items in args:
        print(items)
    print(name)
    print(number)

    for key,value in kwargs.items():
        print(f"{key} is a {value}")

    for key,value in kwargs.items():
        print(key,value)

list=["Harry","Larry","Carry","Arpan","Adarsh"]
name="Lana Rhodes"
number=34
kw={"Arpan":"Boy","Adarsh":"Boy","Vibhuti":"Chutiya","Verma":"Patra"}
funargs(number,name,*list,**kw)