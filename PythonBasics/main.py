import time

def func1(a, b):
    return a + b

def func2(a, b):
    num1 = a
    num2 = b
    if(a>b and a!=3):
        pass
    sum([3,5])
    return a + b

if __name__ == '__main__':
    # init = time()  # for from time import time
    init = time.time()  # for normally import time

    for i in range(0, 1000):
        func1(3,5)
    print("First function takes time: ", time.time()-init)

    # init = time.time()
    for i in range(0, 1000):
        func2(3,5)
    print("Second function takes time: ", time.time()-init)

    print("Overall time: ", time.time()-init)
