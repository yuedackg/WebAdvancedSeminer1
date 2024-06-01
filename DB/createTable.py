import sqlite3

con = sqlite3.connect( "example2.db")
c = con.cursor( )

c.execute('''create table users( id uid, name text, password text)''') 
con.commit()
con.close()
