from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = '54321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jdell012:####@www.eecs.uottawa.ca:15432/jdell012'
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

class Restaurant(db.Model):
    RestId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RestName = db.Column(db.String(50))
    RestType = db.Column(db.String(100))
    Address = db.Column(db.String(100), unique=True)
    PhoneNumber = db.Column(db.String(16))
    URL = db.Column(db.String(150))
    ManagerName = db.Column(db.String(50))
    OpeningDate = db.Column(db.DateTime)

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


# Beginning of flask
@app.route("/")
@login_required
def index():
    createData()
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

    print(getRestaurantDictionary())
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

@app.route("/restaurants")
def restaurants():
    return render_template("restaurant_list.html", restaurants=getRestaurantDictionary())

@app.route("/restaurant_view/<RestId>")
def viewRestaurant(RestId):
    print(RestId)
    return render_template("restaurant_view.html", r=restToDict(Restaurant.query.filter_by(RestId=RestId).first()))

# Logic functions

def getRestaurantDictionary():
    returnList = []
    for r in Restaurant.query.all():
        returnList.append({"RestId" : r.RestId, "RestName" : r.RestName, "Address" : r.Address, "Number" : r.PhoneNumber})

    return returnList

def restToDict(r):
    return {"RestId" : r.RestId, "RestName" : r.RestName, "RestType" : r.RestType, "Address" : r.Address, "Number" : r.PhoneNumber, "URL" : r.URL, "Manager" : r.ManagerName, "OpeningDate" : r.OpeningDate}

def createData():

    try:
        r1 = Restaurant(RestName="Swiss Chalet", RestType="Home-cooked", Address="123 Main Street, Toronto", PhoneNumber="905-123-4567", URL="https://www.SwissChalet.com", ManagerName="Barb Sanders", OpeningDate="1954-03-16")
        r2 = Restaurant(RestName="Khao Thai", RestType="Thai", Address="557 Chapel Street, Ottawa", PhoneNumber="613-809-1122", URL="http://www.khaothai.ca", ManagerName="Par Chiturai", OpeningDate="2001-11-14")
        r3 = Restaurant(RestName="La Bottega", RestType="Italian", Address="981 Somerset West, Ottawa", PhoneNumber="613-333-3145", URL="https://www.labottega.ca", ManagerName="Armi VanDuren", OpeningDate="2002-06-20")
        r4 = Restaurant(RestName="Coconut Lagoon", RestType="Indian", Address="82 King Street, Toronto", PhoneNumber="416-808-9967", URL="https://www.coconutlagoon.ca", ManagerName="Aryn Palwal", OpeningDate="1998-03-15")
        r5 = Restaurant(RestName="The Keg", RestType="American", Address="142 Auburn Lane, Courtice", PhoneNumber="905-372-3758", URL="https://www.kegsteakhouse.com", ManagerName="Janice Smith", OpeningDate="1995-08-03")
        db.session.add(r1)
        db.session.add(r2)
        db.session.add(r3)
        db.session.add(r4)
        db.session.add(r5)
        db.session.commit()
        print("Data Created")
    except:
        pass

if __name__ == "__main__":
    app.run(debug=True)
