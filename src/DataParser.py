from datetime import datetime
from datetime import timedelta
from Tweet import Tweet
import mysql.connector


class DataParser():

# =============================================================================
#     host="tp-epu.univ-savoie.fr",
#     port="3308",
#     user="personma",
#     passwd="rca8v7gd",
#     database="personma"
# =============================================================================

# =============================================================================
#     host = "localhost",
#     port = "3306",
#     user = "root",
#     passwd = "root",
#     database = "marketing_db"
# =============================================================================
    
    
    
    def __init__(self):
        """
        Initializes the dataParser by connecting to the database.
        ----------
        Parameters :
            No parameter.
        Returns :
            No return.
        """
        self.mydb = mysql.connector.connect(
            host = "localhost",
            port = "3306",
            user = "root",
            passwd = "root",
            database = "marketing_db"
        )
        self.mycursor = self.mydb.cursor()

    def setDateTime(self,dateTweet):
        """
        Method that converts the tweet default date format to a date format compatible with MySQL databases (Python datetime)
        For example, "Mon Apr 01 17:09:19 +0000 2019" will be converted in "2019-04-01 18:09:00" (We add one hour to the time
        because we have UTC+2 in France)
        ----------
        Parameters :
            - dateTweet (str) : the tweet's publication date (and time)
        Returns :
            - d (datetime.datetime) : a datetime object
        """
        monthsDic = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                     "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        # We're getting the day,month,year,hour and minute from the tweet time to create a new datetime
        dateToString = dateTweet[8:10] + "/" + monthsDic[dateTweet[4:7]] + "/" + dateTweet[-2:]
        d = datetime.strptime(dateToString, "%d/%m/%y")
        h = dateTweet[dateTweet.find(':') - 2:dateTweet.find(':')]
        m = dateTweet[dateTweet.find(':') + 1:dateTweet.find(':') + 3]
        d = d.replace(hour=int(h), minute=int(m))
        # We add one hour to the time because we have UTC+1 in France
        d = d + timedelta(hours=2)
        return d


    def addFollowerToDB(self, follower):
        """
        Method that adds a follower in parameter into the database (if it isnt already there)
        ----------
        Parameters :
            - follower (Follower) : the follower to add
        Returns :
            no return
        """
        val = (follower.idFollower, follower.name, follower.screen_name)
        query = "INSERT INTO follower (id_follower,name,screen_name) VALUES (%s, %s, %s)"
        try:
            self.mycursor.execute(query, val)
            self.mydb.commit()
        except:
            print("couldn't add the follower with id ",follower.idFollower," (probably already in the database)")


    def addTweetToDB(self, tweet):
        """
        Method that adds a tweet in parameter into the database (if it isnt already there)
        ----------
        Parameters :
            - tweet (Tweet) : the tweet to add
        Returns :
            no return
        """
        val = (tweet.idTweet, tweet.idFollower, self.setDateTime(tweet.date))
        query = "INSERT INTO tweet (id_tweet,id_follower,date ) VALUES (%s, %s, %s)"
        try:
            self.mycursor.execute(query, val)
            self.mydb.commit()
        except:
            print("couldn't add the tweet with id ",tweet.idTweet," (probably already in the database)")

    def getAllTweets(self):
        """
        Get all the tweets of our database
        ----------
        Parameters :
            no parameter
        Returns :
            - all_tweets(List<Tweet>) : a list of Tweet objects
        """
        query = "SELECT * FROM tweet"
        try:
            self.mycursor.execute(query)
            all_tweets=[]
            result = self.mycursor.fetchall()
            for tweet in result:
                tweet = Tweet(tweet[0], tweet[1], tweet[2])
                all_tweets.append(tweet)
            return all_tweets
        except:
            print("a problem occured while trying to get all tweets")

