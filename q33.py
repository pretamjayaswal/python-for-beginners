# dic comprehension demo

ar =  (1,2,3,4,5,6,7,8,9,10)

import itertools

x = filter(lambda x : x%2, ar)

print(list(x))

x = map(lambda x : x**2, ar)

print(list(x))

def ff():
    