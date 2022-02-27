a = [8, 4, 16, 20]

# list comprehension
b1 = [x/2 for x in a]  # -> / -> this will give a float value

# list comprehension
b2 = [x//2 for x in a] # -> // -> this will give a integer value

print(b1)
print(b2)
