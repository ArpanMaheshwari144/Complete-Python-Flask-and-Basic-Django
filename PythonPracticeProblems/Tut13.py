import time
def fibonacciIteration(n):
    prevNum=0
    currentNum=1
    for i in range(1, n):
        prevPrevNum=prevNum
        prevNum=currentNum
        currentNum=prevNum+prevPrevNum

    return currentNum

def fibonacciRecursive(n):
    if n==0:
        return 0
    elif(n==1):
        return 1;
    else:
        return fibonacciRecursive(n-1)+fibonacciRecursive(n-2)

if __name__ == '__main__':
    n=int(input("Enter a number: "))
    initialTime=time.time()
    # print(f"By using recursion the value of fib({n}) is {fibonacciRecursive(n)}")
    print(f"By using iteration the value of fib({n}) is {fibonacciIteration(n)}")
    print(f"It took {time.time() - initialTime} seconds")
