import mysql.connector,sys
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def renderLoginPage():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def verifyAndRenderRespective():
	username = request.form['username']
	password = request.form['password']

	try:
		if username == 'cashier' and password == 'a':
			return render_template('cashier.html')
		elif username == 'manager' and password == 'a':
			return render_template('manager.html')
		else:
			return render_template('loginfail.html')
	except:
		return render_template('loginfail.html')



if __name__ == "__main__":
    app.run()
 
