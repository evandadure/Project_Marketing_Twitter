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
        self.daysList = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday]

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
            tweet_day = self.daysList[tweet.date.weekday()]
            tweet_day.fillDay(tweet)

    def get_days_activity(self, nbFollowers):
        """
        Display the percentage of active users on each day of the week
        ----------
        Parameters :
            - nbFollowers(int) : the total number of followers
        Returns :
            Nothing (displaying method)
        """
        daysDict = {}
        for day in self.daysList:
            daysDict[day.day_name] = int((len(day.getFollowersOfTheDay())/nbFollowers)*100)
        # sort the days by activity rate, by ascending order
        daysDict = sorted(daysDict.items(), key=lambda x: x[1])
        # sort the days by activity rate, by descending order
        daysDict.reverse()
        print("Percentage of active users on each day of the week :")
        for day,rate in daysDict:
            print(day+" : "+str(rate)+"% of users")












