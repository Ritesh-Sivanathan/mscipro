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

@app.route('/p')
def physics():
    return render_template('Subjects/science/rigidbody.html')


# --------------------------------- MATH ---------------------------------#

@app.route('/gr1practice')
def gr1prac():
    return render_template('Subjects/math/Grade 1 PP/grade1practice.html')

@app.route('/gr2practice')
def gr2pract():
    return render_template('Subjects/math/Grade 2 PP/grade2practice.html')

@app.route('/gr3practice')
def gr3pract():
    return render_template('Subjects/math/Grade 3 PP/grade2practice.html')

@app.route('/gr4practice')
def gr4pract():
    return render_template('Subjects/math/Grade 4 PP/grade2practice.html')

@app.route('/gr5practice')
def gr5pract():
    return render_template('Subjects/math/Grade 5 PP/grade2practice.html')

@app.route('/gr6practice')
def gr6pract():
    return render_template('Subjects/math/Grade 6 PP/grade2practice.html')

@app.route('/gr7practice')
def gr7pract():
    return render_template('Subjects/math/Grade 7 PP/grade2practice.html')

@app.route('/gr8practice')
def gr8pract():
    return render_template('Subjects/math/Grade 8 PP/grade2practice.html')

@app.route('/gr9practice')
def gr9pract():
    return render_template('Subjects/math/Grade 9 PP/grade2practice.html')



if __name__ == '__main__':
    app.run(debug=True)