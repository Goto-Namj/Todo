from service import Service


service = Service()

service.make_user("남진명")
service.make_user("LAS")

service.make_todo("남진명", "2019-12-10", "7시 40분 부터 8시 30분까지 식사")
service.make_todo("남진명", "2019-12-10", "23시 30분에 취침")
service.make_todo("남진명", "2019-12-11", "8시에 배변")

service.make_todo("LAS", "1999-99-99", "9시 99분에 출근")
service.make_todo("LAS", "2001-12-25", "크리스마스")

user1_todolist = service.get_all_todo("남진명")
user2_todolist = service.get_all_todo("LAS")

user1_2019_12_10_todolist = service.get_todo_by_date("2019-12-10", "남진명")

for i in user1_2019_12_10_todolist:
    print(i.date, i.content)
print()
for i in user2_todolist:
    print(i.date, i.content)
