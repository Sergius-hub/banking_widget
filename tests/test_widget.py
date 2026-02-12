import pytest

from src.widget import mask_account_card

SUCCESS_CASES = [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
]

ERROR_CASES_INVALID_TYPE = [
    7000792289606361,   # число
    [],                 # пустой список
    None,               # None
]

ERROR_CASES_INVALID_VALUE = [
    "",                  # пустая строка
]

# @pytest.mark.parametrize("valid_value, expected_result", SUCCESS_CASES)
# def test_mask_account_card(valid_value, expected_result):
#     assert mask_account_card(valid_value) == expected_result

@pytest.mark.parametrize("invalid_type", ERROR_CASES_INVALID_TYPE)
def test_mask_account_card_type_errors(invalid_type):
    with pytest.raises(TypeError):
        mask_account_card(invalid_type)