import sqlite3

con = sqlite3.connect( "example3.db")
c = con.cursor()

c = con.execute( '''drop table users3''' )
c = con.execute( '''create table users3( id real, name text, password text)''')
c.execute( "insert into users3 values(1, '24000', 'thisisfirst' )")
c.execute( "insert into users3 values(2, '24002', 'thisissecound' )")
c.execute( "insert into users3 values(3, '24004', 'thisisthird' )")

con.commit()
con.close()

con = sqlite3.connect( "example3.db")
c = con.cursor()
for row in con.execute( "select * from users3"):
	print( row)

print( "case 2 ...")
con = sqlite3.connect( "example3.db")
c = con.cursor()
for row in con.execute( "select * from users3 where name=" + str(24002) ):
	print( row)
con.close()

