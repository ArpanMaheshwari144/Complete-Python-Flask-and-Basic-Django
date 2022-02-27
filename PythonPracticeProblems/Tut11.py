# Funny Names
# Its result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to come up with some funny names.

# Your program should take the number of names and the names separated by space as input. Output should be funny names in the same order.

# Input:
# Enter number of friends:
# 3
# Enter the name of your 3 friends:
# Rohan Das
# Shubham Agarwal
# Ritesh Arora

# Output:
# Ritesh Das
# Shubham Arora
# Rohan Agarwal

import random
num=int(input("Enter The Number Of Games:"))
counter=num
print(f"Enter The {num} space seprated Names")
names=[]
while num:
    names.append(input())
    num-=1


f_individual_list=[]
l_individual_list=[]
for name in names:
    first_name,last_name=name.split(' ',1)
    f_individual_list.append(first_name)
    l_individual_list.append(last_name)
#print(f_individual_list,l_individual_list)

funny_name=[]
while counter:
    f=random.choice(f_individual_list)
    l=random.choice(l_individual_list)

    f_individual_list.remove(f)
    l_individual_list.remove(l)
    funny_name.append(f+' '+l)
    counter-=1

print(funny_name)


