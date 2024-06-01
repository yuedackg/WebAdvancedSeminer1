# filename : app.py
from flask import Flask,render_template,request
import flask, sqlite3

app = Flask( __name__, static_folder=".", static_url_path="")

@app.route( "/")
def index():
	return app.send_static_file( "index.html")

@app.route( "/initialize")
def init_db():
	print( "/initialize")
	con = sqlite3.connect( "system.db")
	# strDropTable = "drop table tusers"
	# con.execute( strDropTable)
	strCreateTable = "create table tusers(uid int, password text)"
	con.execute( strCreateTable)
	con.commit()
	con.close()	
	return app.send_static_file("")

@app.route( "/entry", methods = [ "GET", "POST"]  )
def entry():
	print( "entry() method called.")
	if request.method == "POST":
		print( "> POST...")
		return render_template("form-complete.html")

	else:
		print( "> others.")
		return render_template( "form.html")
	return render_template( "form.html")

if __name__ == "__main__":
	app.run( port=8080, debug=True)
