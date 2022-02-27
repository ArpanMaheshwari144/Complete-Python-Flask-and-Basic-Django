def square(x):
    if type(x) == int:
        result = x * x
        print(result)
        print(type(result))
    elif type(x) == float:
        result = x * x
        print(result)
        print(type(result))
    elif type(x) == str:
        print("Sorry")
    else:
        print("Input is Invalid")


square(9.474848)
