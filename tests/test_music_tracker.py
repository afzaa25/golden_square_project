import pytest
from lib.music_tracker import *


"""
initially there are no songs
"""
def test_returns_empty_list_if_no_songs_added():
    music_tracker = MusicTracker()
    assert music_tracker.music_list()  == []


"""
Given an empty string
it raises an error
"""
def test_raises_error_if_empty_string():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add('')
    error_message = str(e.value)
    assert error_message == "You have not set a song."


"""
when a song is added
it will be reflected in the list of songs
"""
def test_if_one_song_has_been_added():      
    music_tracker = MusicTracker()
    music_tracker.add('Calm Down by Rema')
    assert music_tracker.music_list() == ['Calm Down by Rema']

"""
when multiple songs are added
it will be reflected in the list of songs
"""
def test_if_multiple_songs_have_been_added():
    music_tracker = MusicTracker()
    music_tracker.add('Calm Down by Rema')
    music_tracker.add('Peru by Fireboy DML')
    music_tracker.add('Unforgettable by French Montana, Swae Lee')
    assert music_tracker.music_list() == ['Calm Down by Rema', 'Peru by Fireboy DML', 'Unforgettable by French Montana, Swae Lee']