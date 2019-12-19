import uuid


class User(object):
    def __init__(self, name):
        self.id = uuid.UUID(uuid.uuid4().hex)
        self.name = name
