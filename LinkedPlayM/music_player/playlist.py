from . import Song


class Playlist:
    def __init__(self, name: str = None):
        """Init a new empty playlist"""
        self.name = name if name else "New Playlist"
        self.head: Song | None = None
        self.tail: Song | None = None

        self.length: int = 0

    def add_song(self, path) -> None:
        pass

    def remove_song(self, title: str, artist: str = None) -> Song:
        pass

    def find_song(self, title: str = None, artist: str = None) -> list[Song] | Song | None:
        pass

    def next_song(self) -> Song | None:
        pass

    def prev_song(self) -> Song | None:
        pass

    def shuffle(self) -> None:
        pass

    def loop(self, enable: bool):
        """Enable or disable looping (convert to circular linked list)."""
        pass

    def display(self):
        """Print the playlist in order."""
        pass

    def is_empty(self) -> bool:
        pass

    def to_list(self) -> list[str] | None:
        """Convert the playlist to a list (for saving/loading)."""
        pass
    
    def __str__(self) -> str:
        return f"<Playlist ({self.name})>"
    
    def __repr__(self) -> str:
        return f"<Playlist ({self.name})>"