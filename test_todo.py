from todo import Todo
from todo_factory import TodoFactory
from todo_repository import TodoRepository
from user import User
from user_factory import UserFactory
from user_repository import UserRepository
from service import Service
import time


def test_make_user():
    # Given
    service = Service()
    user_name = "남진명"

    # When
    service.make_user(user_name)

    # Then
    user_id = service.user_repository.get_by_name(user_name).id
    user = service.user_repository.get_by_name(user_name)
    assert isinstance(user, User)
    assert user.id == user_id
    assert user.name == user_name


def test_make_todo():
    # Given
    service = Service()
    user_name = "남진명"
    service.make_user(user_name)
    date = "2019-12-10"
    content = "7시 40분 부터 8시 30분까지 식사"
    user_id = service.user_repository.get_by_name(user_name).id
    
    # When
    service.make_todo(user_name, date, content)

    # Then
    todo = service.todo_repository.get_by_id(user_id)[0]
    assert isinstance(todo, Todo)
    assert todo.id == user_id
    assert todo.date == date
    assert todo.content == content


def test_get_all_user():
    # Given
    service = Service()
    user_name = "남진명"
    service.make_user(user_name)
    user_id = service.user_repository.get_by_name(user_name).id

    # When
    all_user = service.get_all_user()

    # Then
    user = all_user[0]
    assert isinstance(user, User)
    assert user.id == user_id
    assert user.name == user_name


def test_get_user_by_user_name():
    # Given
    service = Service()
    user_name = "남진명"
    service.make_user(user_name)
    user_id = service.user_repository.get_by_name(user_name).id

    # When
    user_by_user_name = service.get_user_by_user_name(user_name)

    # Then
    user = user_by_user_name
    assert isinstance(user, User)
    assert user.id == user_id
    assert user.name == user_name


def test_get_all_todo():
    # Given
    service = Service()
    user_name = "남진명"
    service.make_user(user_name)
    date = "2019-12-10"
    content = "7시 40분 부터 8시 30분까지 식사"
    service.make_todo(user_name, date, content)
    user_id = service.user_repository.get_by_name(user_name).id

    # When
    all_todo = service.get_all_todo(user_name)
    
    # Then
    todo = all_todo[0]
    assert isinstance(todo, Todo)
    assert todo.id == user_id
    assert todo.date == date
    assert todo.content == content


def test_get_todo_by_date():
    # Given
    service = Service()
    user_name = "남진명"
    service.make_user(user_name)
    date = "2019-12-10"
    content = "7시 40분 부터 8시 30분까지 식사"
    service.make_todo(user_name, date, content)
    user_id = service.user_repository.get_by_name(user_name).id

    # When
    todo_by_date = service.get_todo_by_date(user_name, date)
    
    # Then
    todo = todo_by_date[0]
    assert isinstance(todo, Todo)
    assert todo.id == user_id
    assert todo.date == date
    assert todo.content == content