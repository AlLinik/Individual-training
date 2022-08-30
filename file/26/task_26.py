# if not os.path.isdir('test_1.txt'):
#     os.mkdir('test_1.txt')
# if not os.path.isdir('test_2.txt'):
#     os.mkdir('test_2.txt')
# if not os.path.isdir('test_3.txt'):
#     os.mkdir('test_3.txt')
import os
os.chdir('..')
os.chdir('..')
os.chdir('..')
os.chdir('..')
os.chdir('Desktop')
if not os.path.isdir('task_26'):
    os.mkdir('task_26')
os.chdir('task_26')
with open('test_1.txt', 'w') as task_26:
    task_26.write('')
with open('test_2.txt', 'w') as task_26:
    task_26.write('')
with open('test_3.txt', 'w') as task_26:
    task_26.write('')
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir('..')
os.rmdir('task_26')
print(os.getcwd())
#   print(os.path.abspath('text.txt')) - возвращает абсолютный путь до файла указанного в аргументе
