f=open("Adarsh.txt")

try:
    f1=open("Code.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running if except is running so else block is not running")

finally:
    print("Run this anyway...")
    print(f.read())
    f.close()

print("Important code! Execute it")