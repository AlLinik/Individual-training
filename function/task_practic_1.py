def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def exit_program():
    return exit()

while True:
    operation = input('Введите математическое действие (+, -, *, /) или 0 для ВЫХОДА: ')
    if operation == '0':
        print('Вы вышли из программы!')
        print(exit_program())
    elif operation not in ('+', '-', '*', '/'):
        print('ТОЛЬКО (+, -, *, /)')
        continue

    a = float(input('Введите первое вещественное число: '))
    b = float(input('Введите второе вещественное число: '))
    if operation == '+':
        print(f'Сумма чисел {a} и {b} равна {addition(a, b)}')
        print('')
        continue
    elif operation == '-':
        print(f'Разница чисел {a} и {b} равна {subtraction(a, b)}')
        continue
    elif operation == '*':
        print(f'Произведение чисел {a} и {b} равно {multiplication(a, b)}')
        continue
    elif operation == '/':
        if b == 0:
            print('Делить на 0 нельзя! Попробуйте еще раз...')
            continue
        else:
            print(f'Результат деления числа {a} на число {b} равно {division(a, b)}')
            continue

