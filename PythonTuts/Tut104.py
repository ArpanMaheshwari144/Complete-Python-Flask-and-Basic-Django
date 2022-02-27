a = int(input("Enter a number: "))
for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            print("i = ", i)
            print("j = ", j)
            print("k = ", k)
