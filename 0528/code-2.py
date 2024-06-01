# filename: code-2.py
# DBをつくる側
import sqlite3

con = sqlite3.connect( "sampleDB.db")
c = con.cursor()

strsql= '''create table tusers( id text, password text )'''
strsql0 = ''' drop table tusers'''
con.execute( strsql0)
con.execute( strsql)

strSqlInsert1 = '''insert  into  tusers ( id,      password)  values ( "23000", "Ckg23000!" ) '''
con.execute( strSqlInsert1)

strSqlInsert2 = '''insert  into  tusers ( id,      password)  values ( "23001", "Ckg23001!" ) '''
con.execute( strSqlInsert2)

strSqlInsert3 = '''insert  into  tusers ( id,      password)  values ( "ueda", "Ckg23002!" ) '''
con.execute( strSqlInsert3)
con.commit()
con.close()
