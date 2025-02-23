import pathlib
import json

from . import Playlist


class FileManager:
    def load_songs_from_folder(self, folder_path: str) -> None:
        """
        [!] Scan a folder and return a list of valid song file paths.
        - string folder_path to Path object
        - check if folder exists and is folder
        - find all audio files by checking file extensions
        - 
        """

    def save_playlist(self, playlist_name: str, songs: list[str]) -> None:
        """Save a playlist (list of song file paths) to a JSON file."""

    def load_playlist(self, playlist_name: str) -> list[str]:
        """Load a playlist from a JSON file and return song paths."""

    def is_valid_audio_file(self, path: str) -> bool:
        """Check if a file is a valid audio format (MP3, WAV, etc.)."""