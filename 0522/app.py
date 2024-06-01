from flask import Flask, render_template, request

app = Flask( __name__)

@app.route( "/" , methods=[ 'GET', 'POST'] )
def  startScreen():
	if request.method == 'POST' :
		print( 'ユーザIDの値は' + str( request.form['id']))
		print( 'パスワードは' + str( request.form['pwd']))
		if str( request.form['id']) == '23000'  :
			return render_template( "login_success.html")
		else :
			return render_template( "login.html")
	else:
		return render_template( "login.html")
if __name__ == "__main__":
	app.run( port=8000, debug=True)
