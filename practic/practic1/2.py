# # Подсчет чисел в списке
# import random
# m = int(input('Количество чисел для генератора: '))
# n = int(input('Введите количество чисел для списка: '))
# n_1 = int(input('Введите цифру от 0 до 9: '))
# a = [random.randint(0, m) for i in range(n)]
# print('Список рандомных чисел: ', a)
# b = 0
# for i in a:
#     if i == n_1:
#         b += 1
# print(f'Количество повторений цифры "{n_1}" в списке = {b}')
# print(a.count(n_1))   # как вариант
# Подсчет цифр в списке
import random
m = int(input('Количество чисел для генератора: '))
n = int(input('Количество чисел для списка: '))
n_1 = input('Введите цифру от 0 до 9: ')
a = [random.randint(0, m) for i in range(n)]
s = ''.join(str(a))
print('Список рандомных чисел: ', s)
b = 0
for i in s:
    if i == n_1:
        b += 1
print(f'Количество повторений цифры "{n_1}" в списке = {b}')
