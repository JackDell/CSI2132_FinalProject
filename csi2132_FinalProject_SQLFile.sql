/******* 
Creating and Populating Tables & Queries
CSI2132
By: Amelie Khan (8660781) & Jack Dell
April 9th 2018
*******/

CREATE TABLE Rater(
	UserID varchar(6) PRIMARY KEY,
	Email varchar(50) UNIQUE,
	rName varchar(50) UNIQUE,
	JoinDate DATE,
	rType varchar(50),
	reputation integer CHECK (reputation <=5 and reputation >=1)
);
CREATE TABLE Restaurant(
	RestaurantID integer PRIMARY KEY,
	restoName varchar(50),
	restoType text[],
	URL varchar(100),
	managerName text[],
	openingDate date
);

CREATE TABLE Rating(
	UserID varchar(50) REFERENCES Rater(UserID),
	rateDate DATE,
	Price integer CHECK (5>=Price and Price >=1),
	Food integer CHECK (5>=Food and Food >=1),
	Mood integer CHECK (5>=Mood and Mood >=1),
	Staff integer CHECK (5>=Staff and Staff >=1),
	rComments varchar(500),
	RestaurantID integer REFERENCES Restaurant(RestaurantID)
	
);

CREATE TABLE Hours (
RestaurantID integer REFERENCES Restaurant(RestaurantID),
DayOfTheWeek integer CHECK (DayOfTheWeek<=7 and DayOfTheWeek >=1),
OpenTime time,
CloseTime time
);

CREATE TABLE MenuItem(
	ItemID integer PRIMARY KEY,
	itemName varchar(50),
	Category text[],
	description varchar(500),
	itemType varchar(50),
	itemPrice decimal,
	RestaurantID integer REFERENCES Restaurant(RestaurantID)
);

CREATE TABLE RatingItem (
	UserID varchar(50) REFERENCES Rater(UserID),
	itemRateDate date,
	ItemID integer REFERENCES MenuItem(ItemID),
	rating integer CHECK (5>=rating and rating >=1),
	comment varchar(500)
);

/*****************INSERTS********************/
/****Restos*******/
INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(05673847,'El Camino', '{Mexican}','https://eatelcamino.com/', '{Susan Wilkins}','2006-02-16');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(75910384,'Khao Thai', '{Thai}','http://www.khaothai.ca/', '{Par Chiturai}','2001-11-14');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(9288713,'La Bottega', '{Italian}','https://www.labottega.ca/', '{Armi VanDuren}','2000-11-01');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(8876243,'Aroma Meze', '{Mediterranean}','http://www.aromameze.com/', '{Adem Turan}','2002-06-20');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(08707617,'Coconut Lagoon', '{Indian}','http://www.coconutlagoon.ca/', '{Aryn Palwal}','1998-03-15');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(38267910,'The Keg', '{American}','https://www.kegsteakhouse.com/', '{Janice Smith}','1995-08-03');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(44872190,'Kochin Kitchen', '{Asian}','http://www.kochinkitchen.ca/', '{Sagal Parri}','2005-09-21');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(8768947,'The Soca Kitchen', '{South American}','https://www.thesocakitchen.com/', '{Maria Sanchez}','2002-04-10');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(8376491,'222 Lyon Tapas Bar', '{Spanish}','http://www.222lyontapasbar.com/', '{Pablo Navid}','2000-10-16');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(65919981,'Two Six Ate', '{Canadian}','http://twosixate.com/contact-us/', '{Arnold Heffin}','1990-02-02');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(88745672,'Rangoon', '{Burmese}','http://www.rangoonrestaurant.ca/', '{Raina Heldman}','2010-09-20');

INSERT INTO Restaurant(RestaurantID,restoName,restoType,URL,managerName,openingDate)
VALUES(987689765,'Datsun', '{Asian}','http://eatdatsun.com/', '{Marrio Elrani}','2012-11-05');
/****Raters*******/

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(897369,'aby@gmail.com','eater123','2012-07-19','blog',2);

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(885763,'aly67@gmail.com','BigEatsOttawa','2011-03-21','food critic',3);

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(346543,'ellenB@gmail.com','IloveOttawaFood','2006-11-02','online',5);

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(118956,'azzaly@gmail.com','Foodie123','2008-12-06','blog',5);

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(989121,'ilovefoodott@gmail.com','OTTeats','2003-09-16','online',3);

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(736498,'haryKlein@gmail.com','FoodReviewsOtt','2004-07-08','food critic',4);

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(665498,'akhan@gmail.com','fooooodie','2008-05-18','online',1);

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(736098,'georgia@gmail.com','FoodRevOtt','2006-07-10','food critic',3);

INSERT INTO Rater(UserID,Email,rName,JoinDate,rType,reputation)
VALUES(198703,'haryKook@gmail.com','OttLuvsFood','2004-07-08','blog',5);

/****Menu Items****/

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(8475, 'Eggplant Taco','{Main}','Battered and fried eggplant taco','food',6.5,05673847);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(9899, 'Churros','{Dessert}','Traditional mexican churros with dulce de leche dipping sauce','food',5.0,05673847);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(0098, 'Fish Taco','{Main}','Battered and fried fish taco','food',7,05673847);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(8897, 'Chickpea curry','{Main}','Burmese chickpea curry with rice','food',12.0,88745672);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(3327, 'Coconut Rice','{Side}','Burmese coconut rice','food',3.0,88745672);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(7639, '6 oz Filet Mignon','{Main}','Filet mignon with a side of potatos and salad','food',28.0,38267910);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(7483, 'Surf and Turf','{Main}','Lobster tail, shrimp and 6 oz steak with choice of side','food',35.0,38267910);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(2984, 'Ratatouille','{Main}','Sauteed zucchini and eggplant with a spanish flair','food',12.0,8376491);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1190, 'Artichoke Dip','{App}','Served with crostinis and apple slices','food',7.0,8376491);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(7789, 'Eggplant','{Side}','Small eggplant chuncks with a ginger garlic tamarind sauce','food',5.0,44872190);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(0097, 'King Fish Curry','{Main}','King fish pieces in a special blend of chefs spices','food',15.0,44872190);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(4856, 'Ice Cream','{Dessert}','Choice of Vanilla, Mango, Pineapple','food',6.0,44872190);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1911, 'White Manhattan','{Cocktail}','Drink special of the day','drink',14.0,65919981);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1878, 'Ants on a Log','{Main}','Poached and roasted Acorn Creek celeriac is served with Rideau Pine ground cherries','food',20.0,65919981);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1900, 'Charcuterie board','{App}','House charcuterie, mustard, preserves, house bread','food',21.0,65919981);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1213, 'Ice Cream Sandwich','{Dessert}','Rhubard ice cream, strawbeery cookie, chokecherry powder','food',8.0,65919981);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1222, 'Pad Thai Jay','{Main}','Classic thai noodle dish made with tofu, eggs, mixed vegetables ground peanuts and fresh bean sprouts','food',16.0,75910384);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1298, 'Tom Yum Pak','{App}','Vegetables in hot and sour soup with exotic thai spices','food',7.0,75910384);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1200, 'Steamed Jasmine Rice','{Side}',' ','food',2.50,75910384);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5567, 'Steam Bun','{Main}','Fresh asian steam bun','food',5.0,987689765);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5599, 'Jameson','{Beer}','Drink special','drink',3.5,987689765);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5560, 'Tuna Tartar','{Main}','Cured in wasabi, pimento aioli, lime, served with baked pita and cucumber slices','food',13.0,8876243);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5060, 'Lamb Sliders','{Main}','Ground lamb patties (halal), red onion, tomatoes, cucumber, tzatziki sauce on mini-pitas wheels','food',11.0,8876243);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(0960, 'Creme Brulee','{Dessert}','Rich vanilla custard topped with caramelized sugar','food',8.0,8876243);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5960, 'Tzatziki','{Side}','Cucumber,garlic,sheeps milk yoghurt','food',5.0,8876243);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5980, 'Dolmades','{App}','Grape leaves stuffed with extra lean halal ground beef & dill rice, avgolemono sauce','food',6.0,8876243);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5919, 'Italian Sandwich','{Main}','Select a meat, bread and topping for a custom,authentic sandwich','food',6.50,9288713);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5019, 'Tiramisu','{Dessert}','Made in house daily','food',4.50,9288713);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5989, 'Grilled Calamari','{Main}','with citrus homemade yogurt dip','food',15.50,8768947);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(0989, 'Dozen Oysters','{Main}','Fresh oysters accompanied by home made sauces','food',16.0,8768947);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5339, 'Onion Fritters','{App}','Onion Baji with mint chutney','food',9.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(9939, 'Butter Chicken','{Main}','All time favorite Indian specialty','food',23.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1139, 'Vegetable salad','{Side}','Fresh local veggie salad','food',9.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5319, 'Lamb Biryani','{Main}','Authentic flavoured rice dish with spices and slow baked, served with raita','food',19.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5119, 'Pan sauteed Crab Cakes','{App}','Crab cakes with Kerala spices and chili lime aioli','food',12.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5559, 'Vegetable Samosa','{App}','Half dozen crispy samosas with tamarind chutney','food',8.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(4490, 'Nilgiri Chicken','{Main}','Chickecn in fresh corieander and mint sauce','food',23.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(1939, 'Beef Curry','{Main}','Beef cooked in a thick rich curry sauce','food',23.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(5311, 'Chicken Pakoras','{App}','Batter fried chicken filets with chili lime aioli','food',12.0, 08707617);

INSERT INTO MenuItem(ItemID,itemName,Category,description,itemType,itemPrice,RestaurantID)
VALUES(6679, 'Chef creation soup','{App}','Daily creation with fresh & seasonal ingredients','food',8.0, 08707617);

/****** Ratings*******/

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(897369, '2010-02-05',3,4,3,5,'Flavourful food and nice ambience.Good value',05673847);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(897369, '2013-01-05',3,3,3,5,'Great service, food was okay.',75910384);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(897369, '2016-09-16',4,4,4,5,'I come here every weekend, great value and service',08707617);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(885763, '2008-05-03',5,4,4,3,'Everything was great except service was slow. Make sure to make a reservation.',08707617);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(885763, '2008-05-03',5,4,3,5,'Highly recommend',05673847);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(346543, '2006-10-19',2,4,3,5,'Nice place, good value',05673847);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(346543, '2010-04-21',3,4,5,4,'Very authentic. My family and I enjoyed a lot. Highly recommend.',08707617);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(118956, '2017-08-03',2,4,3,3,'Best sandwiches in town. Great selection of toppings!',9288713);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(118956, '2015-09-03',3,4,4,3,'Nice atmosphere and good food.',38267910);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(989121, '2017-10-12',2,4,4,3,'Food and atmosphere is great for date night!',05673847);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(989121, '2009-08-03',4,4,4,5,'Amazing tapas. Little Spain in Ottawa!',8376491);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(989121, '2016-11-05',3,4,3,3,'Only burmese food in Ottawa- amazing flavour.',88745672);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(736498, '2004-10-15',3,4,4,2,'Delicious food, lots of vegan options!',88745672);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(736498, '2008-11-03',3,4,3,3,'Such a fun place for drinks and small plates',987689765);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(736498, '2013-06-03',3,3,3,3,'Casual place, nothing too special but good for takeout',44872190);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(665498, '2008-06-03',3,5,5,3,'Yum!!!',65919981);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(665498, '2017-11-01',4,4,4,5,'Really cute place to take a date',8768947);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(665498, '2017-05-10',3,4,4,4,'great food. Highly recommend ',8876243);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(665498, '2010-09-12',3,5,4,4,'Amazing tacos!! ',05673847);

INSERT INTO Rating(UserId,rateDate,Price,Food,Mood,Staff,rComments,RestaurantID)
VALUES(665498, '2012-10-05',4,5,4,5,'One of my favorite restos, however price is going up',05673847);

/********INSERT INTO HOURS*******/

INSERT INTO Hours(RestaurantID,DayOfTheWeek,OpenTime,CloseTime)
VALUES(05673847, 1,'09:00','21:00');

INSERT INTO Hours(RestaurantID,DayOfTheWeek,OpenTime,CloseTime)
VALUES(05673847, 2,'09:00','21:00');

INSERT INTO Hours(RestaurantID,DayOfTheWeek,OpenTime,CloseTime)
VALUES(05673847, 3,'09:00','21:00');

INSERT INTO Hours(RestaurantID,DayOfTheWeek,OpenTime,CloseTime)
VALUES(05673847, 4,'09:00','21:00');

INSERT INTO Hours(RestaurantID,DayOfTheWeek,OpenTime,CloseTime)
VALUES(05673847, 5,'09:00','21:00');

INSERT INTO Hours(RestaurantID,DayOfTheWeek,OpenTime,CloseTime)
VALUES(05673847, 6,'12:00','20:00');

INSERT INTO Hours(RestaurantID,DayOfTheWeek,OpenTime,CloseTime)
VALUES(05673847, 7,'12:00','20:00');





/*****************QUERIES********************/

/* FOR THE QUERIES THAT REQUIRE USER SELECTION,
   WE HAVE USED A VARIABLE "userSpecified", 
   TO TEST YOU MAY INPUT A RESTO NAME OF YOUR CHOICE (TRY 'El Camino' as an example)*/

/****Resto and Menus*******/

/*a*/
SELECT * 
FROM Restaurant
WHERE restoName= 'userSpecifiedRestoName'; 

/*b*/
SELECT itemName, category, itemPrice, description
FROM MenuItem
WHERE RestaurantID =
	(SELECT RestaurantID
	 FROM Restaurant 
	 WHERE restoName = 'userSpecified')
GROUP BY category, MenuItem.itemName, MenuItem.itemPrice, MenuItem.description; 

/*c*/
SELECT managerName, openingDate
FROM Restaurant
WHERE restoType = 'userSpecifiedRestoType';

/*d*/
SELECT MAX(itemPrice)AS MostExpensiveMenuItem$, itemName, managerName, URL, OpenTime
FROM MenuItem
JOIN restaurant ON MenuItem.restaurantID = restaurant.restaurantID
JOIN Hours ON Hours.restaurantID = restaurant.restaurantID
WHERE MenuItem.restaurantID= 
(SELECT restaurantID
 FROM restaurant
 WHERE restaurant.restoName = 'El Camino')
GROUP BY itemName, managerName, URL, OpenTime
ORDER BY MostExpensiveMenuItem$ DESC
LIMIT 1; 

/*e*/
SELECT AVG(itemPrice), restoType, Category
FROM  MenuItem
JOIN Restaurant ON MenuItem.RestaurantID = Restaurant.RestaurantID
GROUP BY Restaurant.restoType, MenuItem.Category
ORDER BY Restaurant.restoType, MenuItem.Category;

/****Ratings of restaurants****/

/*f*/
SELECT COUNT(rating) AS numRatings,restoName, string_agg(rName,', ')
FROM rating
JOIN Restaurant ON Rating.RestaurantID = restaurant.RestaurantID
JOIN rater ON rater.userID = rating.userID
GROUP BY restoName
ORDER BY numRatings DESC; 

/*g*/
SELECT restoName, restoType
FROM Restaurant
JOIN Rating ON rating.RestaurantID = Restaurant.RestaurantID AND 
Rating.rateDate <> '2015-02-05'
GROUP BY restoName, restoType;

/*h*/
SELECT restoName,openingDate, rateDate
FROM restaurant
JOIN rating ON rating.restaurantID = restaurant.restaurantID AND rating.UserId = '665498' 
WHERE rating.Staff< rating.Mood or rating.Staff<rating.Price or rating.Staff<rating.Food
ORDER BY rateDate DESC; 

/*i*/
SELECT restoName AS "Restaurant",Food AS "Rating", rName AS "Rater Name"
FROM restaurant 
JOIN rating ON rating.restaurantID = restaurant.restaurantID
JOIN rater ON rating.UserId = rater.UserId
WHERE rating.Food =(
  SELECT MAX(rating.Food)
  FROM rating, restaurant
  WHERE restaurant.restotype = '{Asian}');

/*J*//** compares the number of reviews between restaurant types...assume that the more reviews it has, the more popular it is!*/
SELECT COUNT(rating) AS NumRatings,restoType 
FROM restaurant
JOIN rating ON restaurant.restaurantId = rating.restaurantId
GROUP BY restoType
ORDER BY NumRatings DESC; 


/***Raters and their Ratings***/

/*k*//********displayed the top 3, as it wasn't indicated how many "highest overall ratingS" were required****/
SELECT rName, JoinDate, reputation, restoName, rateDate, SUM(Food+Mood) AS OverallRating
FROM rater
JOIN rating ON rating.UserID = rater.UserID JOIN restaurant ON restaurant.restaurantID = rating.restaurantID
GROUP BY rName, JoinDate, reputation, restoName, rateDate
ORDER BY OverallRating DESC
LIMIT 3; 

/** QUERY L) is the same as previous*****/

/*M*//** Comments are separated by comma **/
SELECT rName, COUNT(rating) AS numRatings, reputation,string_agg(rComments,',')AS Comments
FROM rating
JOIN restaurant ON restaurant.restaurantID=rating.restaurantID
JOIN rater ON rating.userID = rater.userID
WHERE restaurant.restaurantID = (
  SELECT restaurantID
  FROM restaurant 
  WHERE restaurant.restoName = 'El Camino')
GROUP BY rName, reputation
ORDER BY numRatings DESC
LIMIT 1;   

/*N*//** we dont have a rater named John, so we used the name "eater123"*/
SELECT rName, Email 
FROM rater
JOIN rating ON rating.UserID = rater.UserID
GROUP BY rName, Email
HAVING SUM(Food+Mood+Price+Staff) < 
( SELECT SUM(Food+Mood+Price+Staff) 
  FROM rater
  JOIN rating ON rating.UserID = rater.UserID
  WHERE rater.UserID = 
    (SELECT rater.UserID
     FROM rater
     WHERE rName = 'eater123')); 













	


