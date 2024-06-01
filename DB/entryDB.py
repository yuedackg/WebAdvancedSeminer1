import sqlite3

con = sqlite3.connect( "example2.db")
c = con.cursor()

c.execute("insert into users values ( 1, '24000', 'hello' )")

con.commit()
con.close()
