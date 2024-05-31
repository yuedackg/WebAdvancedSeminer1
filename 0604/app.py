from flask import Flask,render_template,request
import sqlite3
import os
import sys

app = Flask( __name__)

DBname = "exampleDB.db"


@app.route( "/")
def index():
	if not os.path.isfile( DBname):
		print( "DBファイルが存在しません")
		# init()
		return render_template( "index.html", msg="DBファイルが存在しません")
	else:
		conn = sqlite3.connect( DBname)
		cur = conn.cursor()

		strsql = '''SELECT COUNT(*) FROM sqlite_master WHERE TYPE="table" AND name="tusers"''' 
		cur.execute( strsql)
		if cur.fetchone() != (0,) :
			print( "データが存在します。")
			for row in cur.execute( strsql):
				print( row)
			return render_template( "index.html", msg="データが存在します。")
		else:
			print( "テーブル内のデータが存在しません。")
			return render_template( "index.html", msg="データが存在しません")
	

def createDBFile():
	if not os.path.isfile( DBname) :
		con = sqlite3.connect( DBname)
		con.execute( '''CREATE TABLE IF NOT EXISTS
		 tusers(id text, password text) ''')
		con.commit()
		con.close()

# /view/　に対して、POSTされたときは、view()メソッドを実行する
@app.route( "/view/", methods=["POST"])
def view():
	# index.htmlのファイルの {{msg}} 部分に文字列を埋め込む
	return render_template( "index.html", msg="view() called.")

@app.route( "/init/", methods=["POST"])
def init():
	createDBFile()
	return render_template( "index.html", msg="init() called.")

@app.route( "/append/", methods=["POST"])
def append():
	strsql = '''insert into tusers( id, password) values( "hello", "world") '''
	con = sqlite3.connect( DBname)
	c = con.cursor()
	c.execute( strsql)
	con.commit()
	con.close()
	return render_template( "index.html", msg="append() called.")

if __name__ == "__main__":
	app.run( port=8000, debug=True)