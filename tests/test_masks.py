import pytest

from src.masks import get_mask_account, get_mask_card_number

# 1. КОНСТАНТЫ С ТЕСТОВЫМИ ДАННЫМИ ДЛЯ НОМЕРА КАРТЫ
SUCCESS_CASES_CARD_NUMBERS = [
    (7000792289606361, "7000 79** **** 6361"),
    (1234567890123456, "1234 56** **** 3456"),
    (1111222233334444, "1111 22** **** 4444"),
    (8888888888888888, "8888 88** **** 8888")
]

ERROR_CASES_TYPE_CARD_NUMBERS = [
    "7000792289606361",  # строка
    "1234-5678-9012",    # форматированная строка
    "",                  # пустая строка
    None,                # None
]

ERROR_CASES_VALUE_CARD_NUMBERS = [
    1234,               # слишком короткий
    -123456789012345,   # отрицательный
    0,                  # ноль
]

# Тестируем УСПЕШНЫЕ сценарии функции get_mask_card_number(card_number)
@pytest.mark.parametrize("card_number, expected_result", SUCCESS_CASES_CARD_NUMBERS)
def test_get_mask_card_number_success(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result

# Тестируем ошибки типов в аргументах функции get_mask_card_number(card_number)
@pytest.mark.parametrize("invalid_type", ERROR_CASES_TYPE_CARD_NUMBERS)
def test_get_mask_card_number_type_errors(invalid_type):
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_type)

# Тестируем ошибки значений в аргументах функции get_mask_card_number(card_number)
@pytest.mark.parametrize("invalid_value", ERROR_CASES_VALUE_CARD_NUMBERS)
def test_get_mask_card_number_value_errors(invalid_value):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_value)

# 2. КОНСТАНТЫ С ТЕСТОВЫМИ ДАННЫМИ ДЛЯ НОМЕРА СЧЕТА
SUCCESS_CASES_ACCOUNT_NUMBERS = [
    (70007922896063611234, "**1234"),
    (12345678901212343456, "**3456"),
    (11112222333312344444, "**4444"),
    (88888888888812348888, "**8888")
]

ERROR_CASES_TYPE_ACCOUNT_NUMBERS = [
    "70007922896063611234",  # строка
    "1234-5678-9012-9999",    # форматированная строка
    "",                  # пустая строка
    None,                # None
]

ERROR_CASES_VALUE_ACCOUNT_NUMBERS = [
    1234,               # слишком короткий
    -1234567890123456789,   # отрицательный
    0,                  # ноль
]

@pytest.mark.parametrize("account_number, expected_result", SUCCESS_CASES_ACCOUNT_NUMBERS)
def test_get_mask_account_success(account_number, expected_result):
    assert get_mask_account(account_number) == expected_result

@pytest.mark.parametrize("invalid_type", ERROR_CASES_TYPE_ACCOUNT_NUMBERS)
def test_get_mask_account_type_errors(invalid_type):
    with pytest.raises(TypeError):
        get_mask_account(invalid_type)

@pytest.mark.parametrize("invalid_value", ERROR_CASES_VALUE_ACCOUNT_NUMBERS)
def test_get_mask_account_type_errors(invalid_value):
    with pytest.raises(ValueError):
        get_mask_account(invalid_value)