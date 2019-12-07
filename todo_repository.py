import todo


class TodoRepository(object):
    def get_by_date(self, date):
       raise NotImplementedError


class InMemoryRepository(TodoRepository):
    todos = []

    def get_by_date(self, date):
        fit_todos = []
        for todo in self.todos:
            if todo.date == date:
                fit_todos.append(todo)
        return fit_todos

    def get_todos(self):
        return self.todos

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        self.todos.remove(todo)