from lib.grammar_stats import *

def test_with_valid_sentence():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is a fine day.")
    assert result == True

def test_with_capital_letter_but_no_fullstop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is a fine day")
    assert result == False

def test_with_capital_letter_and_question_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is a fine day?")
    assert result == True

def test_with_capital_letter_and_exclamation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is a fine day!")
    assert result == True

def test_with_capital_letter_and_exclamation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is a fine day,")
    assert result == False

def test_with_capital_letter_and_exclamation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, this is a fine day:")
    assert result == False

def test_with_lowercase_letter_and_fullstop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello, this is a fine day.")
    assert result == False

# def test_for_good_percentage():
#     grammar_stats = GrammarStats()
#     grammar_stats.check("This is a good sentence.")
#     grammar_stats.check("This is not a good sentence.")
#     grammar_stats.check("Another good one!")
#     result = grammar_stats.percentage_good(66)
#     assert result == 66
