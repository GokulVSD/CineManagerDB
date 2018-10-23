import mysql.connector,sys
import datetime
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template
from random import randint

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


# Routes for cashier
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
		list.append( (i[0], int(i[0]/100), i[0]%100 if i[0]%100 != 0 else '00' ) )

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

	totalGold = 0
	totalStandard = 0

	for i in res:
		if i[0] == 'gold':
			totalGold = i[1]
		if i[0] == 'standard':
			totalStandard = i[1]

	res = runQuery("SELECT seat_no FROM booked_tickets WHERE show_id = "+showID)

	goldSeats = []
	standardSeats = []

	for i in range(1, totalGold + 1):
		goldSeats.append([i,''])

	for i in range(1, totalStandard + 1):
		standardSeats.append([i,''])

	for i in res:
		if i[0] > 1000:
			goldSeats[ i[0] % 1000 - 1 ][1] = 'disabled'
		else:
			standardSeats[ i[0] - 1 ][1] = 'disabled'

	return render_template('seating.html', goldSeats = goldSeats, standardSeats = standardSeats)


@app.route('/getPrice', methods = ['POST'])
def getPriceForClass():
	showID = request.form['showID']
	seatClass = request.form['seatClass']

	res = runQuery("SELECT price FROM shows NATURAL JOIN price_listing WHERE show_id = "+showID)

	if res == []:
		return '<h5>Prices Have Not Been Assigned To This Show, Try Again Later</h5>'

	price = int(res[0][0])
	if seatClass == 'gold':
		price = price * 1.5

	return '<h5>Ticket Price: ₹ '+str(price)+'</h5>\
	<button onclick="confirmBooking()">Confirm</button>'


@app.route('/insertBooking', methods = ['POST'])
def createBooking():
	showID = request.form['showID']
	seatNo = request.form['seatNo']
	seatClass = request.form['seatClass']

	if seatClass == 'gold':
		seatNo = int(seatNo) + 1000

	ticketNo = 0
	res = None

	while res != []:
		ticketNo = randint(0, 2147483646)
		res = runQuery("SELECT ticket_no FROM booked_tickets WHERE ticket_no = "+str(ticketNo))
	
	res = runQuery("INSERT INTO booked_tickets VALUES("+str(ticketNo)+","+showID+","+str(seatNo)+")")

	if res == 'No result set to fetch from.':
		return '<h5>Ticket Successfully Booked</h5>\
		<h6>Ticket Number: '+str(ticketNo)+'</h6>'


# Routes for manager
@app.route('/getShowsShowingOnDate', methods = ['POST'])
def getShowsOnDate():
	date = request.form['date']

	res = runQuery("SELECT show_id,movie_name,type,time FROM shows NATURAL JOIN movies WHERE Date = '"+date+"'")
	
	if res == []:
		return '<h4>No Shows Showing</h4>'
	else:
		shows = []
		for i in res:
			shows.append([ i[0], i[1], i[2], int(i[3] / 100), i[3] % 100 ])

		return render_template('shows.html', shows = shows)


@app.route('/getBookedWithShowID', methods = ['POST'])
def getBookedTickets():
	showID = request.form['showID']

	res = runQuery("SELECT ticket_no,seat_no FROM booked_tickets WHERE show_id = "+showID+" order by seat_no")

	if res == []:
		return '<h5>No Bookings</h5>'

	tickets = []
	for i in res:
		if i[1] > 1000:
			tickets.append([i[0], i[1] - 1000, 'Gold'])
		else:
			tickets.append([i[0], i[1], 'Standard'])

	return render_template('bookedtickets.html', tickets = tickets)


@app.route('/fetchMovieInsertForm', methods = ['GET'])
def getMovieForm():
	return render_template('movieform.html')


@app.route('/insertMovie', methods = ['POST'])
def insertMovie():
	movieName = request.form['movieName']
	movieLen = request.form['movieLen']
	movieLang = request.form['movieLang']
	types = request.form['types']
	startShowing = request.form['startShowing']
	endShowing = request.form['endShowing']

	res = runQuery('SELECT * FROM movies')

	for i in res:
		if i[1] == movieName and i[2] == int(movieLen) and i[3] == movieLang and i[4] == types\
		 and i[5].strftime('%Y/%m/%d') == startShowing and i[6].strftime('%Y/%m/%d') == endShowing:
			return '<h5>The Exact Same Movie Already Exists</h5>'

	movieID = 0
	res = None

	while res != []:
		movieID = randint(0, 2147483646)
		res = runQuery("SELECT movie_id FROM movies WHERE movie_id = "+str(movieID))
	
	res = runQuery("INSERT INTO movies VALUES("+str(movieID)+",'"+movieName+"',"+movieLen+\
		",'"+movieLang+"','"+types+"','"+startShowing+"','"+endShowing+"')")

	if res == 'No result set to fetch from.':
		return '<h5>Movie Successfully Added</h5>\
		<h6>Movie ID: '+str(movieID)+'</h6>'

	else:
		return '<h5>Something Went Wrong</h5>'


@app.route('/getValidMovies', methods = ['POST'])
def validMovies():
	showDate = request.form['showDate']

	res = runQuery("SELECT movie_id,movie_name,types,length,language FROM movies WHERE show_start <= '"+showDate+\
		"' and show_end >= '"+showDate+"'")

	if res == []:
		return '<h5>No Movies Available for Showing On Selected Date</h5>'

	return render_template('validmovies.html', movies = res)


@app.route('/getHallsAvailable', methods = ['POST'])
def getHalls():
	movieID = request.form['movieID']
	showDate = request.form['showDate']
	showTime = request.form['showTime']

	res = runQuery("SELECT length FROM movies WHERE movie_id = "+movieID)

	movieLen = res[0][0]

	showTime = int(showTime)

	showTime = int(showTime / 100)*60 + (showTime % 100)

	endTime = showTime + movieLen 

	res = runQuery("SELECT hall_id, length, time FROM shows NATURAL JOIN movies WHERE Date = '"+showDate+"'")

	unavailableHalls = set()

	for i in res:

		x = int(i[2] / 100)*60 + (i[2] % 100)

		y = x + i[1]

		if x >= showTime and x <= endTime:
			unavailableHalls = unavailableHalls.union({i[0]})

		if y >= showTime and y <= endTime:
			unavailableHalls = unavailableHalls.union({i[0]})

	res = runQuery("SELECT DISTINCT hall_id FROM halls")

	availableHalls = set()

	for i in res:

		availableHalls = availableHalls.union({i[0]})

	availableHalls = availableHalls.difference(unavailableHalls)

	if availableHalls == set():

		return '<h5>No Halls Available On Given Date And Time</h5>'

	return render_template('availablehalls.html', halls = availableHalls)
	

@app.route('/insertShow', methods = ['POST'])
def insertShow():
	hallID = request.form['hallID']
	movieID = request.form['movieID']
	movieType = request.form['movieType']
	showDate = request.form['showDate']
	showTime = request.form['showTime']

	showID = 0
	res = None

	while res != []:
		showID = randint(0, 2147483646)
		res = runQuery("SELECT show_id FROM shows WHERE show_id = "+str(showID))
	
	res = runQuery("INSERT INTO shows VALUES("+str(showID)+","+movieID+","+hallID+\
		",'"+movieType+"',"+showTime+",'"+showDate+"',"+'NULL'+")")

	if res == 'No result set to fetch from.':
		return '<h5>Show Successfully Scheduled</h5>\
		<h6>Show ID: '+str(showID)+'</h6>'

	else:
		return '<h5>Something Went Wrong</h5>'


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
 
