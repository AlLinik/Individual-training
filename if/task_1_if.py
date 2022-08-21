# Вводится 3 целых числа, определить какое из них больше

a = int(input('Число №1: '))
b = int(input('Число №2: '))
c = int(input('Число №3: '))
if a > b and a > c:
    print('№1 наибольшее:', a)
elif b > a and b > c:
    print('№2 наибольшее:', b)
elif c > a and c > b:
    print('№3 наибольшее:', c)
elif a == b > c:
    print('№1=№2, наибольшие:', a,',',b)
elif a == c > b:
    print('№1=№3, наибольшие:', a,',', c)
elif b == c > a:
    print('№2=№3, наибольшие:', b,',', c)
else:
    print('Все числа =', a)