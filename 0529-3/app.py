from flask import Flask,render_template, request
import sqlite3

DBname = "exampleDB.db"

app = Flask( __name__)

def processing_index():
	strsql = '''create table if not exists tusers( id, password)'''
	con =sqlite3.connect( DBname)
	con.execute( strsql)
	con.commit()
	con.close()

def processing_showDB():
	strSql = "select * from tusers"
	con =sqlite3.connect( DBname)
	c = con.cursor()
	for row in c.execute( strSql):
		print( row )

def processing_entry():
	if request.method == "POST":
		myid = request.form.get( "uid")
		mypassword = request.form.get( "password")
		con = sqlite3.connect( DBname)
		sqlStr = '''insert into tusers( id, password) values( " '''+ myid + ''' "," ''' + mypassword +'''") '''
		print( ">> "+ sqlStr)
		con.execute( sqlStr)
		con.commit()
		con.close()

@app.route( "/")
def index():
	processing_index()
	return render_template( "index.html", msg="index.html")

@app.route( "/showDB/", methods=["POST","GET"] )
def showDB():
	processing_showDB()
	return render_template( "index.html", msg="showDB")

@app.route( "/initDB/", methods=["POST","GET"])
def initDB():
	return render_template( "index.html", msg="initDB")

@app.route( "/entry/", methods=["POST","GET"])
def entry():
	processing_entry()

	return render_template( "index.html", msg="entry")

if __name__ == "__main__":
	app.run( port=8000, debug=True)
