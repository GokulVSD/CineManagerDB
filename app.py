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
		if username == 'booker' and password == 'placeholder':
			return render_template('booker.html')
		elif username == 'manager' and password == 'placeholder':
			return render_template('manager.html')
		else:
			return render_template('loginfail.html')
	except:
		return render_template('loginfail.html')

# @app.route("/insert", methods = ['POST'])
# def insert():
#     uname=request.form.get('uname')
#     pswd=request.form.get('pswd')
#     sql="INSERT INTO movies values(%s,%s,%s)"
#     val=(request.form.get('name'),request.form.get('lang'),request.form.get('len'))
#     return query(uname,pswd,sql,val)

# @app.route("/update", methods = ['POST'])
# def update():
#     uname=request.form.get('uname')
#     pswd=request.form.get('pswd')
#     sql="UPDATE movies SET "+request.form.get('cont')+" WHERE "+request.form.get('cond')
#     val=None
#     return query(uname,pswd,sql,val)

# @app.route("/delete", methods = ['POST'])
# def delete():
#     uname=request.form.get('uname')
#     pswd=request.form.get('pswd')
#     sql="DELETE FROM movies WHERE "+request.form.get('cond')
#     val=None
#     return query(uname,pswd,sql,val)

# def query(uname,pswd,sql,val):
#     try:
#         conobj = mysql.connector.connect(host='localhost',
#                                        database='test',
#                                        user=uname,
#                                        password=pswd)
#         if conobj.is_connected():
#             cursor = conobj.cursor()
#             cursor.execute(sql,val)
#             conobj.commit()
#             conobj.close()
#             return jsonify({"res" : "Success"})
#     except Error as e:
#         return jsonify({"res" : e.args[1]})
#     finally:
#         conobj.close()
#     return jsonify({"res" : "failed to connect to MySQL"})

if __name__ == "__main__":
    app.run()
 
