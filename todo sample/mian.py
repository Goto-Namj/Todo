from todo_repository import InMemoryRepository
from todo import Todo
from todo_factory import TodoFactory
from user import User
from user_factory import UserFactory
from user_repository import InMemoryUserRepository



TodoService().AddTodotoTodayTodoList(todo, user)
TodoService().AddTodotoTodoList(todo, user.odoService.FindList(user, ""))



las = InMemoryUserRepository().get_by_name("las")[0]
todo = TodoFactory().make_todo("project tranquility coding", important=1)

todolist = las.get_todolist_by_name()
todolist.add_todo(todo)
