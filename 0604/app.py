from flask import Flask,render_template,request
import sqlite3

app = Flask( __name__)

@app.route( "/")
def index():
	return render_template( "index.html", msg="index() called.")

@app.route( "/view/", methods=["POST"])
def view():
	return render_template( "index.html", msg="view() called.")

@app.route( "/init/", methods=["POST"])
def init():
	return render_template( "index.html", msg="init() called.")

@app.route( "/append/", methods=["POST"])
def append():
	return render_template( "index.html", msg="append() called.")

if __name__ == "__main__":
	app.run( port=8000, debug=True)