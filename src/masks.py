def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""

    if len(card_number) < 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""

    if len(account_number) < 8:  # Предполагается, что номера счетов должны быть не менее 8 цифр
        raise ValueError("Номер счета должен содержать минимум 8 цифр.")

    return f"{'*' * (len(account_number) - 4)}{account_number[-4:]}"


print(get_mask_card_number("7000792289606361"))

print(get_mask_account("73654108430135874305"))
#изменения для коммита
