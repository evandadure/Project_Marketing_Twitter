from DataParser import dataParser
from Tweet import Tweet
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
            - account : the account we wand to get the followers form (API keys)
        Returns :
            Return a dictionnary containing as the keys Ids of the followers
            and as the value a list with the name and the screen name of the user
        """
        followers = {}
        api = tweepy.API(auth)
        for page in tweepy.Cursor(api.followers, screen_name=account).pages():
            followers[page[0].id_str] = [page[0].name, page[0].screen_name]
            time.sleep(60)
        return followers

    def getTweetsOfUser(self, auth, idUser):
        """
        Uses the Search API of tweepy to get all the followers from a user defined 
        as parameter.
        ----------
        Parameters :
            - auth : the user's information (API keys)
            - account : the account we wand to get the followers form (API keys)
        Returns :
            Return a dictionnary containing as the keys Ids of the followers
            and as the value a list with the name and the screen name of the user
        """
        listTweets = []
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.user_timeline, id=idUser, tweet_mode='extended').items():
            listTweets.append(Tweet(tweet._json['id_str'], idUser, tweet._json['created_at']))
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
        for tweet in tweepy.Cursor(api.user_timeline, id='3237083798', tweet_mode='extended').items():
            data = dataParser()
            data.addToDB(tweet._json)
