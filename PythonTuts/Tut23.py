#f.tell()->indicate karta hai ki hamara file pointer kitne character read kar chuka hai
# f=open("arpan.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()

f=open("Arpan.txt")
f.seek(0)     #f.seek(0) mtlb ki ye kaha se read karega start kare(jitna aap f.seek(args->number) number denge utne charaters hatake print kar dega)
# f.seek(11)  # 10 characters hatake print karega
print(f.readline())
f.close()