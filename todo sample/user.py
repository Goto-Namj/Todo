import uuid
from todolist import TodoListFactory

class User(object):
    def __init__(self, name):
        self.id = uuid.UUID()
        self.todolists = []

    def make_todolist(self, date):
        todolist = TodoListFactory().make_from_date(date)
        self.todolists.append(todolist)

    def get_today_todolist(self):
        today_list = []
        for todolist in self.todolists:
            if todolist.date == "today":
                return todolist
        return None
    
    def get_all_todo(self):
        pass