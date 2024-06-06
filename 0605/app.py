from flask import Flask, render_template, request

import sqlite3

app = Flask( __name__ )

DBname = "exampleDB.db"

@app.route( "/")
def index():
    return render_template( "index.html", msg="/が指定されました", list="")

def view_sub():
    strSQL = '''SELECT * FROM tusers'''
    con = sqlite3.connect( DBname)
    # 読み出し側が複数行になるときCursorの設定をする
    cur = con.cursor()
    # SQLの実行は、cursorの変数を使って行う
    lines = cur.execute( strSQL)
    for line in lines:
        print( line)
    con.close()
    return lines

@app.route( "/view/", methods=["POST"])
def view():
    results = view_sub()
    return render_template( "index.html", msg="viewボタンが押されました。", lines = results )

def init_sub():

    strSQL = '''CREATE TABLE IF NOT EXISTS tusers ( uid text, password text )'''
    strSQL2 = '''INSERT INTO tusers ( uid, password ) values ( "24000", "ueda" ) '''

    con = sqlite3.connect( DBname)          # データベースに接続する
    con.execute( strSQL )                   # SQLの命令を実行する
    con.execute( strSQL2 )
    # データの読み出し確認
    c = con.cursor()
    strSQL3 = '''SELECT * FROM tusers'''
    for row in c.execute( strSQL3 ):
        print( row )
    con.commit()                            # データベースに結果を反映させる
    con.close()     

@app.route( "/init/", methods=["POST"])
def init():
    init_sub()
    return render_template( "index.html", msg="initボタンが押されました。", list="")

@app.route( "/append/", methods=["POST"])
def append():
    return render_template( "index.html", msg="appendボタンが押されました")

if __name__ == "__main__":
    app.run( port=8000, debug=True)