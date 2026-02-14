import pytest

from src.widget import mask_account_card, get_date

# Тесты функции mask_account_card(value_str: str) -> str
SUCCESS_CASES = [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("7000792289606361", "7000 79** **** 6361"),
    ("8888888888888888", "8888 88** **** 8888")
]

ERROR_CASES_INVALID_TYPE = [
    7000792289606361,   # число
    [],                 # пустой список
    None,               # None
]

ERROR_CASES_INVALID_VALUE = [
    "",                  # пустая строка
    "123456789012345",   # короткая строка
    "123456789012345D",  # неправильный номер
    "Visa Platinum7000792289606361",    # слитный номер
    "Счет73654108430135874305",         # слитный счет
    "Счет8430135874305",                # слитный номер
]
# УСПЕШНЫЕ ИСХОДЫ
@pytest.mark.parametrize("valid_value, expected_result", SUCCESS_CASES)
def test_mask_account_card(valid_value, expected_result):
    assert mask_account_card(valid_value) == expected_result

# ОШИБКИ ТИПА АРГУМЕНТА
@pytest.mark.parametrize("invalid_type", ERROR_CASES_INVALID_TYPE)
def test_mask_account_card_type_errors(invalid_type):
    with pytest.raises(TypeError):
        mask_account_card(invalid_type)

# ОШИБКИ ЗНАЧЕНИЯ АРГУМЕНТА
@pytest.mark.parametrize("invalid_value", ERROR_CASES_INVALID_VALUE)
def test_mask_account_card_value_errors(invalid_value):
    with pytest.raises(ValueError):
        mask_account_card(invalid_value)



# Тесты функции get_date(str_date: str) -> str
# УСПЕШНЫЕ ИСХОДЫ
@pytest.mark.parametrize("valid_value, expected_result",[
    ("2024-03-11T02:26:18.671407", "11.03.2024")
])
def test_get_date(valid_value, expected_result):
    assert get_date(valid_value) == expected_result

# ОШИБКИ ТИПА АРГУМЕНТА
@pytest.mark.parametrize("invalid_type", [
    20240311,       # число
    [],             # пустой список
    None            # ничего
])
def test_get_date_type_errors(invalid_type):
    with pytest.raises(TypeError):
        get_date(invalid_type)

# ОШИБКИ ЗНАЧЕНИЯ АРГУМЕНТА
@pytest.mark.parametrize("invalid_value", [
    "",            # Пустая строка
    "20240311",    # Короткая строка без разделителей
    "2024-03-41",  # Неправильная дата
    "202d-04-11",  # Неправильная дата
    "2026-02-30"   # Несуществующая дата
])
def test_get_date_value_errors(invalid_value):
    with pytest.raises(ValueError):
        get_date(invalid_value)

