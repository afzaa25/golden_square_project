from lib.diary_entry_class import DiaryEntry

"""
when i initilise with title and contents 
i can get title and contents back
"""

def test_construst_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My title", "My Contents")
    assert diary_entry.title == "My title"
    assert diary_entry.contents == "My Contents"

"""
when i initialise with a five word contents
thwn count words should return five
"""
def test_count_words_returns_word_count_of_words():
    diary_entry = DiaryEntry("My title", "One two three four five")
    assert diary_entry.count_words() == 5


"""

"""

def test_reading_time():
    diary_entry = DiaryEntry("My title", "One two three four five")
    assert diary_entry.reading_time(2) == 3

def test_reading__first_chunk():
    diary_entry = DiaryEntry("My title", "One two three four five")
    assert diary_entry.reading_chunk(2,1) == "One two"

def test_reading__second_chunk():
    diary_entry = DiaryEntry("My title", "One two three four five")
    diary_entry.reading_chunk(2,1)
    assert diary_entry.reading_chunk(2,1) == "three four"

def test_reading__third_chunk():
    diary_entry = DiaryEntry("My title", "One two three four five")
    diary_entry.reading_chunk(2,1)
    diary_entry.reading_chunk(2,1)
    assert diary_entry.reading_chunk(2,1) == "five"

def test_reading__fourth_chunk():
    diary_entry = DiaryEntry("My title", "One two three four five")
    diary_entry.reading_chunk(2,1)
    diary_entry.reading_chunk(2,1)
    diary_entry.reading_chunk(2,1)
    assert diary_entry.reading_chunk(2,1) == "One two"


def test_reading__six_chunk():
    diary_entry = DiaryEntry("My title", "One two three four five six")
    diary_entry.reading_chunk(2,1)
    diary_entry.reading_chunk(2,1)
    diary_entry.reading_chunk(2,1)
    assert diary_entry.reading_chunk(2,1) == "One two"
