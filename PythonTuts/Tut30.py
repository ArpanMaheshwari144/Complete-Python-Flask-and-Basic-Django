# str="Arpan"
# a="This is %s"%(str)
# print(a)

# str1="Arpan"
# str2="Maheshwari"
# a="This is %s %s"%(str1,str2)
# print(a)

#String Formatting
# str1="Lana"
# str2="Rhodes"
# a="Hey I am {} {}"
# b=a.format(str1,str2)
# print(b)

# str1="Lana"
# str2="Rhodes"
# str3="Watch"
# str4="My Latest Vedio On"
# str5="PornHub"
# a="Hey I am {4} {3} {2} {1} {0}"  # indexing starts from 0
# b=a.format(str1,str2,str3,str4,str5)
# print(b)

# F-Strings
# str1="Dani"
# str2="Daniels"
# a=f"Hey! This is {str1} {str2}" # this is called f-string
# print(a)

#F-Strings ke andar hum functions bhi use kar sakte hai
import math
str1="Arpan"
str2="Maheshwari"
a=f"This is {str1} {str2} {math.sqrt(49)}"
print(a)