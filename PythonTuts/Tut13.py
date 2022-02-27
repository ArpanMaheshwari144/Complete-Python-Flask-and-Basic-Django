# i=0
# while(i<20):
#     print(i+1,end=" ")
#     i=i+1

# i=0
# while(i<100):
#     if(i==50):
#         break
#     print(i,end=" ")
#     i=i+1

# i=0
# while(i<50):
#     if(i<5):
#         i = i + 1
#         continue
#     print(i,end=" ")
#     i=i+1

# i=0
# while(True):  while(True) or while(1) means ki loop chalta rahega infinite times
#     if(i<5):
#         i=i+1
#         continue
#     print(i,end=" ")
#     if(i==20):
#         break
#     i=i+1

while(1):
    i=int(input("Enter a number: "))
    if(i<=100):
        print("Try again")
        continue
    else:
        print("You entered a number greater than 100")
        break
        #or
# while(True):
#     i=int(input("Enter a number: "))
#     if(i>100):
#         print("You entered a number greater than 100")
#         break
#     else:
#         print("Try again")
#         continue
