from flask import Flask, render_template, request
import sqlite3

app = Flask( __name__)

DBname = 'mydbname.db'
TableName = 'TGAKUSEI'

@app.route( "/")
def index():
	return render_template( "index.html", msg="")

@app.route( "/dbInit/")
def dbinit():	
	return render_template( "dbinit.html")

@app.route( "/dbInitialize/")
def dbInitialize():
	strSQL = f'create table if not exists {TableName} ( id int , simei text, birthYear int)'
	con = sqlite3.connect( DBname)
	con.execute( strSQL)
	con.commit()
	con.close()
	return render_template( "dbinit.html", msg="テーブルを作成しました")

@app.route( "/dbInitializeInsertDummyData/")
def	dbInitializeInsertDummyData():
	strSQL = 'insert into {tableName} ( id, simei, birthYear ) values ( {myId}, "{mySimei}", {myBirthYear})'
	dummyData = [	[ 2000, "ueda", 2001],[ 2001, "suzuki", 2002],	[ 2003, "makisaka",2003]]
	message = ""
	try:
		conn=sqlite3.connect(DBname)	
		for line in dummyData:
			inSQL = strSQL.format( tableName=TableName, myId=line[0], mySimei=line[1], myBirthYear=line[2])
			conn.execute( inSQL)
		conn.commit()
		conn.close()
		message = "db更新成功"
	except sqlite3.DatabaseError:
		message = "db 更新失敗"
	return render_template( "dbinit.html", msg=message)

if __name__ == "__main__":
	app.run( port=8000, debug=True)
