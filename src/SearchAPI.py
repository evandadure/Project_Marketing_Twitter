from DataParser import DataParser
from Tweet import Tweet
from Follower import Follower
import tweepy
import time


class SearchAPI:
    
    def __init__(self):
        self.dp = DataParser() 
        
    
    def getAccountsFollowers(self, auth, screenName):
        """
        Uses the Search API of tweepy to get all the followers from a user defined 
        as parameter, and insert it into the database.
        ----------
        Parameters :
            - auth(OAuthHandler) : the user's information (API keys)
            - screenName(str) : the screen name of the account we want to get the followers from
        Returns :
            Nothing
        """
        api = tweepy.API(auth, wait_on_rate_limit=True)
        for page in tweepy.Cursor(api.followers, screen_name=screenName).pages():
            follower = Follower(page[0].id_str, page[0].name, page[0].screen_name)
            print("ID: " + follower.idFollower + "\nName: " + follower.name + "\nScreen_Name: " + follower.screen_name)
            # adds the current follower in the db
            self.dp.addFollowerToDB(follower)
            # adds all tweets of the current follower in the db
            self.getTweetsOfUser(auth, follower.idFollower)
            # waits 60 sec to overpass the rate limit
            time.sleep(60)

    def getTweetsOfUser(self, auth, idUser):
        """
        Uses the Search API of tweepy to get all the tweets from a user defined 
        as parameter, and insert them into the database.
        ----------
        Parameters :
            - auth(OAuthHandler) : the user's information (API keys)
            - idUser(str) : the id of the user we want to get the tweets from
        Returns :
            No return
        """
        api = tweepy.API(auth, wait_on_rate_limit=True)
        for tweet in tweepy.Cursor(api.user_timeline, user_id=idUser, count='30', tweet_mode='extended').items():
            tweet = Tweet(tweet._json['id_str'], idUser, tweet._json['created_at'])
            print("ID : " + tweet.idTweet + "\nIDFollower: " + tweet.idFollower + "\nDate: " + tweet.date)
            # adds the current tweet in the database
            self.dp.addTweetToDB(tweet)

