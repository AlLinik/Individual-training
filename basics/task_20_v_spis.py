
# print(a)

# for i in range(len(a)):
#
#     # for j in range(len(a[i])):
#                 print(a[i], end=' ')
#     # print()

# for i in a:
#     # for j in i:
#         print(i, end=' ')
#     # print()

# S = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         S += a[i][j]

# S = 0
# for i in a:
#     for j in i:
#         S += int(i in a)
# print(S)
# a.append(S)
# print(a)

print('Введите цифры или буквы через пробел в строку.')
a = input('\nВаша строка: ', ).split()
a[0] = [1, 2, 3]
a.append(sum(a[0]))
print(a)

