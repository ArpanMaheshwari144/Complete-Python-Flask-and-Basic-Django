def matrix(m,n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter the element of matrix in index[{i}][{j}]: "))
            row.append(inp)
        o.append(row)
    return o

def sum(A, B):
    output = []
    for i in range(len(A)): # number of rows
        row = []
        for j in range(len(A[0])):  # number of columns
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

print("\n**********Enter Matrix A**********")
A = matrix(m, n)

print("\n**********Enter Matrix B**********")
B = matrix(m, n)

print("\n**********A matrix is**********")
print(A)
print("\n**********B matrix is**********")
print(B)

s = sum(A, B)
print(f"\nThe sum of the two matrix are")
print(s)

