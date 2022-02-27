import random
import string

punctuations = "!,-,/:;_"
chars = string.ascii_letters + string.digits + punctuations

key_length = 10
key = "". join(random.sample(chars, key_length))
print(key)
