import sqlite3
# データベースに接続する
conn = sqlite3.connect('example.db')
c = conn.cursor()

# レコードを生年月日の降順で取得する
for row in c.execute('SELECT * FROM users ORDER BY birtyday DESC'):
    print(row)

# データベースへのアクセスが終わったら close する
conn.close()
