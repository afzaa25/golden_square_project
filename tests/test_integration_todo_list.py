from lib.todo_list import TodoList
from lib.todo import Todo

"""
When we add two tasks
We get the tasks back in the task list
"""
def test_adds_multiple_tasks_and_lists_them_as_incomplete():
    todo_list = TodoList()
    task_1 = Todo("Take out the laundry")
    task_2 = Todo("Wash the dishes")
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.incomplete() == [task_1, task_2]

"""

"""
def test_marks_tests_as_complete_and_removes_incompletes():
    todo_list = TodoList()
    task_1 = Todo("Take out the laundry")
    task_2 = Todo("Wash the dishes")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    assert todo_list.incomplete() == [task_2]


def test_marks_tests_as_complete_and_appears_in_complete():
    todo_list = TodoList()
    task_1 = Todo("Take out the laundry")
    task_2 = Todo("Wash the dishes")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    assert todo_list.complete() == [task_1]
    assert todo_list.incomplete() == [task_2]

def test_marks_all_tasks_as_complete():
    todo_list = TodoList()
    task_1 = Todo("Take out the laundry")
    task_2 = Todo("Wash the dishes")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.give_up()
    # task_1.mark_complete()
    # task_2.mark_complete()
    assert todo_list.complete() == [task_1, task_2]
