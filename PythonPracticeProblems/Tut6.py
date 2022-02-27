def strPalindrome(s):
    return s == s[::-1]

def intPalindrome(n):
    return str(n) == str(n)[::-1]


print("This is a program to check a string or a integer is palindrome or  not")
a=int(input("Would you Check for String or Integer press 1 for string and 2 for integer:"))
b=a
if b == 1:
    isstr = input("Enter a string:")
    ans = strPalindrome(isstr)

    if ans:
        print("Palindrone")
    else:
        print("Not a Palindronme")

else:
    isint = int(input("Enter a integer:"))
    ans = intPalindrome(isint)

    if ans:
        print("Palindrome")
    else:
        print("Not a Palindrome")
