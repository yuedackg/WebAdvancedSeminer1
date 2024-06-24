from flask import Flask, render_template, request
import sqlite3

app = Flask( __name__)

DBname = 'mydbname.db'
TableName = 'TGAKUSEI'
REQUEST_TYPE="POST"

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

@app.route( "/dbView/")
def dbViewA():
	print( "dbViewA()...")
	message=""
	lines=[]
	strSQL = 'select * from {TableName} '

	try:
		conn = sqlite3.connect( DBname)
		cur = conn.cursor()
		s =  strSQL.format( TableName=TableName)
		print( "SQL:", s )
		cur.execute(s)
		for line in cur.fetchall():
			print(line)
			item = []
			for i in line :
				item.append( i)
			lines.append (item)			
		conn.close()
	except sqlite3.DatabaseError as err :
		message="データベースからの取り出しに失敗しました。"

	return render_template( "dbview.html", msg=message, lines=lines)
	

# @app.route( "/dbView/", methods=["post"])
# def dbView():
# 	message=""
# 	lines=[]
# 	strSQL = 'select * from {TableName} '
# 	if request.method==REQUEST_TYPE:
# 		try:
# 			conn = sqlite3.connect( DBname)
# 			cur = conn.cursor()
# 			cur.execute( strSQL.format( TableName=TableName))
# 			for line in cur.fetchall():
# 				print(line)
# 				lines.append( line)
# 			conn.close()
# 		except sqlite3.DatabaseError as err :
# 			message="データベースからの取り出しに失敗しました。"
# 	return render_template( "dbview.html", msg=message)
	
@app.route( "/dbAppend/")
def dbAppendA():
	return render_template( "dbappend.html")

@app.route( "/dbAppend/", methods=["POST"])
def dbAppend():
	print( "in dbAppend()...")
	message=""
	inNo=0
	strSimei=""
	inYear=0
	if request.method==REQUEST_TYPE:
		try:
			inNo = int( request.form.get( "no"))
			inYear = int( request.form.get( "birthY"))
		except ValueError:
			message="数字が正しく入力されていない"
		strSimei = request.form.get( "simei")
		print( inNo, strSimei, inYear, message)
		strSQL = "select * from {TableName} where id={myId}"
		strSQL = strSQL.format( TableName=TableName, myId=inNo)
		try:
			conn = sqlite3.connect( DBname)
			cur=conn.cursor()
			cur.execute( strSQL)
			if cur.fetchone() == None :
				print( "dataが存在しないために登録")
				try:
					strSQL='insert into {myTable} ( id, simei, birthYear ) values ( {myId}, "{mySimei}", {myYear}) '
					strSQL = strSQL.format(myTable=TableName,myId=inNo, mySimei=strSimei, myYear=inYear)
					conn.execute( strSQL)
					message="データの登録完了"
				except sqlite3.DatabaseError:
					message="データの追加中にエラーが発生しました"
					print(message)
			else:
				message="データが存在するために登録しない"
				print( message)
			conn.commit()
			conn.close()
		except sqlite3.DatabaseError as dberr:
			print( "データベース操作中にエラーが発生しました。")
			print( strSQL)
			print( dberr)
	return render_template( "dbappend.html" , msg=message)

@app.route( "/dbDelete/")
def dbDeleteA():
	return render_template( "dbdelete.html")

@app.route( "/dbDelete/", methods=["POST"])
def dbDelete():
	if request.method == REQUEST_TYPE:
		print( request.form)
	return render_template( "dbdelete.html")


if __name__ == "__main__":
	app.run( port=8000, debug=True)
