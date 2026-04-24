from functools import lru_cache


@lru_cache
def fib(k):
    if k < 3:
        return 1
    return fib(k - 1) + fib(k - 2)


k = int(input())
print(fib(k))