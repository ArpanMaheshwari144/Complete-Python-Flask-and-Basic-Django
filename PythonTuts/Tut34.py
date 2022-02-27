# l1=["Bhindi","Aloo","Chopsticks","Noodles"]
#
# i=1
# for items in l1:
#     if i%2 != 0:
#         print(f"Jarvis please buy {items}")
#     i+=1

#Enumerate function
l1=["Bhindi","Aloo","Chopsticks","Noodles"]
for index,items in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy {items}")
