import csv
import os 
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

 
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials, try again'
		else:
			return redirect(url_for('home'))

	return render_template('login.html', error=error)	


@app.route('/todo', methods=['POST', 'GET'])	#Right now it needs the file to exist for working
												#And if you refresh without input it writes the last input it was declared
def add_todo():
	error = None
	doneTodo = False
	if os.path.getsize("todo.csv") > 0:
		option = 'a'
	else:
		option = 'w'

	with open('todo.csv', option, newline='') as file:
		
		writer = csv.writer(file)
		if request.method == 'POST':
			if request.form['submitButton'] == 'addtodo':
				if len(request.form['todoItem']) > 0:
					writer.writerow([request.form['todoItem']])
				elif len(request.form['todoItem']) == 0:
					error = "To do is empty"
				elif request.form['submitButton'] == 'savetodo':
					doneTodo = True
					#Add something to close the file
					
				
	
	return render_template('todo.html', error=error)


@app.route('/')
def home():
	return "Hello World"


@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


if __name__ == '__main__':
	app.run(debug=True)
