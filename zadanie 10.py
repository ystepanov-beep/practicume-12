def maxlist(a):
    if len(a) == 1:
        return a[0]
    return max(a[0], maxlist(a[1:]))

a = list(map(int, input().split()))
print(maxlist(a))