import pytest
from main import Interval


# запуск тестов:
# pytest имя файла
def test_empty():
    i = Interval(None, None)
    assert i.empty() == True


def test_empty_2():
    i = Interval(4, 8)
    assert i.empty() == False
