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
        searchAPI = SearchAPI()
        searchAPI.getAccountsFollowers(auth, "mohmoassad")

