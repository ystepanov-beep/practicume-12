def search(a, x):
    if len(a) == 0:
        return 0
    if x == a[0]:
        return 1
    return search(a[1:], x)


a = list(map(int, input().split()))
x = int(input())
print(search(a, x))