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

    def make_todo(self, user_name, date, content):
        user = self.user_repository.get_by_name(user_name)
        user_id = user.id
        todo = self.todo_factory.make_todo(user_id, date, content)
        self.todo_repository.add_todo(todo)

    def get_all_user(self):
        all_user = self.user_repository.userlist
        return all_user

    def get_user_by_user_name(self, user_name):
        user_by_user_name = self.user_repository.get_by_name(user_name)
        return user_by_user_name


    def get_all_todo(self, user_name):
        user = self.user_repository.get_by_name(user_name)
        user_id = user.id
        all_todo = self.todo_repository.get_by_id(user_id)
        return all_todo

    def get_todo_by_date(self, user_name, date):
        all_todo = self.get_all_todo(user_name)
        todo_by_date = self.todo_repository.get_by_date(date, all_todo)
        return todo_by_date
