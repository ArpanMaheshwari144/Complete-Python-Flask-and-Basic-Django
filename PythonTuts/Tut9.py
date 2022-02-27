a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=input("Enter a operator addition(represents 1), substraction(represents 2), multiplication(represents 3), division(represents 4), modulus(represents 5), exponent(represents 6) and floor division(represents 7) : ")

if a==45 and b==3 and c=="*":
    print("555")
elif a==56 and b==9 and c=="+":
    print("77")
elif a==56 and b==6 and c=="/":
    print("4")
else:
    if "1" in c:
        print(a + b)
    elif "2" in c:
        print(a - b)
    elif "3" in c:
        print(a * b)
    elif "4" in c:
        print(a / b)
    elif "5" in c:
        print(a % b)
    elif "6" in c:
        print(a ** b)
    elif "7" in c:
        print(a // b)
    else:
        print("Error! Please Check Your Input")

# def calculator():
#     print("\nWellcome to Calc:")
#     operation = input('''
#     Please type in the math operation you would like to complete:
#     + for addition
#     - for subtraction
#     * for multiplication
#     / for division
#     ** for power
#     % for modulo
#
#     Enter Your Choice:
#     ''')
#
#     num1 = int(input("Enter first Number: "))
#     num2 = int(input("Enter second Number: "))
#
#     if operation == '+':
#         if num1 == 56:
#             print("56 + 9 = 77")
#         else:
#             print(f"{num1} + {num2} = {num1 + num2}")
#     elif operation == '-':
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif operation == '*':
#         if num1 == 45:
#             print("45 * 3 = 555")
#         else:
#             print(f"{num1} * {num2} = {num1 * num2}")
#     elif operation == '/':
#         if num1 == 56:
#             print("56/6 = 4")
#         else:
#             print(f"{num1} / {num2} = {num1 / num2}")
#     elif operation == '**':
#         print(f"{num1} ** {num2} = {num1 ** num2}")
#     elif operation == '%':
#         print(f"{num1} % {num2} = {num1 % num2}")
#     else:
#         print("You Press a Invalid Key")
#     again()
#
#
# def again():
#     cal_again = input('''
#     Do you want to calculate again?
#     Please type y for YES or n for NO.
#     ''')
#
#     if cal_again == 'y':
#         calculator()
#     elif cal_again == 'n':
#         print("See You Later")
#     else:
#         again()
#
# calculator()

