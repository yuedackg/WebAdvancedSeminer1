from flask import Flask, render_template, request
import sqlite3

app = Flask( __name__ )
DBname = "exampleDataBase.db"

@app.route( "/")
def index():
    return render_template( "index.html")

def view_sub():
    if request.method=="POST":
        strSQL = '''select * from tusers'''
        data = []
        try:
            conn = sqlite3.connect( DBname)
            cur = conn.cursor()
            cur.execute( strSQL)
            for line in cur.fetchall():
                l = []
                for item in line:
                    l.append( item)
                
                data.append( l)
            
            conn.close()
            return data
        except:
            print("OperationalError")
        return data

@app.route("/view/" , methods=["post"])
def view():
    return render_template( "view.html", lines=view_sub())

@app.route( "/append/", methods=["post"])
def append():
    return render_template( "append.html")

@app.route( "/doAppend/", methods=["post"])
def doAppend():
    if request.method == "POST":
        inUid = request.form.get( "uid")
        inPass = request.form.get( "pass")
        print( inUid, inPass)
    strSQL = '''select * from tusers where uid='''+ inUid + ''''''
    msg=""
    try:
        con = sqlite3.connect( DBname)
        cur = con.cursor()
        cur.execute( strSQL)
        line = cur.fetchone() 
        if line== None:
            strSQL = '''insert into tusers( uid, passwd) values ('''+ inUid + ''', "''' + inPass+ '''")''' 
            print( strSQL)
            cur.execute( strSQL)
            msg="データを追加しました"
        else:
            msg="既存のデータがあるため追加できません"
            con.commit()

        print( line)
        con.close()
      
    except sqlite3.OperationalError:
        msg="データの追加に失敗しました。"
    return render_template( "doAppend.html", msg=msg)

@app.route( "/delete/", methods=["post"])
def delete():
    strSQL = '''select * from tusers'''
    try:
        con = sqlite3.connect(DBname)
        cur = con.cursor()
        cur.execute( strSQL)
        datas = []
        for l in cur.fetchall():
            d =[]
            for item in l:
                d.append( item)
            datas.append( d)
        con.close()
    except sqlite3.OperationalError:
        print( "Operational error.")
    return render_template( "delete.html", lines=datas )

@app.apend( "/doDelete/", methods=["post"])
def doDelete():
    if  request.method=="post":
        #フォームで送られた一覧を表示

@app.route( "/init/", methods=["post"])
def init():
    strSQL = '''create table if not exists  tusers ( uid int , passwd text) '''
    strSQLinsert = '''insert into tusers ( uid, passwd ) values ( 1, "check")'''
    try:
        conn = sqlite3.connect( DBname)
        conn.execute( strSQL)
        conn.execute( strSQLinsert)
        conn.commit()
        conn.close()
    except sqlite3.OperationalError :
        print( "sql error")
        return render_template( "init.html", msg="DBの初期化・初期データの登録が正しくできませんでした")
    return render_template( "init.html", msg="テーブルの作成と初期化　OK")

if __name__ == "__main__" :
    app.run( port=8000, debug=True)

