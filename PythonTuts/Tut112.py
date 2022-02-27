for i in range(1, 9):
    for j in range(1, 9):
        if i == 2 and (j >= 3 and j < 8):
            print(" ", end="")
        elif j == 7 and (i >= 3 and i <= 6):
            print(" ", end="")
        else:
            print("*", end="")
    print()