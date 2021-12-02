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


def test_point_in_interval():
    i = Interval(4, 12)
    point = 5
    assert i.point_in_interval(point) == True


def test_eq():
    a = Interval(4, 10)
    b = Interval(4, 10)
    assert a == b


range_cross_data = [
    (Interval(2, 8), Interval(3, 5), Interval(3, 5)),
    (Interval(4, 7), Interval(1, 3), Interval(None, None)),
    (Interval(4, 9), Interval(5, 11), Interval(5, 9)),
]


@pytest.mark.parametrize("interval1, interval2, expected_result", range_cross_data)
def test_cross(interval1, interval2, expected_result):
    assert interval1.cross(interval2) == expected_result


empty = [
    (Interval(None, None), True),
    (Interval(4, 7), False),
]


@pytest.mark.parametrize("interval1, expected_result", empty)
def test_cross(interval1, expected_result):
    assert interval1.empty() == expected_result


equal = [
    (Interval(1, 5), Interval(1, 5), True),
    (Interval(4, 7), Interval(2, 8), False),

]


@pytest.mark.parametrize("interval1, interval2, expected_result", equal)
def test_cross(interval1, interval2, expected_result):
    assert interval1.__eq__(interval2) == expected_result

point_in_interval = [
    (Interval(1, 5), 5, True),
    (Interval(4, 7), 8, False),

]


@pytest.mark.parametrize("interval1, point, expected_result", point_in_interval)
def test_cross(interval1, point, expected_result):
    assert interval1.point_in_interval() == expected_result