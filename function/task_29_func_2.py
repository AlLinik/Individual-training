# def is_prime(a):
#     if a % 2 == 0:
#         return a == 2
#     d = 3
#     while d * d <= a and a % d != 0:
#         d += 2
#     return d * d > a
#
# print(is_prime(int(input("Enter a number: "))))
def is_prime(number):
    if number == 0 or number == 1:
        return '0 и 1 не являются простыми числами!'
    if number > 1000:
        return 'Вы ввели число больше 1000!'
    for i in range(2, (number // 2) + 1):   # int(number ** 0.5 + 1)
        if number % i == 0:
            return False
    return True
print(is_prime(int(input('Введите число от 2 до 1000: '))))
print(is_prime(int(input('Введите число от 2 до 1000: '))))
print(is_prime(int(input('Введите число от 2 до 1000: '))))
print(is_prime(int(input('Введите число от 2 до 1000: '))))
print(is_prime(int(input('Введите число от 2 до 1000: '))))