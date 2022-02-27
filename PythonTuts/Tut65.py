#Fibonacci series using generators:
# def gen(n):
#     a = -1
#     b = 1
#     while (n!=0):
#         c = a + b
#         yield c
#         a=b
#         b=c
#         n=n-1
#
# g=gen(5)
# for i in g:
#     print(i,end=" ")

#Factorial using generators:
def gen(n):
    if n < 0:
        yield 0
    elif n == 0 or n == 1:
        yield 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        yield fact

g = gen(6)
for i in g:
    print(i,end=" ")