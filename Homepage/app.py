from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory
import csv
import mysql.connector
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

app = Flask(__name__)
app.secret_key = my_secret_key

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=password_a,
            database=database_a
        )

        return conn

    except mysql.connector.Error as e:
        print("Error connecting to database:", e)
        return None

# -------- Homepage --------

@app.route('/')
def index():
    if 'logged_in' not in session:
        session['logged_in'] = False
    return render_template('homepage.html')

# -------- Login & Register --------

# -------- Login --------

@app.route('/login')
def login():
    return render_template('User Management/login.html')

@app.route('/json/resource.json')
def resource():
    return send_from_directory('static', 'resource.json')

def login_user(username, email, password):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE (username = %s OR email = %s) AND password = %s", # avoids sql injection
                       (username, email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['logged_in'] = True
            session['username'] = username

        return user
    else:
        return None

@app.route('/login-form', methods=['POST'])
def login_form():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    user = login_user(username, email, password)
    
    if user:
        return render_template('User Management/loginsuccess.html')
    else:
        return "Invalid username/email or password"

# -------- Register --------

@app.route('/register')
def register():
    return render_template('User Management/register.html')

def register_user(f_name, l_name, username, password, email):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email)) # avoids sql injection

        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            conn.close()
            return "Username/Email Exists. Choose a different Username/Email"
        else:
            cursor.execute("INSERT INTO users (f_name, l_name, username, password, email) VALUES (%s, %s, %s, %s, %s)",
                        (f_name, l_name, username, password, email))
            conn.commit()  # Commit the transaction
            cursor.close()
            conn.close()

            session['logged_in'] = True
            session['username'] = username

            return render_template('User Management/registersuccess.html')

    
    else:
        return "Failed to add user: Database connection error"

@app.route('/submit-form', methods=['POST'])
def submit_form():
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    register_user(f_name, l_name, username, password, email)

    return render_template('User Management/registersuccess.html')

# -------- Log out --------

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect('https://mscipro.pythonanywhere.com/')

@app.route('/myresources')
def myresource():
    return render_template('saved.html')
    

@app.route('/send-resources', methods=['POST'])
def sendResource():

    resource_url = request.form['resource_url']
    resource_name = request.form['resource_name']

    conn = connect_to_db()
    
    if conn:

        cursor = conn.cursor(dictionary=True)
        cursor.execute('INSERT INTO resource (resource_name, resource_url) VALUES (%s, %s)', (resource_name, resource_url))
        conn.commit()  # Commit the transaction
        cursor.close()
        conn.close()

        return 'Resources saved successfully'

    else:
        return 'Error connecting to the database. Please try again.'

# -------- Subjects Main --------

@app.route('/mathematics')
def math():
    if session['logged_in'] == True:
        return render_template('Subjects/math/mathematics.html')
    else:
        return render_template('User Management/register.html')

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

# -------- Science Subpage --------

@app.route('/g1pp')
def g1pp():
    return render_template('Subjects/science/problems/g1pp.html')

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