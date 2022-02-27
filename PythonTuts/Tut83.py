import pickle

# Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki"]  # we use anything(list,set,dictionary,etc..)
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# # dumb 2 arguments leta hai:
# # 1->wo object jo aap pack karna cahate hai
# # 2->file ka object
# pickle.dump(cars, fileobj)
# fileobj.close()

#How to get those pickle object:
file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


# pickle.loads = un objects ke liye use hota hai jo bytes ke format me rhte hai.




