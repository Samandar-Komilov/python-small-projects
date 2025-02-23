

class Song:
    """
    - LinkedList Node - Song class
    """
    def __init__(self, title: str, artist: str, duration: int, path: str):
        # data
        self.title: str = title
        self.artist: str = artist
        self.path: str = path
        self.duration: int = duration
        # pointers
        self.next: Song | None = None
        self.prev: Song | None = None

    
    def __str__(self) -> str:
        return f"<{self.title} by {self.artist} ({self.duration})>"
    
    def __repr__(self) -> str:
        return f"<{self.title} by {self.artist} ({self.duration})>"