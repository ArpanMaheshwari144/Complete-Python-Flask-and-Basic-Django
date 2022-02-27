A = [[1,5,3],
     [4,0,2],
     [6,0,3]]
B = [[1,0],
     [1,0],
     [5,0]]
# A(3X2) B(3X2) ---> C(3X2)
C = [[0,0],
     [0,0],
     [0,0]]

# python indexing always starts from 0

for i in range(0,len(C)):
    for j in range(0, len(C[0])):
        for k in range(0, len(B)):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)


