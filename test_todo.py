from todo_repository import InMemoryRepository
from todo import Todo


def test_todo():
    # Given
    todo1 = Todo("Las's Todo", "Today")
    todo2 = Todo("Nam's Todo", "Next Day")
    repository = InMemoryRepository()

    # When
    repository.add_todo(todo1)
    repository.add_todo(todo2)

    # Then
    assert todo1 in repository.get_by_date("Today")


def test_todo_search_fail():
    # Given
    todo1 = Todo("Las's Todo", "Today")
    todo2 = Todo("Nam's Todo", "Next Day")
    repository = InMemoryRepository()

    # When
    repository.add_todo(todo1)
    repository.add_todo(todo2)

    # Then
    assert repository.get_by_date("Yesterday") == []


def test_today_have_multiple_todo():
    # Given
    todo1 = Todo("Las's Todo", "Today")
    todo2 = Todo("Nam's Todo", "Today")
    repository = InMemoryRepository()

    # When
    repository.add_todo(todo1)
    repository.add_todo(todo2)

    # Then
    assert todo1 in repository.get_by_date("Today")
    assert todo2 in repository.get_by_date("Today")


def test_todo_remove():
    # Given
    todo1 = Todo("Las's Todo", "Today")
    todo2 = Todo("Nam's Todo", "Today")
    repository = InMemoryRepository()
    repository.add_todo(todo1)
    repository.add_todo(todo2)

    # When
    repository.remove_todo(todo2)

    # Then
    assert todo1 in repository.get_by_date("Today")
    assert todo2 not in repository.get_by_date("Today")