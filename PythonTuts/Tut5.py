# Dictionary is nothing but key value pairs
# d1={ }
# print(type(d1))

# d2={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza"}
# print(d2)
# print(d2["Arpan"])

# d3={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza","Shubham":{"Breakfast":"Maggie","Lunch":"Bhindi","Dinner":"Roti"}}
# print(d3)
# print(d3["Shubham"])
# print(d3["Shubham"]["Lunch"])

# d4={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza","Shubham":{"Breakfast":"Maggie","Lunch":"Bhindi","Dinner":"Roti"}}
# d4["Ankit"]="Junk Food"
# d4["Verma"]="Chaat"
# d4[10]="Daal"
# print(d4)

# d5={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza","Shubham":{"Breakfast":"Maggie","Lunch":"Bhindi","Dinner":"Roti"}}
# d5["Ankit"]="Junk Food"
# d5["Verma"]="Chaat"
# d5[10]="Daal"
# del d5[10]
# print(d5)

# Functions in Dictionary
# d6={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza","Shubham":{"Breakfast":"Maggie","Lunch":"Bhindi","Dinner":"Roti"}}
# d7=d6
# del d7["Harry"]
# print(d6)
# print(d7)

# d8={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza","Shubham":{"Breakfast":"Maggie","Lunch":"Bhindi","Dinner":"Roti"}}
# d9=d8.copy()
# del d9["Harry"]
# print(d8)
# print(d9)

# d10={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza","Shubham":{"Breakfast":"Maggie","Lunch":"Bhindi","Dinner":"Roti"}}
# print(d10.get("Harry"))

# d11={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza","Shubham":{"Breakfast":"Maggie","Lunch":"Bhindi","Dinner":"Roti"}}
# d11.update({"Leena":"Candy"})
# print(d11)

d12={"Harry":"Bhindi","Arpan":"Murga","Adarsh":"Pizza","Shubham":{"Breakfast":"Maggie","Lunch":"Bhindi","Dinner":"Roti"}}
print(d12.items())
print(d12.keys())
print(d12.values())