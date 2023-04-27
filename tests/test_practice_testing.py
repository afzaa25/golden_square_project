import pytest
from lib.practice_testing import *

def test_divisible_by_three():
    assert divisible_by_three(15) == True
    assert divisible_by_three(14) == False

def test_divisible_by_five():
    assert divisible_by_five(25) == True
    assert divisible_by_five(24) == False

def test_add_two_numbers_together():
    assert add(5,5) == 10
    assert add(6,4) == 10

def test_subtract_one_number_from_another():
    assert subtract(10,4) == 6
    assert subtract(10, 5) == 5

def test_multiply_numbers_as_string():
    assert multiply_number_string('10', '5') == 50
    assert multiply_number_string('3', '3') == 9


"""
takes a string as an argument and returns the first five words and then a '...' if there are more than that.
"""
def test_if_string_is_empty():
    result = make_snippet("")
    assert result == ""

def test_if_string_has_four_words():
    result = make_snippet("the quick brown fox jumped")
    assert result == "the quick brown fox jumped"

def test_if_string_has_five_words():
    result = make_snippet("the quick brown fox jumped")
    assert result == "the quick brown fox jumped"

def test_if_string_has_more_than_five_words():
    result = make_snippet("the quick brown fox jumped over")
    assert result == "the quick brown fox jumped..."


def test_if_no_words_in_string():
    result = count_words('')
    assert result == 0

def count_four_words_in_strings():
    result = count_words('the quick brown fox')
    assert result == 4

def count_five_words_in_strings():
    result = count_words('the quick brown fox jumped')
    assert result == 5

