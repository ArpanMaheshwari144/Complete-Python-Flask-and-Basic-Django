# list->[],tuple->(),dictionary->{}

#for loop in list
# list=["Harry","Larry","Carry","Marie"]
# for items in list:
#     print(items)

#for loop in tuple
# list1=("Harry","Larry","Carry","Marie")
# for items in list1:
#     print(items)

#for loop in list of list
# list2=[["Harry",1],["Larry",2],["Carry",6],["Marie",25]]
# for items in list2:
#     print(items)
# for items,lollypop in list2:
#     print(items,"and lollypop is",lollypop)

# list3=[["Harry",1],["Larry",2],["Carry",6],["Marie",25]]
# dict1=dict(list3) #typecaste of list into dictionary
# print(dict1)
# for items in dict1:
#     print(items)
# for items,lollypop in dict1.items():
#     print(items,"and lollypop is",lollypop)

# list4=[["Harry",1],["Larry",2],["Carry",6],["Marie",25],["Arpan",5],["Adarsh",10]]
# for items,lollypop in list4:
#     if lollypop>10:
#         print(items , lollypop)

list5=[1,2,3,4,5,6,7,8,9,"Arpan","Darpan","Adarsh",11,12,13,"Verma"]
for items in list5:
    # if(type(items)==int and items>6):
    #     print(items)
    if str(items).isnumeric() and items>6:  #string mei typecaste ho jayenge items or phir check honge ki isnumeric hai ya nhi
        print(items)

