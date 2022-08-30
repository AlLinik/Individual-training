## Вариант 1
# with open('file.txt', 'r') as file:   # "C:\\Users\\HP\\PycharmProjects\\Aliaksandr\\file\\file.txt"
#     counter = summa = 0
#     for line in file:
#         counter += 1
#         length_line = len(line)
#         for i in range(length_line):
#             if line[i].isdigit():
#                 num = int(line[i])
#                 summa += num
#                 if num < 3:
#                     print("Студент, чья оценка по группе меньше 3-х:", line)
#                 break
#     sred = summa / counter
#     print("Средний бал по группе:", sred)

with open('file.txt', 'r') as file:
    count_score = 0
    total_score = 0
    for i in file.readlines():
        i = i.strip("\n")
        count_score += 1
        stud_score = int(i[-1])
        total_score += stud_score
        if stud_score < 3:
            print(f'Студент с оценкой меньше "3" - {i[:-1]}')
print(f'Средний балл по классу - {total_score/count_score}')
