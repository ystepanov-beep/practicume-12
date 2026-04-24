def odd_list(a, n):
    if n == 0:
        return []
    
    result = odd_list(a, n - 1)
    
    if a[n - 1] % 2 == 0:
        result.append(a[n - 1])
    
    return result


a = list(map(int, input().split()))
n = int(input())
print(odd_list(a, n))