from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email
from databaseInfo import *
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = '54321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jdell012:#####@www.eecs.uottawa.ca:15432/jdell012'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# Creating a class that will represent the Rater table in the database
class Rater(db.Model):
    UserId = db.Column(db.String(36), primary_key=True)
    Email = db.Column(db.String(50), unique=True)
    Name = db.Column(db.String(16))
    Password = db.Column(db.String(16))
    JoinDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    rType = db.Column(db.String(50))
    Reputation = db.Column(db.Integer)

db.create_all()
db.session.commit()

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")

class registrationForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message="Please enter a valid email")])
    nickname = StringField("Display Name", validators=[InputRequired()])

    choices = [("Blog", "Blog"), ("Online", "Online"), ("Food Critic", "Food Critic"), ("Other", "Other")]
    rType = SelectField("Type", choices=choices, validators=[InputRequired()])

    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Create Account")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registrationForm()

    if form.validate_on_submit():
        e = str(form.email.data)
        n = str(form.nickname.data)
        t = str(form.rType.data)
        p = str(form.password.data)

        new_rater = Rater(UserId=str(uuid.uuid4()), Email=e, Name=n, Password=p, rType=t, Reputation=1)
        db.session.add(new_rater)
        db.session.commit()

        return "New user successfully created!";

    return render_template("registration.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # If the form is filled out and submitted properly, it will validate
    if form.validate_on_submit():
        e = form.email.data
        p = form.password.data
        return("Hello!")

        # e, p contain the email and password. Test to see if this combination
        # is linked to an account. If so login, if not ask user to make account
        # or inform them that the information entered is incorrect

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
