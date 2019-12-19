import todo


class TodoRepository(object):
    def get_by_date(self, date):
       raise NotImplementedError

    def get_all(self):
       raise NotImplementedError

    def add_todo(self, todo):
       raise NotImplementedError

    def remove_todo(self, todo):
       raise NotImplementedError

    def get_by_user(self, user):
       raise NotImplementedError


class InMemoryRepository(TodoRepository):
    def get_by_date(self, date):
       raise NotImplementedError

    def get_todos(self):
       raise NotImplementedError

    def add_todo(self, todo):
       raise NotImplementedError

    def remove_todo(self, todo):
       raise NotImplementedError
