str_1 = input('Введите слово из букв ВЕРХНЕГО и нижнего регистров: ')

a = 'аАеЕёЁиИоОуУыЫэЭюЮяЯAaEeiIOouUyY'
pair_upp, pair_low, vow, cons = '', '', '', ''
count_pair_upp, count_pair_low, count_vow, count_cons = 0, 0, 0, 0

for i in range(1, len(str_1)):
    if str_1[i - 1].islower() and str_1[i].islower():
        count_pair_low += 1
        pair_low += str(i)
    elif str_1[i - 1].isupper() and str_1[i].isupper():
        count_pair_upp += 1
        pair_upp += str(i)
    print(str_1[i - 1], str_1[i])

for j in str_1:
    if j in a:
        count_vow += 1
        vow += j
    else:
        count_cons += 1
        cons += j
print(f'\nКоличество pair (UPP) - {count_pair_upp}. Количество pair (low) - {count_pair_low}.')
print(f'Количество гласных - {count_vow} ({vow}). Количество coгласных - {count_cons} ({cons}).')
print(f'Длина строки - {len(str_1)}.')



# a = input('Введите слово: ')
# a_1 = 'аАеЕёЁиИоОуУыЫэЭюЮяЯaAeEiIoOuUyY'
# b = 0
# c = 0
# b_1 = ''
# c_1 = ''
#
# for i in a:
#     if i in a_1:
#         b += 1
#         b_1 += i
#     else:
#         c += 1
#         c_1 += i
# print(b, b_1)
# print(c, c_1)
# print(len(a))
#
# low = 0
# upp = 0
# for j in range(1, len(a)):
#     print(a[j - 1], a[j])
#     if a[j - 1].islower() and a[j].islower():
#         low += 1
#     if a[j - 1].isupper() and a[j].isupper():
#         upp += 1
# print('сколько пар (стоят рядом) верхнего регистра:', upp)
# print('сколько пар (стоят рядом) нижнего регистра:', low)
# a = input('Введите слово: ')
# a_1 = 'аАеЕёЁиИоОуУыЫэЭюЮяЯAaEeiIOouUyY'
# x_1 = 0
# y_1 = 0
# x = ''
# y = ''
#
# for i in a:
#     if i in a_1:
#         x_1 += 1
#         x += i
#     else:
#         y_1 += 1
#         y += i
# print(x_1, x)
# print(y_1, y)
# print(len(a))

# if b[0].isupper() == b[1].isupper():
# if len(b) % 2 == 0:

# elif len(b) > 2:
# # elif len(b) % 2 == 0 or len(b) % 2 != 0:
# #     n = len(b) // 2
# #     b1 += n
# if i.isupper() == 2:
#     b += 1
#     print(b)
# elif b != '':
#     b = ''
# # if b != '':
# #     print(b)
# #     b = ''