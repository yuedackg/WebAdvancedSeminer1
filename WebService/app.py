from flask import Flask, render_template, request
import sqlite3

app = Flask( __name__)

@app.route( "/")
def index():
	return render_template( "index.html", msg="")

@app.route( "/dbInit/")
def dbinit():
	
	return render_template( "dbinit.html")


if __name__ == "__main__":
	app.run( port=8000, debug=True)
app.run()