# a=int(input("Enter number of rows you want to enter: "))
# b=input("Enter 0 is for False or 1 is for True: ")
# if b=="1":
#     for i in range(0,a+1):
#         print("*" * i)
# elif b=="0":
#     for i in range(a,0,-1):
#         print("*" * i)

a=int(input("Enter number of rows you want to enter: "))
b=bool(int(input("Enter 0 is for False or 1 is for True: ")))

def star(a,b):
    if b==True:
        c=1
        while(c<=a):
            print(c * "*")
            c=c+1
    else:
        while(a>0):
            print(a * "*")
            a=a-1
star(a,b)