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
        api = tweepy.API(auth)
        dp = DataParser()
        for page in tweepy.Cursor(api.followers, screen_name=account).pages():
            # followers.append(Follower(page[0].id_str, page[0].name, page[0].screen_name))
            print(page[0].id_str, page[0].name, page[0].screen_name)
            dp.addFollowerToDB(Follower(page[0].id_str, page[0].name, page[0].screen_name))
            self.getTweetsOfUser(auth, page[0].id_str,dp)
            time.sleep(10)
        # return followers

    def getTweetsOfUser(self, auth, idUser, dp):
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
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.user_timeline, user_id=idUser, count='30', tweet_mode='extended').items():
            dp.addTweetToDB(Tweet(tweet._json['id_str'], idUser, tweet._json['created_at']))
            print(tweet._json['id_str'], idUser, tweet._json['created_at'])

