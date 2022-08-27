C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
print('Сумма элементов C_1 =', sum(C_1))
print('Сумма элементов C_2 =', sum(C_2))

if sum(C_1) > sum(C_2):
    print('Сумма больше в кортеже C_1')
elif sum(C_2) > sum(C_1):
    print('Сумма больше в кортеже C_2')
else:
    print('C_1 = C_2')

print(f'Min C_1 ({min(C_1)}) - индекс {C_1.index(min(C_1))}', f'\nMax C_1 ({max(C_1)}) - индекс {C_1.index(max(C_1))}')
print(f'Min C_2 ({min(C_2)}) - индекс {C_2.index(min(C_2))}', f'\nMax C_2 ({max(C_2)}) - индекс {C_2.index(max(C_2))}')


