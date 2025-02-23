
from .file_manager import FileManager
from .song import Song


class Playlist:
    def __init__(self, name: str = None):
        """Init a new empty playlist"""
        self.name = name if name else "New Playlist"
        self.head: Song | None = None
        self.tail: Song | None = None

        self.length: int = 0

    def add_song(self, path) -> None:
        is_valid = FileManager.is_valid_audio_file(path)

        if not is_valid:
            print(f"Error: {path} is not a valid audio file.")
            return
        
        title, artist, duration = FileManager.extract_metadata(path)
        new_song = Song(
            title=title,
            artist=artist,
            duration=duration,
            path=path
        )

        if self.head is None or self.tail is None:
            self.head = new_song
            self.tail = new_song

        self.tail.next = new_song
        self.head.prev = new_song

        self.length += 1

        print(f"Added {title} by {artist} ({duration})")

        return None

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