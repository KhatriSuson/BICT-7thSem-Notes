import sqlite3
conn = sqlite3.connect('example.db')
cursor=conn.cursor()
cursor.execute('Create table colz(id int, name varchar(40))')
cursor.execute('Insert into colz values(1, "John")')
cursor.execute('Insert into colz values(2, "Jane")')
cursor.execute('Insert into colz values(3, "Jim")')
cursor.execute('Select * from colz')
print(cursor.fetchall())

