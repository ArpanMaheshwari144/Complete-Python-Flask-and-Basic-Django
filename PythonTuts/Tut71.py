# f=open("Myfile.txt")
# print("Important code! Execute it")
       #or
try:
    f=open("Myfile.txt")

except Exception as e:
    print(e)

print("Important code! Execute it")