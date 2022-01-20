import requests
from flask import *
app = Flask(__name__)
@app.route("https://mahmoudbot.herokuapp.com/e")
def f():
	return "Hello Word ! "
app.run(host='0.0.0.0', port=8080)