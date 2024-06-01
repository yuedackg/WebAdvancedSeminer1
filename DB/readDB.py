import sqlite3

con = sqlite3.connect( "example.db")
c = con.cursor()

for row  in c.execute( 'select * from users;'):
	print( row)

con.commit()
con.close()