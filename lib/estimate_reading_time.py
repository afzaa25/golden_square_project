def estimate_reading_time(text):
    if text == '':
        raise Exception("Can't estimate reading time for an empty text.")
    else:
        words = text.split()
        word_count = len(words)
        return word_count / 200