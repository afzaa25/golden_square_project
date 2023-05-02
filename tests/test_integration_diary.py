from lib.diary import Diary
from lib.diary_entry_class import DiaryEntry



"""
adds two diary entries 
i see them back in the list
"""
def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry("My Title 1", "My Contents 1")
    entry2 = DiaryEntry("My Title 1", "My Contents 2")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]


"""
Given I add two diary entries 
and I call #count_words
i get the sum of all the words in the contents of diary entries
"""

def test_count_words_returns_contents_of_all_words_in_all_entry_contents():
    diary = Diary()
    entry1 = DiaryEntry("My Title 1", "One two")
    entry2 = DiaryEntry("My Title 1", "three four five")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 5

"""
given I add two diary entries with a total length of 5
and i call reading-time with a wpm of 2
then the total readig time should be 3
"""
def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry1 = DiaryEntry("My Title 1", "One two")
    entry2 = DiaryEntry("My Title 1", "three four five")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(2) == 3  

"""
given I add two diary entries one long and one short
and i call #find_best__entry_for_reading_time
with the wpm and minutes that means i can only read the short one
the #find_best__entry_for_reading_time returns the shorter one
"""

def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("My Title 1", "One two three")
    entry2 = DiaryEntry("My Title 1", "One two three four five six seven")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1

def test_best_entry_for_reading_time_returns_entry_fits_in_time():
    diary = Diary()
    entry1 = DiaryEntry("My Title 1", "One two three")
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1


def test_best_entry_for_reading_time_returns_none_if_cannot_read():
    diary = Diary()
    entry1 = DiaryEntry("My Title 1", "One two three four five six seven")
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

def test_best_entry_for_reading_time_return_longest_entry():
    diary = Diary()
    entry1 = DiaryEntry("My Title 1", "One two three")
    entry2 = DiaryEntry("My Title 1", "One two three four five six seven")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry2