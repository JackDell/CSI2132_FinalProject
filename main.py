from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import PrimaryKeyConstraint
from wtforms import StringField, PasswordField, SelectField, SubmitField, IntegerField, FloatField
from wtforms.validators import InputRequired, Email, Length, NumberRange
from wtforms.widgets import TextArea
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = '54321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/postgres'
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

class Rating(db.Model):
    RatingId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId = db.Column(db.String(36), db.ForeignKey("rater.UserId"), nullable=False)
    RestId = db.Column(db.Integer, db.ForeignKey("restaurant.RestId"))
    Date = db.Column(db.DateTime, default=db.func.current_timestamp())
    Price = db.Column(db.Integer)
    Food = db.Column(db.Integer)
    Mood = db.Column(db.Integer)
    Staff = db.Column(db.Integer)
    Comments = db.Column(db.String(300))

class MenuItem(db.Model):
    ItemId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RestId = db.Column(db.Integer, db.ForeignKey("restaurant.RestId"))
    Name = db.Column(db.String(50))
    Type = db.Column(db.String(50))
    Category = db.Column(db.String(50))
    Description = db.Column(db.String(50))
    Price = db.Column(db.Float)

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

class RestaurantForm(FlaskForm):
    RName = StringField("Restaurant Name", validators=[InputRequired()])
    types = [("Fast Food", "Fast Food"), ("Chinese", "Chinese"), ("Italian", "Italian"), ("Greek", "Greek"), ("Indian", "Indian"), ("Mexican", "Mexican"), ("Thai", "Thai"), ("Spanish", "Spanish"), ("American", "American"), ("Other", "Other")]
    RType = SelectField("Type", choices=types, validators=[InputRequired()])
    Address = StringField("Address", validators=[InputRequired()])
    Phone = StringField("Phone Number", validators=[InputRequired()])
    URL = StringField("Website URL", validators=[InputRequired()])
    Manager = StringField("Manager", validators=[InputRequired()])
    OpeningDate = StringField("Date of Opening", validators=[InputRequired()])
    submit = SubmitField("Create Restaurant")

class RatingForm(FlaskForm):
    Price = IntegerField("Price", validators=[InputRequired(), NumberRange(min=1, max=5)])
    Food = IntegerField("Food", validators=[InputRequired(), NumberRange(min=1, max=5)])
    Mood = IntegerField("Mood", validators=[InputRequired(), NumberRange(min=1, max=5)])
    Staff = IntegerField("Staff", validators=[InputRequired(), NumberRange(min=1, max=5)])
    Comments = StringField('Comments', widget=TextArea())
    Submit = SubmitField("Save Rating")


class MenuForm(FlaskForm):
    Name = StringField("Item Name", validators=[InputRequired()])
    types = [("Food", "Food"), ("Beverage", "Beverage")]
    Type = SelectField("Type", choices=types, validators=[InputRequired()])
    categories = [("Starter", "Starter"), ("Main", "Main"), ("Dessert", "Dessert")]
    Category = SelectField("Category", choices=categories, validators=[InputRequired()])
    Description = StringField("Description", validators=[InputRequired()])
    Price = FloatField("Price", validators=[InputRequired()])
    Submit = SubmitField("Add Item")


# Beginning of flask
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
                return redirect(url_for('restaurants'))

    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/restaurants")
@login_required
def restaurants():
    return render_template("restaurant_list.html", restaurants=getRestaurantDictionary())

@app.route("/restaurant_view/<RestId>")
@login_required
def viewRestaurant(RestId):
    print(RestId)
    return render_template("restaurant_view.html", r=restToDict(Restaurant.query.filter_by(RestId=RestId).first()), MenuItems=getMenuItems(RestId), Ratings=getRatings(RestId))

@app.route("/add_restaurant", methods=['GET', 'POST'])
def addRestaurant():
    form = RestaurantForm()

    if form.validate_on_submit():
        r = Restaurant(RestName=form.RName.data, RestType=form.RType.data, Address=form.Address.data, 
                        PhoneNumber=form.Phone.data, URL=form.URL.data, ManagerName=form.Manager.data, 
                        OpeningDate=form.OpeningDate.data)
        db.session.add(r)
        db.session.commit()
        return redirect(url_for('addMenuItem', RestId=r.RestId))

    return render_template("add_restaurant.html", form=form)

@app.route("/add_menuitem/<RestId>", methods=['GET', 'POST'])
def addMenuItem(RestId):
    form = MenuForm()

    if form.validate_on_submit():
        item = MenuItem(RestId=RestId, Name=form.Name.data, Type=form.Type.data, Category=form.Category.data, 
                            Description=form.Description.data, Price=form.Price.data)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('addMenuItem', RestId=RestId))

    return render_template("add_menuitem.html", form=form, RestId=RestId)

@app.route("/review/<RestId>", methods=['GET', 'POST'])
@login_required
def review(RestId):

    form = RatingForm()

    if form.validate_on_submit():
        r = Rating(UserId=current_user.UserId, RestId=RestId, Price=form.Price.data, Food=form.Food.data,
                    Mood=form.Mood.data, Staff=form.Staff.data, Comments=form.Comments.data)
        db.session.add(r)
        db.session.commit()
        return redirect(url_for('viewRestaurant', RestId=RestId))

    return render_template("review.html", form=form);

# Logic functions

def getRestaurantDictionary():
    returnList = []
    for r in Restaurant.query.all():
        returnList.append({"RestId" : r.RestId, "RestName" : r.RestName, "Address" : r.Address, "Number" : r.PhoneNumber})

    return returnList

def getMenuItems(RestId):
    returnList = []
    for item in MenuItem.query.filter_by(RestId=RestId):
        returnList.append({"ItemId" : item.ItemId, "RestId" : RestId, "Name" : item.Name, "Type" : item.Type, "Category" : item.Category, "Desc" : item.Description, "Price" : item.Price})
    return returnList

def getRatings(RestId):
    returnList = []
    for r in Rating.query.filter_by(RestId=RestId):
        returnList.append({"RatingId" : r.RatingId, "UserId" : r.UserId, "RestId" : r.RestId, "Date" : r.Date, "Price" : r.Price, "Food" : r.Food, "Mood" : r.Mood, "Staff" : r.Staff, "Comments" : r.Comments})
    return returnList

def restToDict(r):
    return {"RestId" : r.RestId, "RestName" : r.RestName, "RestType" : r.RestType, "Address" : r.Address, "Number" : r.PhoneNumber, "URL" : r.URL, "Manager" : r.ManagerName, "OpeningDate" : r.OpeningDate}

if __name__ == "__main__":
    app.run(debug=True)
