# import datetime
# def gettime():
#     return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c=int(input("Enter 1 for excersise and 2 for food: "))
#         if(c==1):
#             value=input("Type here\n")
#             with open("harry-ex.txt","a") as op:
#                 op.write(str([str(gettime())])+": "+value+"\n")
#             print("Successfully Written")
#         elif(c==2):
#             value = input("Type here\n")
#             with open("harry-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("Successfully Written")
#     elif(k==2):
#         c = int(input("Enter 1 for excersise and 2 for food: "))
#         if (c == 1):
#             value = input("Type here\n")
#             with open("rohan-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("Successfully Written")
#         elif (c == 2):
#             value = input("Type here\n")
#             with open("rohan-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("Successfully Written")
#     elif(k==3):
#         c = int(input("Enter 1 for excersise and 2 for food: "))
#         if (c == 1):
#             value = input("Type here\n")
#             with open("hammad-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("Successfully Written")
#         elif (c == 2):
#             value = input("Type here\n")
#             with open("hammad-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("Successfully Written")
#     else:
#         print("Plz enter valid input (1(harry),2(rohan),3(hammad)")
# def retrieve(k):
#     if k==1:
#         c=int(input("Enter 1 for excersise and 2 for food: "))
#         if(c==1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i,end="")
#         elif(c==2):
#             with open("harry-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==2):
#         c = int(input("Enter 1 for excersise and 2 for food: "))
#         if (c == 1):
#             with open("rohan-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("rohan-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==3):
#         c = int(input("Enter 1 for excersise and 2 for food: "))
#         if (c == 1):
#             with open("hammad-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("hammad-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     else:
#         print("Plz enter valid input (harry,rohan,hammad)")
# print("Health Management System: ")
# a=int(input("Press 1 for log the value and 2 for retrieve: "))
#
# if a==1:
#     b = int(input("Press 1 for harry 2 for rohan 3 for hammad: "))
#     take(b)
# else:
#     b = int(input("Press 1 for harry 2 for rohan 3 for hammad: "))
#     retrieve(b)


client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
lock_list = {1: "Exercise", 2: "Diet"}
def getdate():
    import datetime
    return datetime.datetime.now()
try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())
    print("Selected Client : ", client_list[client_name], "\n", end="")
    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    op = int(input())
    if op == 1:
        for key, value in lock_list.items():
            print("Press", key, "for", value, "\n", end="")
        lock_name = int(input())
        print("Selected Job : ", lock_list[lock_name])
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'
        while (k != "n"):
            print("Enter", lock_list[lock_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op == 2:
        for key, value in lock_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        lock_name = int(input())
        print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")