class Tweet:
    
    def __init__(self, idTweet, idFollower, date):
        """
        Initializes the dataParser by connecting to the database.
        ----------
        Parameters :
            No parameter.
        Returns :
            No return.
        """
        self.idTweet = idTweet
        self.idFollower = idFollower
        self.date = date