import user


class UserRepositoryInterface(object):
    userlist = []

    def get_by_name(self, name):
        raise NotImplementedError

    def add_user(self, user):
        raise NotImplementedError

    def remove_user(self, user):
        raise NotImplementedError


class UserRepository(UserRepositoryInterface):
    userlist = []

    def get_by_name(self, name):
        return self.find(name)

    def add_user(self, user):
        self.userlist.append(user)

    def remove_user(self, user):
        self.userlist.remove(user)

    def find(self, name):
        find_result = list(filter(lambda x: x.name == name, self.userlist))
        return find_result[0]
