from todo_factory import TodoFactory
from todo_repository import TodoRepository
from user_factory import UserFactory
from user_repository import UserRepository

todo_fact = TodoFactory()
todo_repo = TodoRepository()
user_fact = UserFactory()
user_repo = UserRepository()

user = user_fact.make_user("남진명")
user_repo.add_user(user)
user = user_fact.make_user("LAS")
user_repo.add_user(user)

user = user_repo.get_by_name("남진명")
user111id = user.id
user = user_repo.get_by_name("LAS")
user999id = user.id
print(user111id)

todo = todo_fact.make_todo(user111id, "2019-12-10", "7시 40분에 식사")
todo_repo.add_todo(todo)
todo = todo_fact.make_todo(user111id, "2019-12-10", "23시 30분에 취침")
todo_repo.add_todo(todo)
todo = todo_fact.make_todo(user111id, "2019-12-11", "8시 00분에 배변")
todo_repo.add_todo(todo)

todo = todo_fact.make_todo(user999id, "1999-99-99", "9시 99분에 출근")
todo_repo.add_todo(todo)
todo = todo_fact.make_todo(user999id, "2001-12-25", "00시 00분 부터 크리스마스")
todo_repo.add_todo(todo)

user111_todolist = todo_repo.get_by_id(user111id)
user999_todolist = todo_repo.get_by_id(user999id)

user111_2019_12_10_todolist = todo_repo.get_by_date("2019-12-10", user111_todolist)

for i in user111_2019_12_10_todolist:
    print(i.date, i.content)
print()
for i in user999_todolist:
    print(i.date, i.content)

print("service로 옮기면 끝")