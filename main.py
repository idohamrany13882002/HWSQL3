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
# curser.execute("")
# curser.execute("")
# curser.execute("")
# curser.execute("")
# curser.execute("")
# curser.execute("")
# curser.execute("")