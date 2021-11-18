from functools import lru_cache
from functools import cache






#Memorization method 3(not teached)
@cache
def f(n):
    if n<2:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            return f(n-2) + f(n-1)
    
#Memorization methon 1
cache = {}
def f_cache(n):
    if n<2:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            fn = f(n-2) + f(n-1)
            cache[n] = fn
            return fn

#Memorization method 2
@lru_cache(maxsize = 1000)
def f(n):
    if n<2:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            return f(n-2) + f(n-1)