f = open("text.txt_1", 'r')   # 'r' - для чтения
#print(f.readline())   # выводит первую строку text.txt
#print(f.read())   # выводит все строки text.txt как они записаны в text.txt
print(f.readlines())   # выводит список всех слов text.txt

# Aliaksandr Linik
# 25.12.1986
# Zhabinka
# Zarechnaja
# 10A
# 38

for i in f:
    print(i)

# print(*f)
# f.close()   # обязательно при open()

# f = open("text.txt", 'w')   # меняем на 'w' - для записи (стирает текст до этого)
# f.write('Mark\nDavid')

# f = open("text.txt", 'a')   # меняем на 'a' - дозапись к концу файла (сохраняет текст до этого)
# f.write('\nMark\nDavid\nLidzija')

# f = open("text.txt", 'w')   # меняем на 'w' - для записи (стирает текст до этого)
# list = ['Linik', '25.12.1986', 'Aliaksandr']
# for i in list:
#     f.write(i + '\n')
#     print(i)

# with open('text.txt_1', 'r') as f:   # with сама закрывает файл (не вводим f.close())
#     # f.write('Hello\n')
#     print(f.readlines())   # меняем на 'r', иначе будет ошибка


