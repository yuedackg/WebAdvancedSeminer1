# Python DB
# initialize for DB table.
import sqlite3

con = sqlite3.connect( "example.db")
c = con.cursor()

c.execute( '''CREATE TABLE users(id real, name text, birtyday text)''')
c.execute("INSERT INTO users VALUES (1, '煌木 太郎', '2001-01-01')")
con.commit()
con.close()						