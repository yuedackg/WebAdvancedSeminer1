from flask import Flask, render_template, request
import sqlite3

app = Flask( __name__)

@app.route( "/")
def index():
	return render_template( "index.html", msg="")

@app.route( "/dbInit/")
def dbinit():
	return render_template( "dbinit.html")

@app.route( "/dbView/")
def dbview():
	return render_template( "dbview.html")

@app.route( "/dbAppend/")
def dbappend():
	return render_template( "dbappend.html")

@app.route( "/dbDelete/")
def dbdelete():
	return render_template( "dbdelete.html")

@app.route( "/dbUpdate/")
def dbupdate():
	return render_template( "dbupdate.html")

if __name__ == "__main__":
	app.run( port=8000, debug=True)
app.run()