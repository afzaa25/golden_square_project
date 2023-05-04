from lib.todo_list import TodoList

"""
initially there are no tasks
"""
def test_has_no_tasks():
    tracker = TodoList()
    assert tracker.incomplete() == []
