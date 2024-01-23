from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

# -------- Homepage --------

@app.route('/')
def index():
    return render_template('homepage.html')

# -------- Subjects Main --------

@app.route('/mathematics')
def math():
    return render_template('Subjects/math/mathematics.html')

@app.route('/science')
def science():
    return render_template('Subjects/science/science.html')

@app.route('/programming')
def programming():
    return render_template('Subjects/programming/programming.html')

# -------- Subject Subpage --------

@app.route('/arithmetic')
def gr1prac():
    return render_template('Subjects/math/practiceprob.html')

@app.route('/calculator')
def calculator():
    return render_template('Subjects/math/calculator.html')

@app.route('/novicecoding')
def noviceCoding():
    return render_template('Subjects/programming/problems/novicecoding.html')

# -------- Other Pages --------

@app.route('/adminportal')
def adminPortal():
    return render_template('adminportal.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/settings')
def userSettings():
    return render_template('Client/settings.html')

if __name__ == '__main__':
    app.run(debug=True)