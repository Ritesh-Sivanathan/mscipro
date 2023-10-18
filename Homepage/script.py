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

if __name__ == '__main__':
    app.run(debug=True)