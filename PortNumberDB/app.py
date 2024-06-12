from flask import Flask, render_template, request
import sqlite3

app = Flask( __name__ )
DBname = "exampleDataBase.db"

@app.route( "/")
def index():
    return render_template( "index.html")

@app.route("/view/" , methods=["post"])
def view():
    if request.method=="POST":
        strSQL = '''select * from tusers'''
        try:
            conn = sqlite3.connect( DBname)
            cur = conn.cursor()
            cur.execute( strSQL)
            # conn.commit()
            # conn.close()
        except:
            print("OperationalError")
    return render_template( "view.html",lines = cur.fetchall() )

@app.route( "/append/", methods=["post"])
def append():
    return render_template( "append.html")

@app.route( "/delete/", methods=["post"])
def delete():
    return render_template( "delete.html")
@app.route( "/init/", methods=["post"])
def init():
    return render_template( "init.html")
if __name__ == "__main__" :
    app.run( port=8000, debug=True)
