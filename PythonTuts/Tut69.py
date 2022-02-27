# import time
#
# def some_work(n):
#     # Some tasks taking n seconds
#     time.sleep(n)
#     return n
#
#
# if __name__ == '__main__':
#     print("Now running some work")
#     some_work(3)
#     print("Done.... Calling again")
#     some_work(3)
#     print("Called again")

import time
from functools import lru_cache   # lru_cache ek decorator hai

@lru_cache(maxsize=3)   # maxsize mtlb kitni value ko cache karna cahate hai
def some_work(n):
    # Some tasks taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Done.... Calling again")
    input()
    some_work(3)
    print("Called again")
