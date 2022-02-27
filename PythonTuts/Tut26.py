# l=10 #Global variable ye program mei khi bhi use ho sakta hai
# def function(n):
#     a=5 #Local variable ye sirf apne function mei hi call ho sakta hai
#     b=8
#     print(a,b)
#
#     #change the value of global variable in function by global keyword
#     global l
#     l=l+5
#     print(l)
#
#     print(n,"I have printed")
#
# function("This is it")
# print(l)

def harry():
    x=20
    def rohan():
        global x #agar apne global kissi bhi fuction ke function ke andar likh rakha hai to wo seedha bahar dekhega agar use waha koi bhi variable nhi milega to jo aapne global keyword ki madad se jo bhi varaible bna rakha hai to wo bahar initialise ho jayega
        x=88  #ye x=88 dono fuction ke bahar initialise ho gya hai bcoz of global keyword
    print("Before calling rohan function",x)
    rohan()
    print("After calling rohan function",x)

harry()
print(x)
