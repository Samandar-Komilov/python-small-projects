from . import Song


class HistoryList:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity

    def add_to_history(self) -> None:
        """Add a song to history (remove oldest if over capacity)."""
        pass

    def get_recent_played_songs(self) -> list[Song] | None:
        pass

    def clear_history(self) -> None:
        pass

    def list_history(self) -> list[str] | None:
        pass
    

    def __str__(self) -> str:
        return f"<HistoryList: capacity={self.capacity}>"
    
    def __str__(self) -> str:
        return f"<HistoryList: capacity={self.capacity}>"