def numbers(x):
    print(x % 10)
    if x >= 10:
        numbers(x // 10)


x = int(input())
print(numbers(x))