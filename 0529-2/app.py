# ライブラリの準備
from flask import Flask, render_template, request
import sqlite3
DBname = "exampleDB.db"

# アプリケーションの初期化
app = Flask( __name__)

# ルート情報の設定。　パスと関数の割り付け
@app.route( "/")
def index():
	return render_template( "index.html" )

@app.route( "/entry/", methods=["POST", "GET"])
def entry() :
	if request.method == "POST":
		myuid = request.form.get( "uid")
		mypassword = request.form.get( "password")
		return render_template( "entry.html", uid=myuid,
									password= mypassword)
	else:
		return render_template( "index.html")

@app.route( "/initialize/" , methods=["POST"])
def init_db():

	con = sqlite3.connect( DBname)
	# テーブルの存在を確認する
	# strsql = '''select * from tusers'''
	c = con.cursor()
	# c.execute( strsql)
	# 結果から1行を取り出す。あればテーブルは存在する
	# result = c.fetchone()
	# if  not result:
		# テーブルがない
	strsql = '''CREATE TABLE IF NOT EXISTS  tusers( id text, password text)'''
	c.execute( strsql)
	strsql = '''delete from tusers '''
	c.execute(strsql)
	# strsql = '''CREATE TABLE IF NOT EXISTS  tusers( id text, password text)'''
	# c.execute( strsql)
	return render_template( "index.html" , msg="データベースの初期化を行いました")

@app.route( "/dumpTableTusers/", methods=["POST","GET"])
def dumpTable():
	con = sqlite3.connect( DBname)
	c= con.cursor()
	strSql = '''insert into tusers( id, password ) values( "dumy", "dummy")'''
	c.execute( strSql)	
	strSql = '''select * from tusers'''
	for row in c.execute( strSql ):
		print( row)
	return render_template( "index.html", msg="コンソールにテーブルの一覧出力を行いました。")

@app.route( "/addUser/", methods=["POST","GET"])
def addUser( ):
	if request.method=="POST":
		id = request.form.get( "uid")
		password = request.form.get("password")
		print( id, " -> ", password)	
		return render_template( "entry.html", uid=id, password=password)
	else:
		return render_template( "index.html", msg="POST以外のメソッドが使われました")

# 待ち受けポート番号8000で、デバッグモードで起動
if __name__ == "__main__":
	app.run( port=8000, debug=True)