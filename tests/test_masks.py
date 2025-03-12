import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
  return "1234567812345678" # стандартная длина


def test_get_mask_card_number(card_number):
  masked_number = get_mask_card_number(card_number)
  assert masked_number == "1234 56** **** 5678"


import pytest

@pytest.fixture
def test_get_mask_account():
    account_number = '73654108430135874305'
    masked_account = get_mask_account(account_number)
    assert masked_account == "****************4305"

def test_get_mask_card_number_valid():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"

def test_get_mask_card_number_too_short():
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("123456789012345")  # 15 цифр
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("1234567")  # 7 цифр

def test_get_mask_account_too_short():
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 8 цифр."):
        get_mask_account("1234567")  # 7 цифр
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 8 цифр."):
        get_mask_account("123456")  # 6 цифр

# Запуск тестов
if __name__ == "__main__":
    pytest.main()