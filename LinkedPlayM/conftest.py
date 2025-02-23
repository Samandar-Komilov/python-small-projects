import pytest

from music_player import Playlist


@pytest.fixture
def playlist():
    return Playlist()