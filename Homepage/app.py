# https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/

# https://www.pythonanywhere.com/user/riteshsivanathan/webapps/#tab_id_riteshsivanathan_pythonanywhere_com


# ! TODO: FIX THE GITHUB PAGES NOT WORKING

from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('Login & Register/login.html')

@app.route('/register')
def register():
    return render_template('Login & Register/register.html')


@app.route('/base')
def readmore():
    return render_template('base.html')

# 
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

# RIGID BODY

@app.route('/p')
def physics():
    return render_template('Subjects/science/rigidbody.html')

# MATH - Arithmetic

@app.route('/arithmetic')
def gr1prac():
    return render_template('Subjects/math/practiceprob.html')

@app.route('/calculator')
def calculator():
    return render_template('Subjects/math/calculator.html')

@app.route('/development')
def development():
    return render_template('Development Tracking Pages/devtrack.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/novicecoding')
def noviceCoding():
    return render_template('Subjects/programming/problems/novicecoding.html')

@app.route('/adminportal')
def adminPortal():
    return render_template('adminportal.html')


if __name__ == '__main__':
    app.run(debug=True)
