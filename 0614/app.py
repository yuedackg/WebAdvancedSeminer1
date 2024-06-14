from flask import Flask,render_template,request
import sqlite3

DBname = "exampleDB.db"

app = Flask( __name__)

@app.route( "/")
def index():
	return render_template( "index.html")

@app.route( "/init/")
def	init():
	strSQL = '''if not exists tusers ( uid text, passwd text)'''
	strSQL2='''insert into tusers(uid, passwd) values( "24000", "ueda")"'''
	conn=sqlite3.connect(DBname)
	conn.execute(strSQL)
	conn.execute( strSQL2)
	conn.commit()
	conn.close()
	return render_template( "index.html", msg="データベースの初期化を行いました。")	

if __name__ == "__main__":
	app.run( port=8000, debug=True)

