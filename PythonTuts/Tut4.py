# grocery=["Harpic","Vim Bar","Deo","Soap","Lollypop"]
# grocery1=["Harpic","Vim Bar","Deo","Soap","Lollypop",13]
# print(grocery)
# print(grocery[0])
# print(grocery[1])
# print(grocery[2])
# print(grocery[3])
# print(grocery1)
# print(grocery1[5])

# list=[1,2,3] are mutables(can change) and tuples=(1,2,3) are immutables(cannot change)
numbers=[2, 7, 9, 11, 3]
print(numbers)
# print(len(numbers))
# print(numbers[3])

# numbers.sort()  #ye original list ko change kar deta hai
# print(numbers)

# numbers.reverse()  #ye bhi original list ko change kar deta hai
# print(numbers)

# numbers.sort()
# numbers.reverse()
# print(numbers)

# print(numbers[0:5])
    # or
# print(numbers[0:])
    # or
# print(numbers[:5])
    # or
# print(numbers[:])

#Slicing of list which always return a list
# print(numbers[1:])  #index 1 ko hatake sab print kardo
# print(numbers[1:4]) #index 1 and 4 ko hatake sab print kardo

# print(numbers[::])
   # or
# print(numbers[::1]) #::1->0 gap chodd kar numbers print honge

# print(numbers[::2])  #::2->1 gap chodd kar numbers print honge
# print(numbers[::3])  #::3->2 gap chodd kar numbers print honge
# print(numbers[::-1])   #::-1->list reverse ho jayegi(-1 se kum nhi lena hai)
# print(numbers[1:5:2])

# print(max(numbers))
# print(min(numbers))

# numbers.append(10)  #append ka mtlb last mei add kardo
# print(numbers)

# numbers1=[]
# numbers1.append(1)
# numbers1.append(2)
# numbers1.append(3)
# print(numbers1)

# numbers.insert(2,50)
# print(numbers)

# numbers.remove(2)  #remove function value leta hai index nhi leta
# print(numbers)

# numbers.pop()
# print(numbers)

# numbers[1]=90
# print(numbers)

# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)
# print(sum(a))
# print(a.count(1))
# print(a.index(3))


# tup=(1,2,3)
# print(tup)

# tup1=(1,) #this is tuple
# tup2=(1) #this is not a tuple
# print(tup1)
# print(tup2)

# a=1
# b=2
#Swapping
# temp=a
# a=b
# b=temp
# print(a,b)
  #or
#Swapping
# a,b=b,a
# print(a,b)






