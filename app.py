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


@app.route('/getMoviesShowingOnDate', methods = ['POST'])
def moviesOnDate():
	date = request.form['date']
	res = runQuery("SELECT movie_id,movie_name,type FROM movies NATURAL JOIN shows WHERE Date = '"+date+"'")

	if res == []:
		return '<h4>No Movies Showing</h4>'
	else:
		return render_template('movies.html',movies = res)


@app.route('/getTimings', methods = ['POST'])
def timingsForMovie():
	date = request.form['date']
	movieID = request.form['movieID']
	movieType = request.form['type']
	res = runQuery("SELECT time FROM shows WHERE Date='"+date+"' and movie_id = "+movieID+" and type ='"+movieType+"'")
	
	list = []

	for i in res:
		list.append( (i[0], int(i[0]/100), i[0]%100) )

	return render_template('timings.html',timings = list) 


@app.route('/getShowID', methods = ['POST'])
def getShowID():
	date = request.form['date']
	movieID = request.form['movieID']
	movieType = request.form['type']
	time = request.form['time']
	res = runQuery("SELECT show_id FROM shows WHERE Date='"+date+"' and movie_id = "+movieID+" and type ='"+movieType+"' and time = "+time)
	return jsonify({"showID" : res[0][0]})


@app.route('/getAvailableSeats', methods = ['POST'])
def getSeating():
	showID = request.form['showID']
	res = runQuery("SELECT class,no_of_seats FROM shows NATURAL JOIN halls WHERE show_id = "+showID)
	print(res)
	return 'ok'


@app.route('/getPrice', methods = ['POST'])


@app.route('/insertBooking', methods = ['POST'])


def runQuery(query):
	try:
		db = mysql.connector.connect(
			host='localhost',
			database='db_theatre',
			user='root',
			password='root123')

		if db.is_connected():
			cursor = db.cursor(buffered = True)
			cursor.execute(query)
			db.commit()
			return cursor.fetchall()

	except Error as e:
		#Some error occured
		return e.args[1] 

	finally:
		db.close()

    #Couldn't connect to MySQL
	return None

if __name__ == "__main__":
    app.run(debug=True)
 
