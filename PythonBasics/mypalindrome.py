n = int(input("Enter a number to check it is a palindrome or not: "))
temp = n
reverse = 0

while(n>0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10   # // --> floor division i.e 5.444 --> 5

if temp==reverse:
    print("Number is a Palindrome")
else:
    print("Number is not a Palindrome")

