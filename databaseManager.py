from objectInfo import *
from databaseInfo import *
import time
import getpass
import psycopg2

DB_NAME = 'jdell012'
USERNAME = 'jdell012'
PASSWORD = getpass.getpass(prompt='Etner database password: ', stream=None)
HOST = 'www.eecs.uottawa.ca'
PORT = '15432'

conn = psycopg2.connect(dbname=DB_NAME, user=USERNAME, password=PASSWORD, host=HOST, port=PORT)
cur = conn.cursor()

##############################
# Database Structuring Methods
##############################

def initializeDatabase():
    """ Creates all the tables needed for the website database """
    cur.execute(CREATE_RATER)
    cur.execute(CREATE_RESTAURANT)
    cur.execute(CREATE_RATING)
    cur.execute(CREATE_HOURS)
    cur.execute(CREATE_MENU_ITEM)
    cur.execute(CREATE_RATING_ITEM)
    conn.commit()

def updateDatabase():
    """ Updates the database, needed to be called if table info changes """
    cur.execute("DROP TABLE IF EXISTS Rater CASCADE")
    cur.execute("DROP TABLE IF EXISTS Restaurant CASCADE")
    cur.execute("DROP TABLE IF EXISTS Rating CASCADE")
    cur.execute("DROP TABLE IF EXISTS Hours CASCADE")
    cur.execute("DROP TABLE IF EXISTS MenuItem CASCADE")
    cur.execute("DROP TABLE IF EXISTS RatingItem CASCADE")
    initializeDatabase()

#################
# Saving Methods
#################

def saveRater(x):
    cur.execute("INSERT INTO Rater(UserID, Email, rName, JoinDate, rType, Reputation) VALUES(%s, %s, %s, %s, %s, %s)", [x.UserId, x.Email, x.rName, x.JoinDate, x.rType, x.Reputation])
    conn.commit()

def saveRestaurant(x):
    cur.execute("INSERT INTO Restaurant(RestaurantID, RestName, RestType, URL, ManagerName, OpeningDate) VALUES(%s, %s, %s, %s, %s, %s)", [x.RestaurantId, x.RestName, x.RestType, x.URL, x.ManagerName, x.OpeningDate])
    conn.commit()

def saveRating(x):
    cur.execute("INSERT INTO Rating(UserID, RateDate, Price, Food, Mood, Staff, rComments, RestaurantID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", [x.UserId, x.RateDate, x.Price, x.Food, x.Mood, x.Staff, x.rComments, x.RestaurantId])
    conn.commit()

def saveHours(x):
    cur.execute("INSERT INTO Hours(RestaurantID, DayOfTheWeek, OpenTime, CloseTime) VALUES(%s, %s, %s, %s)", [x.RestaurantId, x.DayOfTheWeek, x.OpenTime, x.CloseTime])
    conn.commit()

def saveMenuItem(x):
    cur.execute("INSERT INTO MenuItem(ItemID, ItemName, Category, Description, ItemType, ItemPrice, RestaurantID)", [x.ItemId, x.ItemName, x.Category, x.Description, x.ItemType, x.ItemPrice, x.RestaurantId])
    conn.commit()

def saveRatingItem(x):
    cur.execute("INSERT INTO RatingItem(UserID, ItemRateDate, ItemID, Rating, Comment) VALUES(%s, %s, %s, %s, %s)", [x.UserId, x.ItemRateDate, x.ItemId, x.Rating, x.Comment])
    conn.commit()

#####################
# Functional Methods
#####################

def test():
    updateDatabase()
    rater = Rater("1234", "jack@test.com", "potato", time.strftime('%Y-%m-%d %H:%M:%S'), "good", 4)
    saveRater(rater)
    cur.execute("SELECT * FROM Rater")
    print(cur.fetchone())
