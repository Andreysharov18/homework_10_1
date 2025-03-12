import pytest

from src.processing import filter_by_state, sort_by_date

from typing import Any

# Исходные данные
list_of_dicts = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

def filter_by_state(list_of_dict: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    return [d for d in list_of_dict if d.get("state") == state]

def sort_by_date(list_of_dict: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    sorted_list = sorted(
        list_of_dict, key=lambda new_list_of_dict: new_list_of_dict["date"], reverse=reverse
    )
    return sorted_list

# Тесты
def test_filter_by_state_executed():
    result = filter_by_state(list_of_dicts, "EXECUTED")
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
    assert result == expected

def test_filter_by_state_canceled():
    result = filter_by_state(list_of_dicts, "CANCELED")
    expected = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]
    assert result == expected

def test_filter_by_state_empty_result():
    result = filter_by_state(list_of_dicts, "PENDING")
    expected = []
    assert result == expected

def test_sort_by_date_default():
    result = sort_by_date(list_of_dicts)
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
    assert result == expected

def test_sort_by_date_reverse():
    result = sort_by_date(list_of_dicts, reverse=False)
    expected = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert result == expected

# Запуск тестов
if __name__ == "__main__":
    pytest.main()