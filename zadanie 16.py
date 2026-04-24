def ten_to_n(x, n):
    if x == 0:
        return ''
    return ten_to_n(x // n, n) + str(x % n)


x = int(input())
n = int(input())
print(ten_to_n(x, n))