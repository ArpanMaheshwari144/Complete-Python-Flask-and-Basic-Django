# without enumerate
a = ["Arpan", "Coding Zone", "Python", "Intermediate"]
i = 0
for item in a:
    i += 1
    if i % 2 == 0:
        print(i, item)


# with enumerate
a = ["Arpan", "Coding Zone", "Python", "Intermediate"]
for i, item in enumerate(a):
    if (i+1) % 2 == 0:
        print(i, item)