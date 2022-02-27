f=open("Adarsh.txt")

try:
    f1=open("Myfile.txt")

except Exception as e:
    print(e)

finally:
    print("Run this anyway...")
    print(f.read())
    f.close()

print("Important code! Execute it")