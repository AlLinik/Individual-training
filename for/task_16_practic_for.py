# Пользователь вводит десятизначное число.
# Программа выводит все четные числа в этом числе.

# a = input('Введите десятизначное число: ')
# c = ''
#
# for i in a:
#     if int(i) % 2 == 0:
#         c = c + i
#
# print('Четные числа из Вашего числа: ', c)

a = input('Введите трехзначное число: ')
b = 0
for i in a:
    b = b + int(i)

print('Сумма чисел Вашего числа:', b)
