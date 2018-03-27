from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from databaseInfo import *
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = '54321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jdell012:#####@www.eecs.uottawa.ca:15432/jdell012'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Creating a class that will represent the Rater table in the database
class Rater(UserMixin, db.Model):
    UserId = db.Column(db.String(36), primary_key=True)
    Email = db.Column(db.String(50), unique=True)
    Name = db.Column(db.String(16))
    Password = db.Column(db.String(80))
    JoinDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    rType = db.Column(db.String(50))
    Reputation = db.Column(db.Integer, default=1)

    # Overriding get_id to return UserId
    def get_id(self):
        return self.UserId

db.create_all()
db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return Rater.query.get(user_id)


# Form classes for wtforms
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message="Please enter a valid email")])
    nickname = StringField("Display Name", validators=[InputRequired()])

    choices = [("Blog", "Blog"), ("Online", "Online"), ("Food Critic", "Food Critic"), ("Other", "Other")]
    rType = SelectField("Type", choices=choices, validators=[InputRequired()])

    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Create Account")

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        e = str(form.email.data)
        n = str(form.nickname.data)
        t = str(form.rType.data)
        hashed_password = generate_password_hash(form.password.data, method='sha256')

        new_rater = Rater(UserId=str(uuid.uuid4()), Email=e, Name=n, Password=hashed_password, rType=t)
        db.session.add(new_rater)
        db.session.commit()

        return redirect(url_for('login'));

    return render_template("registration.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()

    # If the form is filled out and submitted properly, it will validate
    if form.validate_on_submit():
        user = Rater.query.filter_by(Email=form.email.data).first()
        #if the user exists
        if user:
            if check_password_hash(user.Password, form.password.data):
                login_user(user)
                return redirect(url_for('index'))

    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
