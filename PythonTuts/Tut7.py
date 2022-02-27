l=[1,2,3,4]
s_from_list=set(l)
print(s_from_list)
print(type(s_from_list))

s=set()
print(type(s))
s.add(1)
s.add(1)
s.add(2)
s1=s.union({1,2,3})
s2=s.intersection({1,2,3})
print(s,s1,s2)

print(len(s))

print(len(s1))

print(len(s2))

print(min(s))

print(max(s))

print(min(s1))

print(max(s1))

print(min(s2))

print(max(s2))

a={1,2,3}
b={4,5,6}
print(a.isdisjoint(b))
a.remove(2)
print(a)


