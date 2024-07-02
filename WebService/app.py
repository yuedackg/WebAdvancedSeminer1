from flask import Flask, render_template, request
import sqlite3
import random

app = Flask( __name__)
DBname = "myDatabase.db"
TableName = "TGAKUSEI"
REQUEST_TYPE = "POST"
RECIEVE_METHOD_TYPE = "post"

@app.route( "/")
def index():
	return render_template( "index.html", msg="")

@app.route( "/dbInit/")
def dbinit():
	return render_template( "dbinit.html", msg="")

@app.route( "/doInit/", methods=[RECIEVE_METHOD_TYPE])
def dbInitialize():
	print( "db initialize...")
	message = ""
	strSQL = 'create table if not exists {} ( gakusekiNo int primary key , simei text , birthYear int)'
	if request.method == REQUEST_TYPE:
		con = sqlite3.connect( DBname)
		con.execute( strSQL.format( TableName))
		s='insert into {} ( gakusekiNo, simei, birthYear) values ( {}, "{}", {}) '
		for k in range(5):
			sql = s.format( TableName, random.randint( 23900, 23999), "dummy", random.randint( 2000, 2003) )
			con.execute( sql)
		con.commit()
		con.close()
		message = "データベースを作成しました"

	return render_template( "index.html", msg=message)

@app.route( "/dbView/")
def dbView():
	print( "dbView()...")
	message=""
	lines=[]
	strSQL = 'select * from {TableName}'
	

	try:
		con = sqlite3.connect( DBname)
		cur = con.cursor()
		s = strSQL.format( TableName=TableName)
		cur.execute( s)
		for line  in cur.fetchall():
			item =[] 
			for i in line:
				item.append( i)
			lines.append( item)
		con.close()
	except sqlite3.DatabaseError:
		message="データベースからの取り出しに失敗しました。"

	return render_template("dbview.html", msg=message, lines=lines)

@app.route( "/dbAppend/")
def dbAppend():
	return render_template( "dbappend.html")

@app.route( "/dbDelete/")
def dbDelete():
	return render_template( "dbdelete.html")

@app.route( "/dbUpdate/")
def dbupdate():
	return render_template( "dbupdate.html")

if __name__ == "__main__":
	app.run( port=8000, debug=True)
app.run()