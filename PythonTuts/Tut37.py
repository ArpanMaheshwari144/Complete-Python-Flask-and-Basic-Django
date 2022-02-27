def printhar(string):
    return f"This is a function {string}"

def add(num1,num2):
    return num1+num2+5

# name ki value main tabhi hogi jab hum us file se main ko run kar rahe hai jis file mei main function hai
print("The name is", __name__)
if __name__ == '__main__':  # main function kisi bhi dusri file mei run nhi hoga ye sirf apni hi file me run hoga
    print(printhar("Arpan"))
    x=add(3,3)
    print(x)