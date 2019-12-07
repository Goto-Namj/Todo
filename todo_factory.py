from todo import Todo
import time


class TodoFactory(Todo):
    def __init__(self, name, date = "default"):
        self.name = name
        if date == "default":
            date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.date = date