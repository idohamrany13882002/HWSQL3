import sqlite3

conn = sqlite3.connect("hw_solution.db")
conn.row_factory = sqlite3.Row

curser = conn.cursor()

curser.execute("CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);")
curser.execute("INSERT INTO shopping VALUES (1, 'Avokado', 5);")
curser.execute("INSERT INTO shopping VALUES (2, 'Milk', 2);")
curser.execute("INSERT INTO shopping VALUES (3, 'Bread', 3);")
curser.execute("INSERT INTO shopping VALUES (4, 'Chocolate', 8);")
curser.execute("INSERT INTO shopping VALUES (5, 'Bamba', 5);")
curser.execute("INSERT INTO shopping VALUES (6, 'Orange', 10);")
print([tuple(row) for row in (curser.execute("SELECT * FROM shopping;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT * FROM shopping WHERE amount > 5;").fetchall())])
curser.execute("DELETE from shopping WHERE name like 'Orange';")
curser.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba';")
curser.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk';")
print([tuple(row) for row in (curser.execute("SELECT COUNT(*)from shopping;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT * FROM shopping WHERE id > 0;").fetchall())])

conn.commit()
conn.close()