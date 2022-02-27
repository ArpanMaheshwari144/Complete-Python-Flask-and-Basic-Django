# try:
#     open("Arpan.txt")
# except Exception as e:
#     print(e)
# print("Code.....")



# try:
#     open("Arpan.txt", 'r')
# except EOFError as e:
#     print("EOF Error")
# except IOError as e:
#     print("IO Error")
# finally:
#     print("This will be printed irrespective if the exception occurrence")



try:
    print("I will try this code and will throw exception if there is any problem")
except Exception as e:
    print("I will run only if try block fails")
else:
    print("I will run only if there is no exception. Use this to run code which should only execute if there "
          "is no exception")
finally:
    print("This will be printed in every case")
