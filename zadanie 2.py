def count(n):
    if len(str(n)) == 1:
        return 1
    return 1 + count(n // 10) 


n = int(input())
print(count(n))