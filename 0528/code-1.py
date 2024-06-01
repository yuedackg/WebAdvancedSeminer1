# sqlite3に接続するためのパッケージを取り込む
import sqlite3

# sqlite3のデータベース用のファイルsampleDB.dbに接続する
# ファイル名は、作成者の裁量でつける
con = sqlite3.connect( "sampleDB.db")

# カーソル（行）を作成する；　sqlite3独特
c = con.cursor()

# SQL命令を文字列化しました（前後に’’’を付けた）；
# 再利用するかもしれないので変数strsqlに入れた
strsql= '''create table tusers( id text, password text )'''

# 既存のテーブルを消去
strsql0 = ''' drop table tusers'''

# SQLの命令を実行する
con.execute( strsql0)
con.execute( strsql)

strSqlInsert1 = '''insert  into  tusers ( id,      password)  values ( "23000", "Ckg23000!" ) '''
con.execute( strSqlInsert1)

strSqlInsert2 = '''insert  into  tusers ( id,      password)  values ( "23001", "Ckg23001!" ) '''
con.execute( strSqlInsert2)

strSqlInsert3 = '''insert  into  tusers ( id,      password)  values ( "ueda", "Ckg23002!" ) '''
con.execute( strSqlInsert3)

# id とpasswordのセットを取り出すSQLを設定する 
strSqlSelect = '''select id, password from tusers'''

# SQLを実行すると、複数行の結果が得られる。
# これを1行ずつ取り出して表示する
for row in con.execute( strSqlSelect ):
	print( row)
con.commit()
# 接続の終了
con.close()