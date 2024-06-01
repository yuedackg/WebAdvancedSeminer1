# 文字列をHTMLに埋め込みたいときは、reder_templateをimportする
from flask import Flask,render_template
# アプリケーションオブジェクトの作成；　この時点では起動していない
app = Flask(__name__)

# ルーティングの設定１
@app.route('/')
def index():
	return render_template('index.html', STR_NAME="花子さん")

# ルーティングの設定２
@app.route( "/<name>")
def index2( name):
	return render_template( 'index.html', STR_NAME=name)
	
# 直接モジュールを起動している場合には、アプリケーションサーバとして起動する
if __name__ == "__main__":
	app.run(port=8000, debug=True)