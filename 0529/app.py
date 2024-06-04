# filename: app.py
# パッケージの読み込み
# Flask：Webアプリのフレームワーク
# render_template：HTMLの中に文字列を埋め込むパッケージ
# request：　通信関係を扱う
from flask import Flask, render_template,request
# sqlite3：データベース
import sqlite3

# データベースの名前を設定　複数個所で扱うため
DBname = "exampleDB.db"

app = Flask( __name__)

@app.route( "/")
def index():
	return render_template( "index.html")

# POSTで送られてきた情報をentry.htmlの中に埋め込む
@app.route( "/entry/", methods=["POST", "GET"])
def entry():
	if request.method == "POST":
		uid = request.form.get( "uid")
		password = request.form.get( "password")
		return render_template( "entry.html" , uid=uid, password=password)
	
	else :
		# POST以外の通信は、index.html（トップページ）
		return render_template( "index.html")

@app.route( "/initializeDB/", methods=["POST","GET"])
def initDB():
	# データベースの初期化は、最初にテーブルがあることが前提
	con = sqlite3.connect( DBname)
	cursor = con.cursor()
	strSql = '''select id from tusers'''
	cursor.execute( strSql)
	# 以上の操作で、テーブルがあれば1件以上読み出すことが出来る
	# 以下の命令で、1行だけ取り出すか試す（True/False）
	result = cursor.fetchone()
	if not  result:
		# 1行も読めなければ、テーブルをつくる
		strSql = '''create table tusers( id text, password text)'''
		con.execute( strSql)

	# データを追加する
	strSql = '''insert into tusers( id, password) values( "2000", "ueda")'''
	con.execute( strSql)

	# データをファイルに反映
	con.commit()
	con.close()

	# トップページに移動
	return render_template( "index.html", msg="初期化されました")

@app.route( "/readDB/", methods=["POST", "GET"])
def readDB():
	# 未作成
	return render_template( "index.html" ,msg="データを読み込みます")

if __name__ == "__main__":
	app.run( port=8000, debug=True)

