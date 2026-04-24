def progress(a1, r, n):
    if n == 1:
        return a1
    return r + progress(a1, r, n - 1)


n = int(input())
a1 = int(input())
r = int(input())


def sum_progress(a1, r, n):
    if n == 1:
        return progress(a1, r, n)
    return a1 + r * (n - 1) + sum_progress(a1, r, n - 1)


print(sum_progress(a1, r, n))