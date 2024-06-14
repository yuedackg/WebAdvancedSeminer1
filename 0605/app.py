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
    cur = con.cursor()
    lines = cur.execute( strSQL)
    return lines.fetchall()

@app.route( "/view/", methods=["POST"])
def view():
    lines = view_sub()
    return render_template( "index.html", msg="viewボタンが押されました。", lines = lines )

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

def append_sub():
    if request.method == "POST":
        inUid = request.form.get("userid")
        inPassword = request.form.get( "password")
        print( inUid, inPassword)
        strSql = '''insert into tusers ( uid, password ) values ("''' + inUid  +  '''"," ''' +inPassword +'''")'''
        print( strSql)
        con = sqlite3.connect(DBname)
        con.execute( strSql)
        con.commit()
        con.close()

@app.route( "/append/", methods=["POST"])
def append():
    append_sub()
    return render_template( "index.html", msg="appendボタンが押されました")

@app.route( "/delete/", methods=["POST"])
def delete():
    if request.method == "POST":
        # step 1　通信からフォーム内のデータを取り出す
        uid = request.form.get( "deleteUid")
        # step 2 SQLを作る
        strSQL = '''delete from tusers where uid =="'''+ uid + '''"'''
        print( strSQL)
        # step 3　SQLを実行
        try:
            con = sqlite3.connect( DBname)
            con.execute( strSQL)
            con.commit()
            con.close()
        except sqlite3.OperationalError:
            print( "DB操作ができません")

        return render_template( "index.html", msg="削除ボタンが押されました", lines="")

@app.route( "/login/", methods=["POST"])
def login():
    if request.method == "POST":
        inUserid = request.form.get( "userid")
        inPassword = request.form.get("userserPassword")
        # print( inUserid, inPassword)
        strSql = '''select * from tusers where uid="''' + inUserid +     '''"  and password="''' + inPassword + '''"'''
        print( strSql)

        conn = sqlite3.connect( DBname)
        cur = conn.cursor()
        cur.execute( strSql)

        # print( cur.fetchone())
        if cur.fetchone() == None :
            return render_template( "index.html", msg="loginできません" )
        else:
            return render_template( "loginsuccess.html")

        conn.close()
        # ALT+z 右側で折り返し
    return render_template( "index.html", msg="loginできません" )

@app.route( "/update/" , methods=["post"])
def update():
    if request.method == "POST":
        inUserid = request.form.get( "userid")
        inPassword = request.form.get( "userserPassword")
        sreSQL = '''update tusers set password="''' + inPassword + '''" where uid="''' + inUserid + '''"'''
        print(  sreSQL)
        
if __name__ == "__main__":
    app.run( port=8000, debug=True)
