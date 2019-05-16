

class Follower:
    
    def __init__(self, idFollower, name, screen_name):
        """
        Initializes the follower by specifying an id, a name and a screen name.
        ----------
        Parameters :
            - idFollower(str) : the id of the follower
            - name(str) : the name of the follower
            - screen_name(str) : the screen name of the follower
        Returns :
            No return.
        """
        self.idFollower = idFollower
        self.name = name
        self.screen_name = screen_name