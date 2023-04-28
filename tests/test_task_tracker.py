import pytest
from lib.task_tracker import *

"""
initially there are no tasks
"""
def test_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []


"""
when we add a task
it is reflected in the list of tasks
"""
def test_add_task_reflected_in_task():
    tracker = TaskTracker()
    tracker.add("play with cat")
    assert tracker.list_incomplete() == ['play with cat']



"""
when we add multiple tasks
it is reflected in the list of tasks
"""
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("play with cat")
    tracker.add("work")
    tracker.add("assingment")
    tracker.list_incomplete # => ['play with cat', 'work', 'assingment']

"""
when we add multiple tasks
and mark one as complete
it disappears
"""
def test_marks_task_as_complete():
    tracker = TaskTracker()
    tracker.add("play with cat")
    tracker.add("work")
    tracker.add("assingment")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ['play with cat', 'assingment']



""" if we try to mark a track that does not exist
it raises an error
"""
def test_mark_task_not_exist_too_low():
    tracker = TaskTracker()
    tracker.add("play with cat")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(-1) # raise an error
        assert str(e.value) == "No such task to mark complete"
        assert tracker.list_incomplete() == ['play with cat']

""" if we try to mark a track that does not exist
it raises an error
"""
def test_mark_task_not_exist_too_high():
    tracker = TaskTracker()
    tracker.add("play with cat")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(1) # raise an error
    assert str(e.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ['play with cat']
