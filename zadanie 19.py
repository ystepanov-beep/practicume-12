def count(a, b):
    if a == b:
        return 1
    if a > b:
        return 1 + count(a - b, b)
    else:
        return 1 + count(a, b - a)
    

a = int(input())
b = int(input())
print(count(a, b))