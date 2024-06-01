# filename: code-3.py
# DBを読み込む側
# sqlite3に接続するためのパッケージを取り込む
import sqlite3

con = sqlite3.connect( "sampleDB.db")
c = con.cursor()

strSqlSelect = '''select id, password from tusers'''
for row in con.execute( strSqlSelect ):
	print( row)
	
con.close()