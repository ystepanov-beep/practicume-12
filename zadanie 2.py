def count(n: int) -> int:
    """
    Рекурсивная функция, которая считает количество цифр в натуральном числе n.
    """
    if len(str(n)) == 1:
        return 1
    return 1 + count(n // 10) 


n = int(input())
print(count(n))
