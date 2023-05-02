from lib.track import Track

"""
when we create a new track 
we can get its title and artist back
"""

def test_construct_track_and_get_tite():
    track = Track("Always The Hard Way", "Terror")
    assert track.title == "Always The Hard Way"
    assert track.artist == "Terror"

def test_format_title_and_artist():
    track = Track("Always The Hard Way", "Terror")
    assert track.format() == "Always The Hard Way by Terror"