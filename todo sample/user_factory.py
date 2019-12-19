from user import User


class UserFactoryInterface(object):
    @staticmethod
    def make_user(id, password):
        raise NotImplementedError

UserFactory.make_user("las")
class UserFactory(UserFactoryInterface):
    @staticmethod
    def make_user(name):
        user = User(name, [])
        return user