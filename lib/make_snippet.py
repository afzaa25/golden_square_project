
def make_snippet(text):
    words = text.split()
    #if the length of the words is less than 5 return the text as it is
    if len(words) <= 5:
        return text
    #otherwise return 5 words with an elipssis at the end
    else:
        return " ".join(words[:5]) + "..."