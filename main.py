from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired
from databaseInfo import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '54321'
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class registrationForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    nickname = StringField("Alias", validators=[InputRequired()])

    choices = ["Blog", "Online", "Food Critic", "Other"]
    rType = SelectField(label='Type', choices=choices)

    password = PasswordField("Password", validators=[InputRequired()])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST']):
def register():
    return "register"

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # If the form is filled out and submitted properly, it will validate
    if form.validate_on_submit():
        e = form.email.data
        p = form.password.data

        # e, p contain the email and password. Test to see if this combination
        # is linked to an account. If so login, if not ask user to make account
        # or inform them that the information entered is incorrect

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
