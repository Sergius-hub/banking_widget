import pytest

from src.masks import get_mask_account, get_mask_card_number

# 1. КОНСТАНТЫ С ТЕСТОВЫМИ ДАННЫМИ
SUCCESS_CASES = [
    (7000792289606361, "7000 79** **** 6361"),
    (1234567890123456, "1234 56** **** 3456"),
    (1111222233334444, "1111 22** **** 4444"),
    (8888888888888888, "8888 88** **** 8888")
]

ERROR_CASES_TYPE = [
    "7000792289606361",  # строка
    "1234-5678-9012",    # форматированная строка
    "",                  # пустая строка
    None,                # None
]

ERROR_CASES_VALUE = [
    1234,               # слишком короткий
    -123456789012345,   # отрицательный
    0,                  # ноль
]

# Тестируем УСПЕШНЫЕ сценарии функции get_mask_card_number(card_number)
@pytest.mark.parametrize("card_number, expected_result", SUCCESS_CASES)
def test_get_mask_card_number_success(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result

# Тестируем ошибки типов в аргументах функции get_mask_card_number(card_number)
@pytest.mark.parametrize("invalid_type", ERROR_CASES_TYPE)
def test_get_mask_card_number_type_errors(invalid_type):
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_type)

# Тестируем ошибки значений в аргументах функции get_mask_card_number(card_number)
@pytest.mark.parametrize("invalid_value", ERROR_CASES_VALUE)
def test_get_mask_card_number_value_errors(invalid_value):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_value)


# # Тестируем функцию get_mask_account(account_number)
# @pytest.mark.parametrize(
#     "account_number, expected_result",
#     [
#         (73654108430135874305, "**4305")
#     ]
# )
# def test_get_mask_account(account_number, expected_result):
#     assert get_mask_account(account_number) == expected_result