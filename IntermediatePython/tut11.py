# This module is helpful when we want to know where should we insert our value in a list.

import bisect
number = 10
a = [1,2,3,4,9,11,12,13]
print(bisect.bisect(a, number))
bisect.insort(a, number)
print(a)

