# a=input("What is your name: ")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")


# a=input("What is your name: ")
# b=int(input("How much do you earn: "))
# if b==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")

c=input("Enter your name: ")
try:
    print(a)

except Exception as e:
    if c=="Harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")