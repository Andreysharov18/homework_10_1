import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
  return "1234567812345678" # стандартная длина


def test_get_mask_card_number(card_number):
  masked_number = get_mask_card_number(card_number)
  assert masked_number == "1234 56** **** 5678"





