# filter function
def greater_than_2(n):
    if n > 2:
        return True
    else:
        return False

h1 = [1,2,3,4,5,6,7,8,9]

# bcoz filter return object to isilye hum usse list mei typecast krenge
greater_than_2 = list(filter(greater_than_2, h1))  

print(greater_than_2)