from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Set a secret key for session management.
app.secret_key = 'your_secret_key'
# Replace 'your_secret_key' with a strong secret key.

# Define a sample user for demonstration.
sample_user = {
    'username': 'your_username',
    'password': 'your_password',
}

mail_list = {
    
}

@app.route('/')
def index():
    return render_template('homepage.html')
    

@app.route('/base')
def readmore():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/mathematics')
def math():
    return render_template('Subjects/mathematics.html')

@app.route('/science')
def science():
    return render_template('Subjects/science.html')

@app.route('/auth', methods=['POST'])
def authenticate():
    if request.referrer.endswith('/login'):
        username = request.form.get('username')
        password = request.form.get('password')

        # Replace this with your actual authentication logic.
        with open('Homepage/users.txt', 'r') as file:
            content = file.read()
            if username and password in content:
                session['logged_in'] = True
                return redirect(url_for('dashboard'))
            else:
                return mail_list
    
    elif request.referrer.endswith('/register'):
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        with open('Homepage/users.txt', 'r+') as file:
            file.write(f"{username} : {password}")

        return render_template('homepage.html')

        


@app.route('/dashboard')
def dashboard():
    if session.get('logged_in'):
        return render_template('homepage.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/loginfailed')
def failedtest():
    return render_template('loginfailed.html')

if __name__ == '__main__':
    app.run(debug=True)
    