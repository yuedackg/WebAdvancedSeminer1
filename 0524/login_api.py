# fillename: login_api.py
from flask import Flask
import flask

app = Flask( __name__, static_folder='.',static_url_path='')

login_state = False

@app.route('/')
def index():
	return  app.send_static_file( 'index.html')

@app.route( '/mypage')
def mypage():
	login_state = False
	if login_state is False:

		return  flask.jsonify( {
					"code" : 400 ,
					"msg"  : "Bad Request"
			     })
	else:
		userdata = {
			"username": "ueda"
		}
		return flask.jsonify({
					"code": 200,
					"msg": "OK",
					"result": userdata
				})


if __name__ == "__main__":
	app.run( port=8000, debug=True)
	
#  http://localhost:8000/
#  http://localhost:8000/mypage
