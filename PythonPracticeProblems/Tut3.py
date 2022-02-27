# You visit a restaurant called CodeWithHarry and food items in this restaurant are sorted based on their amount of calories. You have to reverse this list of food items containing their calories.
#
# You have to use following three methods to reverse a list:
#
# • Inbuilt method of python
# • Listname[::-1] slicing trick
# • Swapping first element with last one and second element with second last one and so on….
# Input:
# Take a list as an input from the user.
# [5,4,1]
#
# Output:
# [1,4,5]
# [1,4,5]
# [1,4,5]
# All the three methods give same results!

# Python practice problem 3 solution

# Take the size of the list from the user
size = int(input("Enter size of list: "))

# Initialize a blank list
mylist = []

# Take the input from the user one by one

for i in range(size):
    mylist.append(int(input("Enter the list elments:")))

# mylist = [7,3,2, 34, 1,0]
print(f"Your list is {mylist}: ")

reverse1 = mylist[:]   # hum reverse1 mei mylist ki copy save karenge by the help of mylist[:] use hamari original list pe koi farak nhi padega
reverse1.reverse()
print(f"My First reversed list of {mylist} is {reverse1}")

reverse2 = mylist[::-1]
print(f"My Second reversed list of {mylist} is {reverse2}")

reverse3 = mylist[:]
for i in range(len(reverse3) // 2):    # //2 ka mtlb integer milega float nhi milega
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]
    # print(f"the reversed list at i={i} is {reverse3}")

print(f"My Third reversed list of {mylist} is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")


