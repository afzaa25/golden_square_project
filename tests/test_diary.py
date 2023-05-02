import pytest
from lib.diary import Diary

"""
initially has empty list of diaries
"""
def test_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []


"""
initially word count is zero
"""
def test_initially_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0

"""
initially #reading-time should raise an error
"""
def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    assert str(e.value) == "No entries added yet."

"""
iitially should raise an error
"""
def test_initially_best_entry_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(2,2)
    assert str(e.value) == "No entries added yet"
