mystr="Harry is a good boy"
print(mystr)

print(len(mystr))

print(mystr[3])  # 0 se indexing ho rhi hai

print(mystr[0:5]) # 0 to 5-1 tak hi print hoga

print(mystr[0:25])

print(mystr[0:]) # 0:->ki puri string print kar dega

print(mystr[:])

print(mystr[:5]) # :5->ki 0 to 5-1 tak hi print karega

print(mystr[0:5:2]) # 0:5:2->phle 0 to 5-1 tak print karega phir jo string return hui hai usme 1 ke gap par jo words aayenge unko print karega

print(mystr[::])  # ::->0:19:1

print(mystr[0:19:1])

print(mystr[0::])

print(mystr[:19:])

print(mystr[::1]) #::1->0 ke gap par words print karega

print(mystr[::2])  #::2->1 ke gap par words print karega

print(mystr[::3])  #::3->2 ke gap par words print karega

print(mystr[-4:-2])
   # or
print(mystr[15:17])

print(mystr[::-1])  #::-1->ye string reverse kar dega

print(mystr[::-2])  #::-2->ye phle string reverse karega phir ek ke gap se print karega

#Strings functions
print(mystr.isalnum()) #isalnum(is alpha numeric)-> it means agar kisi bhi string mei numbers hai or spaces nhi hai to ye true return karega agar numbers hai or space nhi hai to ye false return karega agar numbers hi nhi hai to ye only false return karega

print(mystr.isalpha()) #isalpha->ki string mei spaces hai to false or spaces nhi hai to true

print(mystr.endswith("boy"))
print(mystr.endswith("arpan"))

print(mystr.count("o"))

print(mystr.capitalize())  #capitalize->always string mei phle letter ko capital kar dega

print(mystr.find("good"))

print(mystr.lower())

print(mystr.upper())

print(mystr.replace("Harry","Arpan"))

print(mystr.casefold()) #Converts string into lower case