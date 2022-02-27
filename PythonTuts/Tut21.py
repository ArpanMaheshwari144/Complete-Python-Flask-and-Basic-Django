#w->open a file for writing means ki agar us naam ki file hai to jo usme likha hai use saaf kardo or jo f.write mei likha hai use likh do or us naam ki file nhi bni to phle file banao or jo f.write mei likha hai use likhdo
# f=open("Arpan1.txt","w")
# f.write("Arpan Maheshwari")
# f.close()

#a->append mode ka means ki jo file mei hai use to rakho or jo f.write mei likha hai use file mei daal do
# f=open("Arpan1.txt","a")
# f.write("Arpan Maheshwari\n")
# f.close()

# f=open("Arpan1.txt","a")
# a=f.write("Arpan Maheshwari\n")
# print(a)
# f.close()

f=open("Arpan1.txt","w")
a=f.write("Arpan Maheshwari\n") #f.write number of characters return karta hai jitne us file mei characters hai including new line character
print(a)
f.close()

# r+->for read and writing into a file
# f=open("Arpan1.txt","r+")
# print(f.read())
# f.write("Thank You")
# f.close()