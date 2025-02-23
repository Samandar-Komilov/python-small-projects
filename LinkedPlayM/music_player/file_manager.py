import pathlib
import json
import eyed3

from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1


class FileManager:
    @staticmethod
    def is_valid_audio_file(path: str) -> bool:
        VALID_AUDIO_FORMATS: tuple[str] = (".mp3",)
        file: Path = Path(path)
        
        return file.suffix in VALID_AUDIO_FORMATS


    @staticmethod
    def extract_metadata(path: str) -> tuple:
        audio = eyed3.load(path)
        
        title = audio.tag.title
        artist = audio.tag.artist
        duration = audio.info.time_secs

        print(">>>", title, artist, duration)

        return title, artist, duration


    @staticmethod
    def load_songs_from_folder(folder_path: str) -> None:
        """
        [!] Scan a folder and return a list of valid song file paths.
        - string folder_path to Path object
        - check if folder exists and is folder
        - find all audio files by checking file extensions
        """

    @staticmethod
    def save_playlist(playlist_name: str, songs: list[str]) -> None:
        """Save a playlist (list of song file paths) to a JSON file."""

    @staticmethod
    def load_playlist(playlist_name: str) -> list[str]:
        """Load a playlist from a JSON file and return song paths."""
