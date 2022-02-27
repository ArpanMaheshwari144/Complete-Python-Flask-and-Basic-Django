# Factorial using iterative method
# def factorial_iterative(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
# number=int(input("Enter the number for factorial: "))
# print("Factorial of a given number by iterative method",factorial_iterative(number))

# Factorial using iterative method
# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# number = int(input("Enter the number for factorial: "))
# print("Factorial of a given number by recursive method", factorial_recursive(number))

#Fibonacci series by recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2)
number=int(input("Enter the number: "))
if(number<=0):
    print("Please enter a number which is greater than 0")
else:
    for i in range(number):
        print(fibonacci(i),end=" ")
