file_input = open('input.txt', 'w')
my_list = ['155', '56']
for i in my_list:
    file_input.write(i + ' ')
file_input.close()

file_input = open('input.txt', 'r')
for j in file_input:
    num = j.split()
    print('Список элементов input.txt -', num)
    num_1 = int(num[0])
    num_2 = int(num[1])
    print(f'Элемент №1 - {num_1}; Элемент №2 - {num_2}')
file_input.close()

with open('output.txt', 'w') as file_output:
    file_output.write(str(num_1 - num_2))

x = open('input.txt', 'r')
print('"input.txt" -', x.readlines())
y = open('output.txt', 'r')
print('"output.txt" -', y.readlines())

