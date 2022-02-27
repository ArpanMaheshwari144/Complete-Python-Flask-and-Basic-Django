# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
#
# print(ls)
#      #or
# # List Comprehensions: ek line mei list ko banane ka tarika
# ls = [i for i in range(100) if i%3==0]
# print(ls)
# print(type(ls))

#Dictionary Comprehensions:
# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# print(dict1)
# print(type(dict1))

# dict1 = {i:f"Item {i}" for i in range(5)}
# print(dict1)

# dict1 = {i:f"Item {i}" for i in range(5)}
# dict2= {value:key for key,value in dict1.items()}
# print(dict1)
# print(dict2)

# Set in python->{ }
# Set Comprehensions:
# dresses = {dress for dress in ["dress1", "dress2","dress1","dress2","dress1", "dress2"]}  # this return a set
# dresses1 = [dress for dress in ["dress1", "dress2","dress1","dress2","dress1", "dress2"]]  # this return a list
# print(dresses)
# print(type(dresses))
# print(dresses1)
# print(type(dresses1))

# Generators ek baar hi iterate ho sakte hai
# Generators Comprehensions:ek line mei generators banane ka tarika
evens = (i for i in range(100) if i%2==0)
print(evens)
print(type(evens))

for i in evens:
    print(i,end=" ")