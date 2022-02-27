def factorial(n):
    factorial = 1

    if n < 0:
        print("Error: Factorial of a negative number can not be calculated")
    elif n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        return  factorial


if __name__ == '__main__':
    n = int(input("Enter a number to calculate it's factorial: "))
    print("The factorial of", n, "is", factorial(n))
    a = input()
