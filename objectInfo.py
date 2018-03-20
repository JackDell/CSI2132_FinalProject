class Rater:
    def __init__(self, UserId, Email, rName, Password, JoinDate, rType, Reputation):
        self.UserId = UserId
        self.Email = Email
        self.rName = rName
        self.Password = Password
        self.JoinDate = JoinDate
        self.rType = rType
        self.Reputation = Reputation

class Restaurant:
    def __init__(self, RestaurantId, RestName, RestType, URL, ManagerName, OpeningDate):
        self.RestaurantId = RestaurantId
        self.RestName = RestName
        self.RestType = RestType
        self.URL = URL
        self.ManagerName = ManagerName
        self.OpenngDate = OpeningDate

class Rating:
    def __init__(self, UserId, RateDate, Price, Food, Mood, Staff, rComments, RestaurantId):
        self.UserId = UserId
        self.RateDate = RateDate
        self.Price = Price
        self.Food = Food
        self.Mood = Mood
        self.Staff = Staff
        self.rComments = rComments
        self.RestaurantId = RestaurantId

class Hours:
    def __init__(self, RestaurantId, DayOfTheWeek, OpenTime, CloseTime):
        self.RestaurantId = RestaurantId
        self.DayOfTheWeek = DayOfTheWeek
        self.OpenTime = OpenTime
        self.CloseTime = CloseTime

class MenuItem:
    def __init__(self, ItemId, ItemName, Category, ItemType, ItemPrice, RestaurantId):
        self.ItemId = ItemId
        self.ItemName = ItemName
        self.Category = Category
        self.ItemType = ItemType
        self.ItemPrice = ItemPrice
        self.RestaurantId = RestaurantId

class Rating:
    def __init__(self, UserId, ItemRateDate, ItemId, Rating, Comment):
        self.UserId = UserId
        self.ItemRateDate = ItemRateDate
        self.ItemId = ItemId
        self.Rating = Rating
        self.Comment = Comment
