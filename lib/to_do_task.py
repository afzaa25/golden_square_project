def to_do(text):
    if '#TODO' not in text:
        raise Exception("this does not have a todo")
    else:
        return "This is a todo, make sure to carry out a task."