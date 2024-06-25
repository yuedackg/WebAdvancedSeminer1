from flask import Flask, render_template, request
import sqlite3

app = Flask( __name__)

DBname = 'mydbname.db'
TableName = 'TGAKUSEI'
REQUEST_TYPE="POST"

@app.route( "/")
def index():
	return render_template( "index.html", msg="")




if __name__ == "__main__":
	app.run( port=8000, debug=True)
