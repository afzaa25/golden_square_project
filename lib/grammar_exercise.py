'''
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
'''

def check_sentence_grammar(text):
    return text[0].isupper() and text[-1] in '.?!'

