num1=input("Enter first number: ")
num2=input("Enter second number: ")
try:
    print("The sum of these two numbers is",int(num1)+int(num2))
except Exception as e:
    print(e)

print("This is very important code")