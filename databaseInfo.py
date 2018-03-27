CREATE_RATER = """CREATE TABLE Rater(
    UserID varchar(50) PRIMARY KEY,
	Email varchar(50),
	Name varchar(50),
    Password varchar(50),
	JoinDate DATE,
	rType varchar(50),
	Reputation integer CHECK (reputation <=5)
)"""

CREATE_RESTAURANT = """CREATE TABLE Restaurant(
	RestaurantID integer PRIMARY KEY,
	RestName varchar(50),
	RestType text[],
	URL varchar(100),
	ManagerName text[],
	OpeningDate date
)"""

CREATE_RATING = """CREATE TABLE Rating(
	UserID varchar(50) REFERENCES Rater(UserID),
	RateDate DATE,
	Price integer CHECK (5>=Price),
	Food integer CHECK (5>=Food),
	Mood integer CHECK (5>=Mood),
	Staff integer CHECK (5>=Staff),
	rComments varchar(500),
	RestaurantID integer REFERENCES Restaurant(RestaurantID)
)"""

CREATE_HOURS = """CREATE TABLE Hours (
RestaurantID integer REFERENCES Restaurant(RestaurantID),
DayOfTheWeek integer CHECK (DayOfTheWeek<=6),
OpenTime time,
CloseTime time
)"""

CREATE_MENU_ITEM = """CREATE TABLE MenuItem(
	ItemId integer PRIMARY KEY,
	ItemName varchar(50),
	Category text[],
	Description varchar(500),
	ItemType varchar(50),
	ItemPrice decimal,
	RestaurantId integer REFERENCES Restaurant(RestaurantID)
)"""

CREATE_RATING_ITEM = """CREATE TABLE RatingItem (
	UserID varchar(50) REFERENCES Rater(UserID),
	ItemRateDate date,
	ItemID integer REFERENCES MenuItem(ItemID),
	Rating integer CHECK (5>=rating),
	Comment varchar(500)
)"""
