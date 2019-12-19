from user import User


class UserFactoryInterface(object):
    def make_user(self, name):
        raise NotImplementedError

class UserFactory(UserFactoryInterface):
    def make_user(self, name):
        user = User(name)
        return user