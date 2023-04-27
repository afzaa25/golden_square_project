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
