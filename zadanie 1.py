def pownum(a, n):
    if n == 1:
        return a
    return a * pownum(a, n - 1)


a = int(input())
n = int(input())
print(pownum(a, n))