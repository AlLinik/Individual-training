# # else выполняется
# a = 2
# while a < 10:
#     print(a)
#     a = a + 1
# else:
#     print('Good')
#
# # else не выполняется
# a = 2
# while a < 10:
#     print(a)
#     a = a + 1
#     if a == 5:
#         break
# else:
#     print('Good')
# a = 1
#
# while a <= 10:
#     print('Квадрат числа', a, '=', a**2)
#     a = a + 1
# print('Теперь задание выполнено :-)')

# a = 5
# while a <= 55:
#     if a % 2 != 0:
#     # if a % 2 == 1:
#         print(a, end=' ')
#     a += 1
# n = int(input())
# i = 1
# while i <= n:
#     print(i * '*')
#     i = i + 1
# n = int(input())
# stars = '*'
# while len(stars) <= n:
#     print(stars)
#     stars += '*'
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# a = int(input())
# b = int(input())
# s = 0
# i = a
# while i <= b:
#     s += i
#     i += 1
# print(s)

# a = int(input())
# s = 0
# while a != 0:
#     s += a
#     a = int(input())
# print(s)

# for i in range(10):
#     print('*' * i)

a = (1, 2)
b = [1, 4]
c = 2
d = (a + tuple(b)) * c
print(d)