import sqlite3

conn = sqlite3.connect('homework.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id_book INTEGER PRIMARY KEY AUTOINCREMENT, 
                  title VARCHAR(50), author VARCHAR(30), price DECIMAL(8, 2), amount INT)''')

cursor.execute('''INSERT INTO book(title, author, price, amount) 
                  VALUES('Python', 'Mark Lutz', '123456.78', '100')''')
conn.commit()

cursor.execute('''SELECT*FROM book''')
k = cursor.fetchall()
print(k)
cursor.close()

for i in k:
    i = list(i)
    h = 0
    print(' '.join(str(h) for h in i))



# book_5 = 'new string'
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_homework(col_5 TEXT)''')
# cursor.execute('''INSERT INTO tab_homework(col_5) VALUES(?)''', (book_5,))
# conn.commit()

# cursor_2 = conn.cursor()
# cursor_2.execute('''SELECT col_2 FROM tab_homework''')
# k_2 = cursor_2.fetchall()
