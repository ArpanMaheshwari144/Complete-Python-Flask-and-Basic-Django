# without list comprehension
list_1 = [1,2,3,4,5,6,7,8,9]
divide_by_3 = []
for item in list_1:
    if item % 3 == 0:
        divide_by_3.append(item)
print("without using list comprehension ",divide_by_3)

# with list comprehension
print("with using list comprehension ",[item for item in list_1 if item % 3 == 0])

# dictionary comprehension
dict1 = {'a':45, 'b':65, 'A':100}
print({k.lower():dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys()})

# set comprehension
squared = {x**2 for x in [1,2,3,4,5,5,4,4]}
print(squared)

# generator
gen = (i for i in range(10) if i % 3 ==0)
for item in gen:
    print(item)
