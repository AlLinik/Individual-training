# def factorial(n):
#     if n != 0:
#         return n * factorial(n - 1)
#     else:
# #         return 1
#
# def factorial_2(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial_2(n - 1)
# #print(factorial(3))
# print(factorial_2(5))3

import random

my_list = [random.randint(0, 100) for i in range(10)]
print('\nНО ВЕДЬ ТАК ПРОЩЕ:-) -', sum(my_list))

def num_adding(my_list):

    if len(my_list) == 0:
        return 0
    else:
        return my_list[0] + num_adding(my_list[1:])

print('\nСуммирование с помощью рекурсивной функции -', num_adding(my_list))

