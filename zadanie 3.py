def progress(a1, r, n):
    if n == 1:
        return a1
    return r + progress(a1, r, n - 1)


n = int(input())
a1 = int(input())
r = int(input())
print(progress(a1, r, n))