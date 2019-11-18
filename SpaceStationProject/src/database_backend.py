import sqlite3

DATABASE_PATH = r'C:\Users\princ\Desktop\DEV\SchoolProject\sample3.sqlite'

con = sqlite3.connect(DATABASE_PATH)

cur = con.cursor()

result = cur.execute("""SELECT "Country of Operator/Owner" FROM data""").fetchall()

result = set(result)
print(result)
