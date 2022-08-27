# Если введено больше или меньше 7 символов - добавляем цикл после строки:
#     if len(a) > 7 or len(a) < 7:
#         print('Вы ввели не семизначное число! Попробуйте еще раз!')
#         exit()

# # ВАРИАНТ 1
# a = input('Введите семизначное число: ')
# a_1 = []
# b = 0
# c = 0
# for i in a:
#     if i not in a_1:
#         a_1.append(int(i))
# for j in a:
#     if int(j) % 2 == 0:
#         b += 1
#     else:
#         c += 1
# if b > c:
#     print(sum(a_1))
# else:
#     print(a_1[0] * a_1[2] * a_1[5])

# # ВАРИАНТ 2
a = input('Введите семизначное число: ')
if len(a) > 7 or len(a) < 7:
    print('Вы ввели не семизначное число! Попробуйте еще раз!')
    exit()
b = 0
c = 0
for i in a:
    if int(i) % 2 == 0:
        b += 1
    else:
        c += 1
if b > c:
    print('Сумма всех чисел =', int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) + int(a[4]) + int(a[5]) + int(a[6]))
else:
    print('Произведение 1, 3 и 6 чисел =', int(a[0]) * int(a[2]) * int(a[5]))
