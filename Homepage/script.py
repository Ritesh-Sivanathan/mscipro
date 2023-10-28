# https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

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