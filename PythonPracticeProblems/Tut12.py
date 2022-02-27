n = int(input("Enter a number: "))
sum = 0
order = len(str(n))
# print(order)
copy_n = n
while(n > 0):
    digit = n % 10
    sum = sum + digit ** order  # ** -> exponentiation operator in python
    n = n // 10  # in python 88/10=8.8 and 88//10=8(it gives floor division)

if(sum == copy_n):
    print(f"{copy_n} is a armstrong number")
else:
    print(f"{copy_n} is not a armstrong number")
