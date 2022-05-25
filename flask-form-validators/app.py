from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY']='SOME_KEY'

# class UserCheck:
#     def __init__(self, banned, message=None):
#         self.banned = banned
#         if not message:
#             message = 'Please choose another username'
#         self.message = message

#     def __call__(self, form, field):
#         if field.data.lower() in (word.lower() for word in self.banned):
#             raise ValidationError(self.message)

class myForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        # UserCheck(message="That username is not allowed", banned = ['root','admin','sys']),
        Length(min=2,max=15)
        ])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        for banned in ["admin", "root", "sys"]:
            if username.data.lower()== banned:
                raise ValidationError(f"Can't use that username")
        not_allowed = " *?!'^+%&\/\"()=}][{$#£ "
        for char in username.data.lower():
            if char in not_allowed:
                raise ValidationError(f"Special characters are not allowed in username.")

@app.route('/', methods=['GET','POST'])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home.html', form = form, username=username)
    else:
        return render_template('home.html', form = form, username="")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')