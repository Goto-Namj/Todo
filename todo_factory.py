from todo import Todo


class TodoFactoryInterface(object):
    def make_todo(self, id, date, content):
        raise NotImplementedError


class TodoFactory(TodoFactoryInterface):
    def make_todo(self, id, date, content):
        todo = Todo(id, date, content)
        return todo