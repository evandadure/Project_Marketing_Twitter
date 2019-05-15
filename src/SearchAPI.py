from DataParser import DataParser
from Tweet import Tweet
from Follower import Follower
import tweepy
import time


class SearchAPI:

    def getAccountsFollowers(self, auth, account):
        """
        Uses the Search API of tweepy to get all the followers from a user defined 
        as parameter.
        ----------
        Parameters :
            - auth : the user's information (API keys)
            - account : the account we want to get the followers from (API keys)
        Returns :
            Return a list containing Followers
        """
        followers = []
        api = tweepy.API(auth)
        for page in tweepy.Cursor(api.followers, screen_name=account).pages():
            followers.append(Follower(page[0].id_str, page[0].name, page[0].screen_name))
            print(page[0].id_str, page[0].name, page[0].screen_name)
            self.getTweetsOfUser(auth, page[0].screen_name)
        return followers

    def getTweetsOfUser(self, auth, screen_name):
        """
        Uses the Search API of tweepy to get all the tweets from a user defined 
        as parameter.
        ----------
        Parameters :
            - auth : the user's information (API keys)
            - idUser : the id of the user we want to get the tweets from (API keys)
        Returns :
            Return a list containing Tweets
        """
        listTweets = []
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name, count='30', tweet_mode='extended').items():
            listTweets.append(Tweet(tweet._json['id_str'], screen_name, tweet._json['created_at']))
            print(tweet._json['id_str'], screen_name, tweet._json['created_at'])
        return listTweets
        
    def getPreviousTweets(self, auth):
        """
        Uses the Search API of tweepy to get all the previous tweets. Here we want only the tweets of BGPStream.
        Only the first 3000 tweets are available.
        ----------
        Parameters :
            - auth : the user's information (API keys)
        Returns :
            No return.
        """
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.user_timeline, id='891475922', tweet_mode='extended').items():
            data = DataParser()
            data.addToDB(tweet._json)
            print(tweet._json)
