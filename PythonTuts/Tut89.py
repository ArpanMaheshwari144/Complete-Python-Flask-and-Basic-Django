# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object

a=[7,4,5]
b=a
print(id(a))
print(id(b))
print(b==a)
print(b is a)
#
b[0]=0
print(a)
print(id(b))
print(id(a))
#
c=a[:]  # it is making a copy of a
print(c)

print(id(c))
print(id(a))
print(id(b))
print(b==c)
print(a==c)
#
print(b is c)
print(a is c)


# a =[6, 4 , "34"]
# b = [6, 4 , "34"]
# print(id(a))
# print(id(b))
# print(b is a)
