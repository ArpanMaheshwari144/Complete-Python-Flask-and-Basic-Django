a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = [a, b, c]
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if i != j & j != k & k != i:  # Bitwise Operator
            # if i != j and j != k and k != i:  # Logical operator
                print(d[i], " ", d[j], " ", d[k])
