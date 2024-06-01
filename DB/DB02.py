# 必要モジュールをインポートする
import sqlite3

# データベースに接続する
conn = sqlite3.connect('example.db')
c = conn.cursor()

# テーブルの作成
c.execute( '''DROP TABLE users''')
c.execute('''CREATE TABLE users(id real, name text, birtyday text)''')

# データの挿入
c.execute("INSERT INTO users VALUES (1, '煌木 太郎', '2001-01-01')")
c.execute("INSERT INTO users VALUES (2, '学習 次郎', '2006-05-05')")
c.execute("INSERT INTO users VALUES (3, '牌存 花子', '2017-09-10')")

# 挿入した結果を保存（コミット）する
conn.commit()

# データベースへのアクセスが終わったら close する
conn.close()

