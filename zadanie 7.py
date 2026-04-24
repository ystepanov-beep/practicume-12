def nod(a, b): 
    if a == b:
        return a
    if a > b:
        if a % b == 0:
            return b
        else:
            return nod(b, a % b)
    if b < a:
        if b % a == 0:
            return a
        else:
            return nod(a, b % a)
    

a = int(input())
b = int(input())
print(nod(a, b))