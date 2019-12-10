class TodoRepositoryInterface(object):
   todolist = []

   def get_by_id(self, id):
      raise NotImplementedError

   def get_by_date(self, date, todolist):
      raise NotImplementedError

   def add_todo(self, todo):
      raise NotImplementedError

   def remove_todo(self, todo):
      raise NotImplementedError


class TodoRepository(TodoRepositoryInterface):
   todolist = []

   def get_by_id(self, id):
      # 이렇게 해놓고 로그인한 사용자의 id에 맞는 todolist가져와서 다른 get_by에서 활용한다.
      return list(filter(lambda x: x.id == id, self.todolist))

   def get_by_date(self, date, todolist):
      return list(filter(lambda x: x.date == date, todolist))

   def add_todo(self, todo):
      self.todolist.append(todo)

   def remove_todo(self, todo):
      self.todolist.remove(todo)
