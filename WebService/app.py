from flask import Flask, render_template, request
import sqlite3

app = Flask( __name__)
DBname = "myDatabase.db"

@app.route( "/")
def index():
	return render_template( "index.html", msg="")

@app.route( "/dbInit/"	)
def dbinit():
	return render_template( "dbinit.html", msg="dbが作られました。")

@app.route( "/doInit/", methods=["POST"])
def doInit():
	print( "db initialize...")
	# SQLを作る	
	strSQL = '''create table if not exists TGAKUSEI( gakusekiNo int, simei text , birthYear int )'''
	strSQL2 = '''insert into TGAKUSEI( gakusekiNo, simei, birthYear) values ( 20001, "ueda", 2000)'''
	strSQL3 = '''insert into TGAKUSEI( gakusekiNo, simei, birthYear) values ( 20002, "suzukki", 1970)'''
	
	# 通信を確認
	if request.method=="POST":
		# SQLite3に接続する
		conn = sqlite3.connect( DBname )
		conn.execute( strSQL)				# SQLを実行する
		conn.execute( strSQL2)
		conn.execute( strSQL3)
		conn.commit()						# commit()する
		conn.close()						# 閉じる
		return render_template( "index.html", msg="データベースを作成しました。")
	return render_template( "index.html", msg="作成失敗")


@app.route( "/dbView/" )
def dbView():
	# 通信があるかの確認　→Aタグを押されてジャンプしてくるので、この判断は不要
	# フォームから送られてきたデータを変数に移動　→今回はない
	# SQL文の作成
	strSQL = '''select * from TGAKUSEI '''
	
	# SQLite3に接続する.　接続の変数はconn
	conn = sqlite3.connect( DBname)

	# カーソル（Cursor()）を作る。作られたカーソルはcur。
	cur = conn.cursor()

	# SQLを実行する
	ret = cur.execute( strSQL)
	
	# 最終的な結果を格納する空リストを作る。変数名はresult。
	result = []

	# 繰り返しfor分を使って、要素を一つずつ取り出す
	for line in ret:

	# レコードを格納する空リストを作る。変数名はrecord
		record = []

	# 学籍番号、名前、年齢を リストrecordに格納する
		record.append(line[0])
		record.append(line[1])
		record.append( line[2])

	# 作成したリストrecordをリストresultに格納する
		result.append( record)

	# （すべての繰り返しを終えて、）リストが空なら、index.htmlにジャンプ
	# リストresultが空でないなら、vewDB.htmlにジャンプする
	# print( "result>", result)
	if result == None :
		return render_template( "index.html", msg="テーブルにデータがない")
	else:
		return render_template( "viewDB.html", data=result)
	
	# ここまで終わったら例外処理についての対処を行う。
	# 例外は、DatabaseErrorでまとめるか、OperationalErrorで詳細にとるか判断




if __name__ == "__main__":
	app.run( port=8000, debug=True)
app.run()