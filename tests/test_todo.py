from lib.todo import Todo

def test_is_initially_incomplete():
    todo = Todo("Do the laundry")
    assert todo.complete == False


def test_is_complete():
    todo = Todo("Do the laundry")
    todo.mark_complete()
    assert todo.complete == True

