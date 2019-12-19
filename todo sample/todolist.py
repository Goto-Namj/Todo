class TodoList(object):
    def __init__(self, date, name):
        self.name = name
        self.todos = []
        self.date = date
    
    def add_todo(self, todo):
        self.todos.append(todo)
    
    def get_all_todo(self):
        

class TodoListFactory():
    def make_from_date(self, date):
        return TodoList(date, f"{date} - Todo List")
