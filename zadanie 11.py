def maxlist(a):
    if len(a) == 1:
        return a[0]
    return max(a[0], maxlist(a[1:]))

a = list(map(int, input().split()))


def ind_maxlist(a):
    if len(a) == 1: 
        return 0

    if a[0] >= maxlist(a[1:]):
        return 0
    else:
        return 1 + ind_maxlist(a[1:])
    

print(ind_maxlist(a))