# Coroutines->ki function ek bar initialise ho kar dobara usse call karne ki zarurat na padhe wo chalata rahe

# sirf jab next run hoga tab ye function call hoga or 4 seconds ka delay milega
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(3)

# uske baad hum jab bhi search.send()(means ki searcher function mei kuch search karenge) laga kar kuch bhi send karenge tab wo direct yaha aayega while loop mei
    while True:
        text = (yield)   # searcher function as a Coroutine use ho raha hai
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("3 seconds delay")
next(search)  # ye 4 seconds ka delay le raha hai uske baad koi delay nhi hoga bcoz wo phir text method ko call karega or waha se hamara searcher function Coroutine ki tarah behave karega
print("Next method run")
search.send("harry")  # ye direct text method ko call kar raha hai
input("Press any key:")
search.send("harry and") # ye bhi direct text method ko call kar raha hai
search.close()   # Ek baar Coroutine ko close karne ke baad hum usme dobara kuch bhi nhi send kar sakte hai

