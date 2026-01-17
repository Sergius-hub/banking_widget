def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты, возвращает строку с замаскированными цифрами номера карты"""
    # Ожидаем ошибку
    try:

        # Проверяем номер на соответствие типа аргумента, должен быть int
        if type(card_number).__name__ != "int":
            raise TypeError("Ошибка: неправильный тип аргумента в функции 'get_mask_card_number()' ")

        # Приводим число к строке
        card_number_str = str(card_number)

        # Проверяем количество символов (цифр числа), должно быть 16
        if len(card_number_str) != 16:
            raise ValueError("Ошибка: номер карты не соответствует 16-ти цифрам")

    # Блок обработки ошибок
    except (TypeError, ValueError) as e:
        # Возвращаем ошибку
        return str(e)
    else:
        # Производим маскировку и форматирование
        mask = card_number_str[:6] + "******" + card_number_str[-4:]
        formatted_mask = f"{mask[:4]} {mask[4:6]}** **** {mask[-4:]}"

        # Вывод: замаскированой строки
        return formatted_mask


def get_mask_account(account_number: int) -> str:
    """Функция принимает номер карты, возвращает строку с замаскированными цифрами номера карты"""

    # Ожидаем ошибку
    try:
        # Проверяем номер на соответствие типа аргумента, должен быть int
        if type(account_number).__name__ != "int":
            raise TypeError("Ошибка: неправильный тип аргумента в функции 'get_mask_account()'")
        # Приводим число к строке
        account_number_str = str(account_number)

        # Проверяем количество символов (цифр числа), должно быть 20
        if len(account_number_str) != 20:
            raise ValueError("Ошибка: номер карты не соответствует 20-ти цифрам")

    # Блок обработки ошибок
    except (TypeError, ValueError) as e:
        # Возвращаем ошибку
        return str(e)
    else:
        # Производим маскировку
        mask = f"**{account_number_str[-4:]}"

        # Вывод: замаскированой строки
        return mask
