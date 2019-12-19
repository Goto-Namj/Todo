import user


class UserRepository(object):
    def get_by_id(self, id):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def get_by_name(self, name):
        raise NotImplementedError

    def add_user(self, user):
        raise NotImplementedError

@singleton
class InMemoryUserRepository(UserRepository):
    users = []

    def get_by_id(self, id):
        return list(filter(lambda x: x.id == id, self.users))

    def get_all(self):
        return self.users
    def get_by_name(self, name):

        return list(filter(lambda x: x.name == name, self.users))

    def add_user(self, user):
        self.users.append(user)
Todo
repo = InMemoryUserRepository()
repo.users == []
repo.add_user("las")
repo.users = ["las"]
TodoFactory
repo = InMemoryUserRepository()
repo.users == ["las"]

user_repo = UserRepository(InMemoryUserRepository())

user_repo.get_by_name()
todo = Todo()
todo_info = todo.get_info()
todo.user_id -> user -> user.name, user.login_id
todo_info.writer

todo_repo -> todo -> todo.get_info -> todo_info