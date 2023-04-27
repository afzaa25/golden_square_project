import pytest
from lib.diary_entry_solution import *

"""
given empty title and contents
raises an error
"""

def test_errors_on_empty_title():
    with pytest.raises(Exception) as e:
        DiaryEntry('', 'contents')
    assert str(e.value) == "Diary entries must have title and contents"

def test_errors_on_empty_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry('title', '')
    assert str(e.value) == "Diary entries must have title and contents"

"""
given a title and its contents
format returns a formatted entry like:
#   "My Title: These are the contents"
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == ("My Title: Some contents")


"""
given a title and contents 
returns number of words
"""

def test_counts_words_in_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4


def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntry("My Title", "Some contents have been")
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "Some contents have")
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_time_with_zero_wpm():
    diary_entry = DiaryEntry("My Title", "Some contents have")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "Cannot calculate reading time with wpm of 0"


"""
given contentsw of six words
wpm of 2
and a minute of 1
reading chunk returns first two words

"""
def test_reading_chunk_with_two_wpm_and_one_minutes():
    diary_entry = DiaryEntry("My Title", "Some contents have been written so")
    result = diary_entry.reading_chunk(2,1)
    assert result  == "Some contents"


"""
given contentsw of six words
wpm of 2
and a minute of 1
reading chunk returns first four words

"""
def test_reading_chunk_with_two_wpm_and_one_minutes():
    diary_entry = DiaryEntry("My Title", "Some contents have been written so")
    result = diary_entry.reading_chunk(2,2)
    assert result  == "Some contents have been"

"""
given a contents of six words
and a wpm of 2 and 1 minute
first time returns first two words
next time the next two words
"""

def test_reading_chunk_with_two_wpm_and_one_called_multple():
    diary_entry = DiaryEntry("My Title", "Some contents have been written so")
    assert diary_entry.reading_chunk(2,1) == "Some contents"
    assert diary_entry.reading_chunk(2,1) == "have been"
    assert diary_entry.reading_chunk(2,1) == "written so"

"""
given a contents six words
if reading chunk is called repeatedly
the last chunk is the last words in the text
blahblah"""

def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntry("My Title", "Some contents have been written so")
    assert diary_entry.reading_chunk(2,2) == "Some contents have been"
    assert diary_entry.reading_chunk(2,2) == "written so"
    assert diary_entry.reading_chunk(2,2) == "Some contents have been"


def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntry("My Title", "Some contents have been written so")
    assert diary_entry.reading_chunk(2,2) == "Some contents have been"
    assert diary_entry.reading_chunk(2,1) == "written so"
    assert diary_entry.reading_chunk(2,2) == "Some contents have been"

