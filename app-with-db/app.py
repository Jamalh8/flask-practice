from flask import Flask,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

db.create_all()

@app.route('/')
def home():
    return 'Hello'

@app.route('/square/<int:num>')
def square(num):
    answer = num*num
    return str(answer)

@app.route('/another')
def another():
    return 'Heres another page'

@app.route('/urlfor')
def urlfor():
    return redirect(url_for('home'))

@app.route('/css')
def css():
    return '<style>body {background-color: SteelBlue;} </style> <h1 style="color:orange;"> Orange text on blue background </h1>'

@app.route('/css2')
def css2():
    return "<body style='background-image: linear-gradient(-45deg, powderblue, darkblue);'> <div style='padding:10px; margin: 10px 25%' > <h1 style='text-align:center; border: 1px solid black; border-radius: 25px; background: grey; color:blue;'> Hello Internet! </h1> </div> <h2><p style='text-align:center; text-shadow: 0 0 3px #ff0000'> This is my first python/flask page </h2></p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)