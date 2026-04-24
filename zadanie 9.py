from functools import lru_cache


@lru_cache
def combin(n, k):
    if k < 0 or k > n:
        return 0

    if k == 0 or k == n:
        return 1
    return combin(n - 1, k - 1) + combin(n - 1, k)


n = int(input())
k = int(input())
print(combin(n, k))