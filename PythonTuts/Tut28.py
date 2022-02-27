#Lambda functions/Anonymous functions
# def add(a,b):
#     return a+b
# print("This addition function is written without lambda function",add(2,3))
#
# add=lambda a,b:a+b
# print("This addition function is written with lambda function",add(2,3))
#
# def minus(a,b):
#     return a-b
# print("This substraction function is written without lambda function",minus(9,4))
#
# minus=lambda a,b:a-b
# print("This substraction function is written with lambda function",minus(9,4))

def a_first(a):
    return a[1]  #a[1] sort by index 1
a=[[11,12],[5,13],[14,3]]
a.sort(key=a_first)  #sort function argument leta hai as a key="fuction name"
print(a)

a=[[11,12],[5,13],[14,3]]
a.sort(key=lambda x:x[0])  #x[0] sort by index 0
print(a)
