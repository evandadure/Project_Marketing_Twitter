

class Follower:
    
    def __init__(self, idFollower, name, screen_name):
        """
        Initializes the dataParser by connecting to the database.
        ----------
        Parameters :
            No parameter.
        Returns :
            No return.
        """
        self.idFollower = idFollower
        self.name = name
        self.screen_name = screen_name