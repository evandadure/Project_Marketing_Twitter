from Day import Day
import datetime
import time

class Week():

    def __init__(self):
        """
        Initializes the Week with 7 objects "Day" corresponding to the 7 days of the week
        ----------
        Parameters :
            - one Day per day of the week
        Returns :
            No return.
        """
        self.monday = Day("Monday")
        self.tuesday = Day("Tuesday")
        self.wednesday = Day("Wednesday")
        self.thursday = Day("Thursday")
        self.friday = Day("Friday")
        self.saturday = Day("Saturday")
        self.sunday = Day("Sunday")


    def get_day_of_the_week(self, dayNumber):
        """
        Get the day corresponding to a given number (ex : 0 = monday, 4 = friday...)
        ----------
        Parameters :
            - dayNumber(int) : the number of the day (from 0 to 6)
        Returns :
            - an object Day of the current Week
        """
        daysList = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday]
        return daysList[dayNumber]

    def fill_week(self, list_tweets):
        """
        Fills the week (= every day of the week) with a list of tweets, in order to analyze on which day or hour
        the tweets are mostly posted
        ----------
        Parameters :
            - list_tweets(List<Tweet>) : a list of tweets (containing their publication date)
        Returns :
            No return (only fills the objects Day of the current Week
        """
        for tweet in list_tweets:
            tweet_day = self.get_day_of_the_week(tweet.date.weekday())
            tweet_day.fillDay(tweet)









