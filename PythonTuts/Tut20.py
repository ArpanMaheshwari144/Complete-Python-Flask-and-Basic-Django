#f=open(filename,mode)

# f=open("arpan.txt","r") #->r is for read mode
# f=open("arpan.txt","rb") #->rb is for read binary mode
# f=open("arpan.txt","rt")  #->rt is for read text mode
# content=f.read()
# print(content)
# f.close()

# f=open("arpan.txt","rt")
# content=f.read(3)
# print("1",content)
# content=f.read(3)
# print("2",content)
# f.close()

# f=open("arpan.txt","rt")
# content=f.read(3445)
# print("1",content)
# content=f.read(3445)
# print("2",content)
# f.close()

# f=open("arpan.txt","rt")
# for line in f:
#     print(line,end="")
# f.close()

# f=open("arpan.txt","rt")
# print(f.readline())
# print(f.readline())
# f.close()

f=open("Arpan.txt","rt")
print(f.readlines())  #readlines()->it returns the lines into lists
f.close()