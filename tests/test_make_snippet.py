
# A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.
#
from lib.make_snippet import *

def test_if_string_is_empty():
    result = make_snippet("")
    assert result == ""

def test_if_string_has_four_words():
    result = make_snippet("the quick brown fox jumped")
    assert result == "the quick brown fox jumped"

def test_if_string_has_five_words():
    result = make_snippet("the quick brown fox jumped")
    assert result == "the quick brown fox jumped"

#test to see if the text has morw than 5 words to add elipsis at the end
def test_if_string_has_more_than_five_words():
    result = make_snippet("the quick brown fox jumped over")
    assert result == "the quick brown fox jumped..."



