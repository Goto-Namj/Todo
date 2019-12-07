from todo_repository import InMemoryRepository
from todo_factory import TodoFactory
from todo import Todo
import time


def test_todo():
    # Given
    todo1 = Todo("Las's Todo", "2020-12-30")
    todo2 = Todo("Nam's Todo", "2020-12-31")
    repository = InMemoryRepository()

    # When
    repository.add_todo(todo1)
    repository.add_todo(todo2)

    # Then
    assert todo1 in repository.get_by_date("2020-12-30")


def test_todo_search_fail():
    # Given
    todo1 = Todo("Las's Todo", "2020-12-30")
    todo2 = Todo("Nam's Todo", "2020-12-31")
    repository = InMemoryRepository()

    # When
    repository.add_todo(todo1)
    repository.add_todo(todo2)

    # Then
    assert repository.get_by_date("2020-12-29") == []


def test_today_have_multiple_todo():
    # Given
    todo1 = Todo("Las's Todo", "2020-12-30")
    todo2 = Todo("Nam's Todo", "2020-12-30")
    repository = InMemoryRepository()

    # When
    repository.add_todo(todo1)
    repository.add_todo(todo2)

    # Then
    assert todo1 in repository.get_by_date("2020-12-30")
    assert todo2 in repository.get_by_date("2020-12-30")


def test_todo_remove():
    # Given
    todo1 = Todo("Las's Todo", "2020-12-30")
    todo2 = Todo("Nam's Todo", "2020-12-30")
    repository = InMemoryRepository()
    repository.add_todo(todo1)
    repository.add_todo(todo2)

    # When
    repository.remove_todo(todo2)

    # Then
    assert todo1 in repository.get_by_date("2020-12-30")
    assert todo2 not in repository.get_by_date("2020-12-30")


def test_todofactory():
    # Given
    factory = TodoFactory()

    # When
    todo1 = factory.make_todo("Las's Todo", "2020-12-30")
    
    # Then
    assert isinstance(todo1, Todo)


def test_dateparameter_empty():
    # Given
    factory = TodoFactory()

    # When
    todo1 = factory.make_todo("Las's Todo")
    
    # Then
    now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    assert todo1.date == now_date

    
def test_todo_set_past_day():
    # Given
    factory = TodoFactory()

    # When, Then
    try:
        todo1 = factory.make_todo("Las's Todo", "1000-12-30")
        assert False
    except:
        assert True