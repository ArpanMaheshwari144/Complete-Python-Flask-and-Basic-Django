import os

print(dir(os))

# print(os.getcwd())  # get current working directory

# f = open("Adarsh.txt")

# os.chdir("C://")   # to change the current working directory

# print(os.getcwd())

# f = open("Adarsh.txt")

# listdir() return karta hai list
# print(os.listdir())    # jo bhi current directory mei hai unhe print kar dega(by deafault ye wo directory leta hai jisme hum kaam kar rahe hai)

# print(type(os.listdir()))

# print(os.listdir("C://"))  # arguments mei humne ise ek dusri directory dedi ab jo bhi is directory mei hai unhe print kara dega

# print(type(os.listdir("C://")))

# os.mkdir("This")   # mkdir ek folder bna dega aapki current directory mei(jaha aap kaam kar rahe hai)

# os.makedirs("This")  #makedirs ek folder bna dega aapki current directory mei

# os.makedirs("This/Arpan")  # makedirs-> folder ke andar ek or folder bhi bna sakta hai

# os.makedirs("This/Arpan/That")  #makedirs->folder ke andar folder or us folder ke andar ek or folder bhi bna dega means ki aapko jitne folder or folder ke andar folder banane hai wo makedirs se ban sakte hai

# os.rename("file1.txt", "file.txt")

# print(os.environ.get('Path'))

# print(os.path.join("C://", "ArpanMaheshwari.txt"))

# print(os.path.join("C://", "/ArpanMaheshwari.txt"))

# print(os.path.join("C:/", "ArpanMaheshwari.txt"))

# print(os.path.exists("C://"))

# print(os.path.exists("C://Arpan"))

# print(os.path.isdir("C://"))

print(os.path.isfile("C://Program Files"))
