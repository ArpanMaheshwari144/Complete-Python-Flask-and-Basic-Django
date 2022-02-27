n = int(input("Enter the number you want multiplication table of: "))
m = int(input("Enter a number where you want your table to be print: "))

for i in range(1,m+1):
    print(n, "X", i ,"=", n*i)