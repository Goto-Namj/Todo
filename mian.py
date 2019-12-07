from todo_repository import InMemoryRepository
from todo import Todo

todo1 = Todo("Las's Todo", "Today")
todo2 = Todo("Nam's Todo", "Next Day")

repository = InMemoryRepository()
repository.add_todo(todo1)
repository.add_todo(todo2)

assert repository.get_by_date("Today") == todo1