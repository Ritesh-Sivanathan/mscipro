# https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/

# https://www.pythonanywhere.com/user/riteshsivanathan/webapps/#tab_id_riteshsivanathan_pythonanywhere_com


# ! TODO: FIX THE GITHUB PAGES NOT WORKING

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

# Create the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Configure the secret key for session management
app.secret_key = 'your_secret_key'  # Replace with an actual secret key

# Define the login_required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return decorated_function

@app.route('/admin')
def admin():
    users = User.query.all()
    user_data = [{"id": user.id, "username": user.username, "password": user.password} for user in users]
    return jsonify(users=user_data)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/base')
def readmore():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = db.session.query(User).filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return render_template('Subjects/math/mathematics.html')
        else:
            return "Invalid"  # Handle invalid login here
    else:
        return render_template('Login & Register/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id  # Store the user ID in the session
            return redirect(url_for('index'))
        except:
            return render_template('Login & Register/register.html')
    else:
        return render_template('Login & Register/register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/mathematics')
# @login_required
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

if __name__ == '__main__':
    app.run(debug=True)