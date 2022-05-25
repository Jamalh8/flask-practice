from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    dob= DateField("Enter your D.O.B: ")
    number = IntegerField("Enter your favourite number: ")
    food= SelectField("Enter in your favourite food: ", choices=[("pizza", "Pizza"), ("chips", "Chips"), ("steak", "Steak")])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        number = form.number.data
        food = form.food.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you. Your personalised username is: {food}{dob}{first_name}{number}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')