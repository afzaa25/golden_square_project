# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._todo = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        self._todo.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [task for task in self._todo if task.complete == False]
        

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [task for task in self._todo if task.complete == True]
        
    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        for task in self._todo:
            task.complete = True
