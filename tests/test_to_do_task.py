import pytest
from lib.to_do_task import *

def test_has_no_to_do():
    with pytest.raises(Exception) as e:
        result = to_do("i have this to do")
    error_message = str(e.value)
    assert error_message == "this does not have a todo"

def test_has_a_to_do():
    result = to_do("#TODO this is a task i need to do")
    assert result == "This is a todo, make sure to carry out a task."