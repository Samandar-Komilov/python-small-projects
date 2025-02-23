

class Song:
    """
    - LinkedList Node - Song class
    """
    def __init__(self, title, artist, duration, path):
        # data
        self.title = title
        self.artist = artist
        self.path = path
        self.duration = duration
        # pointers
        self.next = None
        self.prev = None

    
    def __str__(self):
        return f"<{self.title} by {self.artist} ({self.duration})>"
    
    def __repr__(self):
        return f"<{self.title} by {self.artist} ({self.duration})>"