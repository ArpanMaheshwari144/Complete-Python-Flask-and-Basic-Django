import pickle
import requests
data=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').text
print(data)

l1=data.split("\n")
print(l1)

l2=[item.split(",") for item in l1 if len(item)!=0]
print(l2)

# pickling the python object
with open("myirisData.pkl","wb") as f:
    pickle.dump(l2, f)

#Reading Of Pickel file
with open('myirisData.pkl','rb') as f:
    print(pickle.load(f))