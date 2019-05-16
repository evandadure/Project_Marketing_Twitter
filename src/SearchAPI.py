from DataParser import DataParser
from Tweet import Tweet
from Follower import Follower
import tweepy
import time


class SearchAPI:
    
    def __init__(self):
        self.dp = DataParser() 
        
    
    def getAccountsFollowers(self, auth, account):
        """
        Uses the Search API of tweepy to get all the followers from a user defined 
        as parameter, and insert it into the database.
        ----------
        Parameters :
            - auth : the user's information (API keys)
            - account : the account we want to get the followers from (API keys)
        Returns :
            Nothing
        """
        api = tweepy.API(auth)
        for page in tweepy.Cursor(api.followers, screen_name=account).pages():
            follower = Follower(page[0].id_str, page[0].name, page[0].screen_name)
            print("ID: " + follower.idFollower + "\nName: " + follower.name + "\nScreen_Name: " + follower.screen_name)
            self.dp.addFollowerToDB(follower)
            self.getTweetsOfUser(auth, follower.idFollower)
            time.sleep(60)

    def getTweetsOfUser(self, auth, idUser):
        """
        Uses the Search API of tweepy to get all the tweets from a user defined 
        as parameter, and insert them into the database.
        ----------
        Parameters :
            - auth : the user's information (API keys)
            - idUser : the id of the user we want to get the tweets from (API keys)
        Returns :
            Nothing
        """
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.user_timeline, user_id=idUser, count='30', tweet_mode='extended').items():
            tweet = Tweet(tweet._json['id_str'], idUser, tweet._json['created_at'])
            print("ID : " + tweet.idTweet + "\nIDFollower: " + tweet.idFollower + "\nDate: " + tweet.date)
            self.dp.addTweetToDB(tweet)

