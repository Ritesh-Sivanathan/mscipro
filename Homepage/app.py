from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory, render_template_string
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import mysql.connector

# cannot unpack none ->
# when doing cursor select

# session variables -> u_id, username, logged_in
# mysql> select * from users where id=(select u_id from resource where r_id=25);

app = Flask(__name__)
app.secret_key = '[REDACTED]'
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    return render_template('homepage.html'), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def database_connection_error(error):
    return render_template('500.html'), 500

@app.errorhandler(Exception)
def some_random_error(error):
    return render_template('new_error.html'), 500

# ----------------------------------------------

# -------- Database Configuration --------

def connect_to_db():

    try:

        conn = mysql.connector.connect(
            'stop - trying - bro - bro'
        )

        return conn

    except mysql.connector.Error as e:

        return ("Error connecting to database:", e)

# -------- Homepage --------

@app.route('/')
def index():
    if 'logged_in' not in session:
        session['logged_in'] = False
        session['user_id'] = None
        session['username'] = None
    return render_template('homepage.html')

# -------- Login & Register --------

# -------- Login --------

@app.route('/login')
def login():
    return render_template('User Management/login.html')

@app.route('/login-form', methods=['POST'])
def login_form():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    user = log_user_in(username, email, password)

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

        cursor.execute("SELECT * FROM users WHERE username=%s OR email=%s", (username, email)) # avoids sql injection

        existing_user = cursor.fetchone()

        if existing_user:

            cursor.close()
            conn.close()
            return redirect("https://mscipro.pythonanywhere.com")

        if existing_user is None:

            conn = connect_to_db()

            cursor = conn.cursor(dictionary=True)
            cursor.execute("INSERT INTO users (f_name, l_name, username, password, email) VALUES (%s, %s, %s, %s, %s)",
                        (f_name, l_name, username, password, email))
            conn.commit()  # Commit the transaction

            cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
            user_id = cursor.fetchone()

            cursor.close()
            conn.close()



            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = user_id

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
    logout_user()
    session['logged_in'] = False
    return redirect('https://mscipro.pythonanywhere.com/')

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

# -------- Science Subpage --------

@app.route('/g1pp') # need to import g1pp.html
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