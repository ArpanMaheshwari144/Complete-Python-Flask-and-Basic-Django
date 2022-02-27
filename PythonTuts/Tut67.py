no_of_list = int(input("How many items you want to add in a list: "))
input_string = input("Enter elements separated by space and starts with 0: ")
t= int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension: "))
if t==1:
    ls = [i for i in range(no_of_list)]
    print(ls)
    print(type(ls))
elif t==2:
    dict1 = {i: f"Item {i}" for i in range(no_of_list)}
    print(dict1)
    print(type(dict1))
elif t==3:
    s = (i for i in range(no_of_list) if i>1)
    print(s)
    print(type(s))

    for i in s:
        print(i, end=" ")


