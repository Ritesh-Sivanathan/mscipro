from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import csv

app = Flask(__name__)

def get_element_info(element_name):
    with open('elements.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Element'].lower() == element_name.lower():
                return row['Symbol'], row['Element'], row['AtomicMass'], row['AtomicNumber'], row['NumberofElectrons'], row['NumberofProtons'], row['NumberofNeutrons'], row['Type']
        return None

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

@app.route('/chem') 
def chemistry():
    return render_template('Subjects/science/chem.html')

@app.route('/get_element_info', methods=['POST'])
def getElementInfo():
    element_name = request.form['elementName']
    element_info = get_element_info(element_name)
    valuesDicts = {
        'Symbol': element_info[0],
        'Name': element_info[1],
        'Atomic Mass': element_info[2],
        'Atomic Number': element_info[3],
        '# of Electrons': element_info[4],
        '# of Protons': element_info[5],
        '# of Neutrons': element_info[6],
        'Type': element_info[7]
    }
    return jsonify(valuesDicts)

if __name__ == '__main__':
    app.run(debug=True)