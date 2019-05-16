from DataParser import DataParser
from Tweet import Tweet
from Follower import Follower
import tweepy
import time


class SearchAPI:

    def getAccountsFollowers(self, auth, screenName):
        """
        Uses the Search API of tweepy to get all the followers from a user defined 
        as parameter.
        ----------
        Parameters :
            - auth : the user's information (API keys)
            - screenName : the screen name of the account we want to get the followers from (API keys)
        Returns :
            Return a list containing Followers
        """
        api = tweepy.API(auth)
        dp = DataParser()
        for page in tweepy.Cursor(api.followers, screen_name=screenName).pages():
            print(page[0].id_str, page[0].name, page[0].screen_name)
            # adds the current follower in the database
            dp.addFollowerToDB(Follower(page[0].id_str, page[0].name, page[0].screen_name))
            # adds the 30 last tweets/retweets of the current follower in the database
            self.getTweetsOfUser(auth, page[0].id_str,dp)
            # sleeps 60 sec to overpass the rate limit
            time.sleep(60)

    def getTweetsOfUser(self, auth, idUser, dp):
        """
        Uses the Search API of tweepy to get all the tweets from a user defined 
        as parameter.
        ----------
        Parameters :
            - auth : the user's information (API keys)
            - idUser : the id of the user we want to get the tweets from
            - dp (DataParser) : the DataParser used to add stuff in our database
        Returns :
            No return
        """
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.user_timeline, user_id=idUser, count='30', tweet_mode='extended').items():
            # adds the current tweet in the database
            dp.addTweetToDB(Tweet(tweet._json['id_str'], idUser, tweet._json['created_at']))
            print(tweet._json['id_str'], idUser, tweet._json['created_at'])

