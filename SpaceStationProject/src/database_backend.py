import sqlite3

DATABASE_PATH = r'sample3.sqlite'

con = sqlite3.connect(DATABASE_PATH)

cur = con.cursor()

result = cur.execute("""SELECT "Country of Operator/Owner" FROM Лист1""").fetchall()

result = set(result)
print(result)
