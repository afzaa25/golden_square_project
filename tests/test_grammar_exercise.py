from lib.grammar_exercise import *



def test_with_valid_sentence():
    result = check_sentence_grammar("Hello, this is a fine day.")
    assert result == True


def test_with_capital_letter_but_no_fullstop():
    result = check_sentence_grammar("Hello, this is a fine day")
    assert result == False

def test_with_capital_letter_and_question_mark():
    result = check_sentence_grammar("Hello, this is a fine day?")
    assert result == True

def test_with_capital_letter_and_exclamation_mark():
    result = check_sentence_grammar("Hello, this is a fine day!")
    assert result == True

def test_with_capital_letter_and_exclamation_mark():
    result = check_sentence_grammar("Hello, this is a fine day,")
    assert result == False

def test_with_capital_letter_and_exclamation_mark():
    result = check_sentence_grammar("Hello, this is a fine day:")
    assert result == False

def test_with_lowercase_letter_and_fullstop():
    result = check_sentence_grammar("hello, this is a fine day.")
    assert result == False
