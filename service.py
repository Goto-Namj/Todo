from todo_factory import TodoFactory
from todo_repository import TodoRepository
from user_factory import UserFactory
from user_repository import UserRepository


class ServiceInterface(object):
    def __init__(self):
        raise NotImplementedError

    def make_user(self, user_name):
        raise NotImplementedError

    def make_todo(self, user_name, date, do):
        raise NotImplementedError

    def get_all_todo(self, user_name):
        raise NotImplementedError

    def get_todo_by_date(self, user_name, date):
        raise NotImplementedError


class Service(ServiceInterface):
    def __init__(self):
        self.todo_factory = TodoFactory()
        self.todo_repository = TodoRepository()
        self.user_factory = UserFactory()
        self.user_repository = UserRepository()

    def make_user(self, user_name):
        user = self.user_factory.make_user(user_name)
        self.user_repository.add_user(user)

    def make_todo(self, user_name, date, do):
        user = self.user_repository.get_by_name(user_name)
        user_id = user.id
        todo = self.todo_factory.make_todo(user_id, date, do)
        self.todo_repository.add_todo(todo)

    def get_all_todo(self, user_name):
        user = self.user_repository.get_by_name(user_name)
        user_id = user.id
        user_all_todo = self.todo_repository.get_by_id(user_id)
        return user_all_todo

    def get_todo_by_date(self, user_name, date):
        user_all_todo = self.get_all_todo(user_name)
        user_todo_by_date = self.todo_repository.get_by_date(date, user_all_todo)
        return user_todo_by_date
