# Task Tracker class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my tasks
> I want a program that I can add todo tasks to and see a list of them.
> As a user
> So that I can focus on tasks to complete
> I want to mark tasks as complete and have them disappear from the list.


## 2. Design the class interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

# EXAMPLE

class TaskTracker():
    def add(self, task):
        #Parameters
        #       task: string, representing a task
    pass

    def list_incomplete(self):
        #returns
        #a list of incomplete tasks

    def mark_complete(self,index):
        # parameters:
        index: an integer representing the task to complete
        side effect:
        removes the task at index from the list of the tasks

        pass








## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

# EXAMPLE

"""
initially there are no tasks
"""
tracker = TaskTracker():
tracker.list_incomplete() # => []


"""
when we add a task
it is reflected in the list of tasks
"""

tracker = TaskTracker():
tracker.add("play with cat")
tracker.list_incomplete # => ['play with cat']



"""
when we add multiple tasks
it is reflected in the list of tasks
"""

tracker = TaskTracker():
tracker.add("play with cat")
tracker.add("work")
tracker.add("assingment")
tracker.list_incomplete # => ['play with cat', 'work', 'assingment']

"""
when we add multiple tasks
and mark one as complete
it disappears
"""

tracker = TaskTracker():
tracker.add("play with cat")
tracker.add("work")
tracker.add("assingment")
tracker.mark_complete(1)
tracker.list_incomplete # => ['play with cat', 'assingment']



""" if we try to mark a track that does not exist
it raises an error
"""

tracker = TaskTracker():
tracker.add("play with cat")
tracker.mark_complete(-1) # raise an error
tracker.list_incomplete # => ['play with cat', 'assingment']

""" if we try to mark a track that does not exist
it raises an error
"""

tracker = TaskTracker():
tracker.add("play with cat")
tracker.mark_complete(2) # raise an error
tracker.list_incomplete # => ['play with cat', 'assingment']



## 4. Implement the behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._