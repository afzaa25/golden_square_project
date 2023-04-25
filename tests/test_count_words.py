from lib.count_words import *
# A function called count_words that takes a string as an argument and returns the number of words in that string.

def test_if_string_is_empty():
    result = count_words("")
    assert result == 0

def test_count_number_of_words():
    result = count_words("the quick brown fox")
    assert result == 4
