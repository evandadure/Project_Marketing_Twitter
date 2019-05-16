from tweepy import OAuthHandler
from SearchAPI import SearchAPI
from DataParser import DataParser
from Follower import Follower
from Tweet import Tweet
import json


class Main():
    if __name__ == '__main__':
        # This handles Twitter authentication and the connection to Twitter API
        # The API Key Information are stored in data/keys.json
        with open('../data/keys.json') as json_file:
            data = json.load(json_file)
        auth = OAuthHandler(data['consumer_key'], data['consumer_secret'])
        auth.set_access_token(data['access_token'], data['access_token_secret'])

    
        # Creates a new SearchAPI object and gets the previous tweets
        # dp = DataParser()
        # fol = Follower("849848","Evan Dadure","evandadure")
        # tw1 = Tweet("48941891", "849848", "Fri May 10 17:59:07 +0000 2019")
        # tw2 = Tweet("489451218", "849848", "Tue May 09 11:12:41 +0000 2019")
        # dp.addFollowerToDB(fol)
        # dp.addTweetToDB(tw1)
        # dp.addTweetToDB(tw2)
#        searchAPI.getAccountsFollowers(auth, "IAmAlanSmithee_")
#        searchAPI.getTweetsOfUser(auth, 371325036)
#        searchAPI.getPreviousTweets(auth)
        searchAPI = SearchAPI()
        searchAPI.getAccountsFollowers(auth, "mohmoassad")
