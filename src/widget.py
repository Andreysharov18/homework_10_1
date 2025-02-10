from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию о картах и счетах"""
    number_card = ''.join(el if el.isdigit() else '' for el in data_card)
    number_card_mask = get_mask_card_number(number_card)
    name_card = ''.join("" if el.isdigit() else el for el in data_card)
    data_card_mask = name_card + number_card_mask
    return data_card_mask


#для промежуточного коммита


def get_date(user_date: str) -> str:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ"""
    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
