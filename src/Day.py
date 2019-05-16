from Tweet import Tweet

class Day():

    def __init__(self, day_name):
        self.day_name = day_name
        # a timetable is composed of 12 lists representing the 12 timestamps "00-02", "02-04"..."22-00"
        self.timetable = [[],[],[],[],[],[],[],[],[],[],[],[]]

    def fillDay(self, tweet):
        """
        Add the idfollower of the tweet into the correct timetable depending on
        the hour the tweet was posted. When added, remove duplicate, so those who
        post huge amount of tweets in a short time won't have too much influence.
        ----------
        Parameters :
            - tweet : The tweet we will work. We'll insert its idFollower into 
            the correct timetable
        Returns :
            Nothing
        """
        self.timetable[tweet.date.hour//2].append(tweet.idFollower)
        #Remove the duplicate
        self.timetable[tweet.date.hour//2] = list(dict.fromkeys(self.timetable[tweet.date.hour//2]))


