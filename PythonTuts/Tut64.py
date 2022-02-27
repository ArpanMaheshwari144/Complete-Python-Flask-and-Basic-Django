"""
Iterable -> ye dono method define hote hai-> __iter__() or __getitem__()
Iterator -> ye method define hota hai-> __next__()
Iteration
"""

# generators special tarah ke iterators hote hai jo ki sirf ek baar hi iterate ho sakte hai

# for i in range(5):  #range ek generator hota hai jo ki value ko on fly(time) print karta hai unhe store nhi karta
#     print(i)

def gen(n):
    for i in range(n):
        # return i  #return ek function hai jo ki sirf value ko return karta hai
        yield i  #yeild ek generator hai jo ki on the fly(time) generate karta hai values ko or ye ek generator object return karega

#gen(args) ke arguments mei hum jitni value denge __next__ function utne tak hi print kar payega
# g = gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# g = gen(3)
# for i in g:
#     print(i)

# String iterable hoti hai bcoz isme __iter__() or __getitem() define hota hai
h="Harry"
print(h[0])
print(iter(h))
for i in h:
    print(i)

# String iterable hoti hai bcoz isme __iter__() or __getitem() define hota hai
h = "Harry"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# Bcoz Integer mei __iter__() or __getitem() define nhi hota hai or hum ise iterator nhi de sakte so isiliye ye iterable nhi hota hai so it returns error
# h=34343
# ier=iter(h)
# print(ier.__next__())