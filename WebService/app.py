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
			sql = s.format( TableName, random.randint( 22900, 22999), "dummy", random.randint( 2000, 2003) )
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

@app.route( "/doappend/", methods=["post"])
def doAppend():
	message=""
	inNo=0
	strSimei=""
	inYear=""

	if request.method == REQUEST_TYPE:
		try:
			inNo=int(request.form.get( "no"))
			inYear = int (request.form.get( "birthY"))
		except ValueError:
			message="正しく数字が入力されていない"
		strSimei = request.form.get("simei")
		strSql = 'select * from {} where id = {} '.format( TableName, inNo)
		try:
			con=sqlite3.connect(DBname)
			cur =con .cursor()
			if cur.fetchone() == None:
				print( "データが存在し泣いたため、登録OK")
				try:
					strSQL = 'insert into {} values( {}, "{}", {}) '.format( TableName, inNo, strSimei, inYear)
					print( "strSQL: {}".format( strSQL))
					con.execute( strSQL)
					message="データの登録完了"
				except sqlite3.DatabaseError:
					message="データの追加中にエラーが発生しました"
			else:
				message="データが存在するために登録できない"
			con.commit()
			con.close()
		except sqlite3.DatabaseError:
			message="データベースにエラーが発生した"
	print( "message:{}".format( message))
	return render_template( "dbappend.html", msg = message)

def DeleteMain():
	strSQL = 'select * from {} '.format( TableName)
	con = sqlite3.connect( DBname)
	cur = con.cursor()
	cur.execute( strSQL)
	lines=[]
	for item in cur.fetchall():		# テーブルから1行ずつ処理
		line = [] 
		for i in item :
			line.append(i)
			print( line)
		lines.append( line)
	print( lines)
	con.close()
	return lines

@app.route( "/dbDelete/")
def dbDelete0():
	lines = DeleteMain()
	return render_template( "dbdelete.html", msg="", lines=lines)


@app.route( "/dbDelete/",methods=["post"])
def dbDelete():
	if request.method == REQUEST_TYPE:
		rets = request.form.to_dict()  # 削除のチェックが入ったデータを受取る
		print( rets)					# 状態を確認

		con =sqlite3.connect( DBname)	# データベースにつなげる
		for item in rets:				# チェックボックスのデータを取出す
			print ( "item : " , item ) 	# 1組ずつ取り出してみる⇒検討
										# SQLを使いまわしできないか検討
										# forで繰り返せないか検討
			strSQL='delete from {} where gakusekiNo = {}'.format( TableName, item)
			con.execute( strSQL)		# SQLの実行
		con.commit()					# commit()の位置で
										# 　DBの反映のタイミングが決まる
		con.close()
	lines = DeleteMain()				# 現在のテーブルの状態を取得する
										# メッセージを「deleted!」
										# テーブルの状態のリストlines埋める
	return render_template( "dbdelete.html", msg="deleted!", lines=lines)

def getList():
	statement = 'select * from {} '.format( TableName)
	list = []

	con = sqlite3.connect( DBname)
	cur = con.cursor()
	cur.execute( statement)

	for item in cur.fetchall():
		line = []
		for it in item :
			line.append( it)
		list.append( line)
	print( list)
	return list


@app.route( "/dbUpdate/")
def dbupdate():
	list = getList()
	return render_template( "dbupdate.html", msg="", lines=list)

@app.route( "/dbUpdate/", methods=[REQUEST_TYPE])
def dbupdate2():
	DB_COL_NAME = 	[ "gakusekiNo", "simei",	"birthYear"]
	HTML_COL_NAME = [ "namae", 		"simei", 	"year"]
	strSQL_base = 'update {} set {}="{}", {}={} where {}={}'
	strSQL_check = 'select * from {} where {}={}'
	message=""
	if request.method==REQUEST_TYPE:
		inNo 	= request.form.get( HTML_COL_NAME[0])
		inSimei = request.form.get( HTML_COL_NAME[1])
		inYear 	= request.form.get( HTML_COL_NAME[2])
		strSQL0 = strSQL_check.format( TableName, DB_COL_NAME[0], inNo)
		print( "strSQL0:", strSQL0)
		strSQL = strSQL_base.format( TableName, DB_COL_NAME[1], inSimei, DB_COL_NAME[2],inYear,DB_COL_NAME[0],inNo)
		print( "strSQL: ", strSQL)
		try:
			con = sqlite3.connect( DBname)
			cur = con.cursor()
			cur.execute( strSQL0)
			if cur.fetchone()==None:
				message = "該当するデータが存在しない"
				print( message)
			else:
				con.execute( strSQL)
				con.commit()
				message="データベースの更新が完了しました"
				con.close()
		except sqlite3.DatabaseError :
			message =  "databsaseの更新ができません"
	list = getList()
	return render_template( "dbupdate.html", msg=message, lines=list)

if __name__ == "__main__":
	app.run( port=8000, debug=True)



