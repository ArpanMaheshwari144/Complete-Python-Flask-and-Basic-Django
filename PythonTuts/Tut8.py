# var1=6
# var2=56
# var3=int(input("Enter a number: "))

# if var3>var2:      # :->ki hum statement ke andar jana chahte hai
#     print("Greater")
# if var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# if var3>var2:      # : + enter-> ki hum statement ke andar chale jate hai
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# in keyword
# list=[5,7,3]
# print(5 in list)
# if 5 in list:
#     print("Yes it is in the list")

# list1=[1,2,3]
# print(4 in list1)
# if 4 in list1:
#     print("Yes it is in the list1")

# not in keyword
# list2=[1,2,3]
# print(5 not in list2)
# if 5 not in list2:
#     print("No its not in list2")

# age=int(input("Please Enter your age: "))
# if age>18:
#     print("You can drive")
# elif age==18:
#     print("We cannot decide please come here and gives a driving test")
# else:
#     print("You cannot drive")

age1=int(input("Please Enter your age: "))
if age1>18 and age1<=100:
    print("You can drive")
elif age1>6 and age1<18:
    print("You cannot drive")
elif age1==18:
    print("We cannot decide please come here and gives a driving test")
else:
    print("Enter a valid age")