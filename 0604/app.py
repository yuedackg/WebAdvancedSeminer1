from flask import Flask, render_template, request

import sqlite3

app = Flask( __name__ )

DBname = "exampleDB.db"

def view_sub():
    strSQL = '''SELECT * FROM tusers'''
    con =sqlite3.connect( DBname)
    cur = con.cursor()
    cur.execute( strSQL)
    list = cur.fetchall()
    con.close()
    return list    

@app.route( "/")
def index():
    return render_template( "index.html", msg="/が指定されました", list="")

@app.route( "/view/", methods=["POST"])
def view():
    list = view_sub()
    print(list)
    return render_template( "index.html", msg="viewボタンが押されました。", list=list)

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
    con.close()                             # 接続を切る

@app.route( "/init/", methods=["POST"])
def init():
    init_sub()
    return render_template( "index.html", msg="initボタンが押されました。", list="")

def append_sub():
    if request.method == "POST":
        print( request.form.uid )

        # return "[OK]appendボタンが押されました"
        return
    else:

        # return "[NG]appendボタンの登録で失敗しました"
        return

@app.route( "/append/", methods=["POST"])
def append():
    append_sub()
    return render_template( "index.html", msg="appendボタンが押されました") 

if __name__ == "__main__":
    app.run( port=8000, debug=True)
