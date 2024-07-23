import pytest

from main import BooksCollector


@pytest.fixture(scope='function')  # создаем экземпляр (объект) класса BooksCollector
def collector():
    collector = BooksCollector()
    return collector
