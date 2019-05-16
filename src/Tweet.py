class Tweet:
    
    def __init__(self, idTweet, idFollower, date):
        """
        Initializes the dataParser by connecting to the database.
        ----------
        Parameters :
            - idTweet(str) : The tweet's id
            - idFollower(str) : The tweet's follower's id
            - date(str/datetime) : The tweet's date
        Returns :
            No return.
        """
        self.idTweet = idTweet
        self.idFollower = idFollower
        self.date = date