# numbers=["3","34","79"]
# for i in range(len(numbers)):  # hum range me number as a argument hi daal sakte hai
#     numbers[i]=int(numbers[i])
# numbers[2]=numbers[2]+1
# print(numbers[2])

#Map Function:
# numbers=["1","2","3"]
# # map function 2 arguments lega:
# # 1 argument:wo function jo ki aap chahte hai ki wo saare elements par apply ho jaye.
# # 2 argument:wo jaha aap apply karna chahte hai
# numbers=list(map(int,numbers))  #hum map object(kyoki map function object return karta hai) ko phle list me typecaste karenge kyoki hum map function ko list pe apply kar rahea hai
# numbers[2]=numbers[2]+1
# print(numbers[2])

# def square(a):
#     return a*a
# num=[1,2,3,4,5,6,7,8,9]
# squ=list(map(square,num))  #map function object return karta hai
# print(squ)

# num=[1,2,3,4,5,6,7,8,9]
# squ=list(map(lambda a:a*a,num))
# print(squ)

# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func=[square, cube]
# n=int(input("Enter a number to find square or cube: "))
# for i in range(n):
#     # aap jabhi bhi map use karenge to list ko bhi lagana padega agar aap list return karana chahate hai to
#     value=list(map(lambda x:x(i), func)) # ans list mei print hoga kyoki humne use list mei typecaste kar rakha hai
#     print(value)

#Filter Function:
# list_1=[1,2,3,4,5,6,7,8,9,10]
#
# def is_greater_than_5(num):
#     return num>5
#
# # filter function 2 arguments lega:
# # 1 argument:wo function jo ki aap lagana chahate hai.
# # 2 argument:wo list jis par wo function lagana chahate hai
# greater_than_5=list(filter(is_greater_than_5, list_1))  # hum filter object(kyoki filter function object return karta hai) ko phle list me typecaste karenge kyoki hum filter function ko list pe apply kar rahea hai
# print(greater_than_5)

# list_2=["Arpan","Adarsh","Verma","Patra"]
# def name_length(names):
#     if names[0] != 'A':
#         return names
#
# name=list(filter(name_length,list_2))
# print(name)

#Reduce Function:
# list1=[1,2,3,4,5,6,7]
# num=0
# for i in list1:
#     num=num+i
# print(num)

    #or

from functools import reduce
list1=[1,2,3,4,5,6,7]

# filter function 2 arguments lega:
# 1 argument:wo function jo ki aap lagana chahate hai.
# 2 argument:wo list jis par wo function lagana chahate hai
num=reduce(lambda x,y:x+y, list1)
print(num)


