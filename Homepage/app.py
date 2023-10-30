# https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

migrate = Migrate(app, db)  # 'db' should be your SQLAlchemy database instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/base')
def readmore():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('Login & Register/login.html')

@app.route('/register')
def register():
    return render_template('Login & Register/register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/mathematics')
def math():
    return render_template('Subjects/math/mathematics.html')

@app.route('/science')
def science():
    return render_template('Subjects/science/science.html')

@app.route('/programming')
def programming():
    return render_template('Subjects/programming/programming.html')

@app.route('/loading')
def loading():
    return render_template('Subjects/programming/programming.html')


# ‐-----‐----- RIGID BODY‐------------

@app.route('/p')
def physics():
    return render_template('Subjects/science/rigidbody.html')


# --------------------------------- MATH ---------------------------------#

@app.route('/mathematics/arithmetic')
def gr1prac():
    return render_template('Subjects/math/practiceprob.html')

if __name__ == '__main__':
    app.run(debug=True)