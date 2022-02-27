#for loop ke sath else jabhi chalega jab for loop properly end ho raha ho mtlb for loop ke andar koi break statement na ho agar for loop ke andar koi break statement hai to phir else nhi chalega

# ingridients=["roti","chawal","bhindi"]
# for item in ingridients:
#     print(item)
# else:
#     print("This for loop ended properly")

# ingridients=["roti","chawal","bhindi"]
# for item in ingridients:
#     print(item)
#     break
# else:
#     print("This for loop ended properly")

# ingridients=["roti","chawal","bhindi"]
# for item in ingridients:
#     if item=="paratha":
#         break
# else:
#     print("Your item was not found")

ingridients=["roti","chawal","bhindi"]
for item in ingridients:
    if item=="roti":
        print("Your item is in list")
        break
else:
    print("Your item was not found")



