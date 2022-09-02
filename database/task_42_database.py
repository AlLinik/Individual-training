import sqlite3

conn_string = sqlite3.connect('database_string.db')
cursor_string = conn_string.cursor()
cursor_string.execute('''CREATE TABLE IF NOT EXISTS tab_string(id_str INTEGER PRIMARY KEY AUTOINCREMENT, col TEXT)''')
conn_string.commit()

conn_integer = sqlite3.connect('database_integer.db')
cursor_integer = conn_integer.cursor()
cursor_integer.execute('''CREATE TABLE IF NOT EXISTS tab_integer(id_int INTEGER PRIMARY KEY AUTOINCREMENT, col INT)''')
conn_integer.commit()

my_list = [1, 2, 3, 'string', 'integer', 'database']
for i in my_list:
    if type(i) == str:
        cursor_string.execute('''INSERT INTO tab_string(col) VALUES(?)''', (i,))
        conn_string.commit()
        cursor_integer.execute('''INSERT INTO tab_integer(col) VALUES(?)''', (len(i),))
        conn_integer.commit()
    elif type(i) == int:
        if i % 2 == 0:
            cursor_integer.execute('''INSERT INTO tab_integer(col) VALUES(?)''', (i,))
            conn_integer.commit()
        else:
            cursor_string.execute('''INSERT INTO tab_string(col) VALUES(?)''', ('нечетное',))
            conn_string.commit()

cursor_string.execute('''SELECT*FROM tab_string''')
cursor_integer.execute('''SELECT*FROM tab_integer''')
k_string = cursor_string.fetchall()
k_integer = cursor_integer.fetchall()
print(k_string)
print(k_integer)
print(len(k_integer))
if len(k_integer) > 5:
    cursor_string.execute('''DELETE FROM tab_string WHERE id_str = 1''')
    conn_string.commit()
else:
    cursor_string.execute('''UPDATE tab_string SET col = 'hello' WHERE id_str = 1''')
    conn_string.commit()

cursor_string.execute('''SELECT*FROM tab_string''')
k_string = cursor_string.fetchall()
print(k_string)

