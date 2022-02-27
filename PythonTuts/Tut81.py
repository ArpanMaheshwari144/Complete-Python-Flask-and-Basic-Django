import json

data = '{"var1":"harry", "var2":56}'
# print(data)
# print(data[ 'var1'])
# print(type(data))

parsed = json.loads(data)
# print(parsed)
# print(parsed['var1'])
# print(type(parsed))

# json.load =  string input leta hai or output me json object deta hai...
# key sort in dumps = result ko sort krna hai ya nahi .. specify krne k liye


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
jscomp = json.dumps(data2)  # dumbs json file ke data ko js object mei change karta hai
print(jscomp)

