with open("Arpan.txt") as f:
    a=f.read()
    print(a)

#with block ke baad agar hum koi file open kar ke read karte hai to wo read hogi bcoz with block open and close karta hai files automatically
f=open("Arpan.txt")
print(f.read())
f.close()

