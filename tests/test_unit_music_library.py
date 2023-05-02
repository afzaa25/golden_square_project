from lib.music_library import MusicLibrary


def test_initially_has_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []


def test_initially_searches_returns_empty():
    music_library = MusicLibrary()
    assert music_library.search_by_title("hello") == []