# ПРИМЕРЫ РЕКУРСИВНОЙ ФУНКЦИИ ФАКТОРИАЛА:

def factorial1(n):
    if n == 1:
        return n
    else:
        return n * factorial1(n - 1)


def factorial2(n):
    if n != 0:
        return n * factorial2(n - 1)
    else:
        return 1


print(factorial1(8))
print(factorial2(0))


# ПРИМЕР ИТЕРАТИВНОЙ ФУНКЦИИ ФАКТОРИАЛА:

def iterative_factorial(n):
    factorial = 1
    if n < 0:
        print('Факториал не вычисляется для отрицательных чисел')
    else:
        for i in range(1, n + 1):
            factorial *= i
        print(f'Факториал числа {n} равен {factorial}')


iterative_factorial(5)