def degree5(n):
    if n % 5 != 0:
        return -1
    if n == 5:
        return 1
    return 1 + degree5(n / 5)


n = int(input())
print(degree5(n))