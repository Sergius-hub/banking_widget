from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card: str) -> str:
    """
    Функция mask_account_card(account_or_card), принимает строку с номером карты или номером счёта,
    возвращает такую же строку только с замаскированной строкой номера карты или счёта.
    :param account_or_card: Visa Platinum 7000792289606361
    :return masked string: Visa Platinum 7000 79** **** 6361
    """
    try:

        result = ""
        size_str = len(account_or_card)
        # Проверяем длину строки
        if size_str < 16:
            raise ValueError("Ошибка: недостаточно символов")

        # Определяем позицию среза с конца строки
        offset_reverse = -16

        # Полагаем что это номер карты
        card_number = account_or_card[offset_reverse:]

        # Проверяем номер карты число?
        if not card_number.isdigit():
            raise ValueError("Ошибка: неправильный номер карты или счёта")

        # Проверяем строку на 20 и более символов
        if size_str >= 20:
            # Если строка более 20 можем взять срез, и полагаем что это префикс для номера счета
            account_number_prefix = account_or_card[offset_reverse - 4 : offset_reverse]
            # Если префикс число, это номер счета
            if account_number_prefix.isdigit():
                # Если цифр достаточно для номера счета уменьшаем офсет
                offset_reverse -= 4

        # Проверяем пробел
        if account_or_card[offset_reverse - 1] != " ":
            if offset_reverse == -16:
                raise ValueError("Ошибка: нет пробела для разделения номера карты")
            elif offset_reverse == -20:
                raise ValueError("Ошибка: нет пробела для разделения номера счета")

    except ValueError as e:
        # Возврат ошибки
        return str(e)

    else:
        # Строим результирующую строку
        if offset_reverse == -16:
            result = account_or_card[:offset_reverse] + get_mask_card_number(int(card_number))
        elif offset_reverse == -20:
            result = account_or_card[:offset_reverse] + get_mask_account(int(account_number_prefix + card_number))

        return result


def get_date(str_date: str) -> str:
    """
    Функция get_date(str_date) принимает строку с датой в начале,
    возвращает только дату в формате ДД.ММ.ГГГГ
    :param str_date: "2024-03-11T02:26:18.671407"
    :return: string date: "11.03.2024"
    """
    try:
        result = ""
        # Проверяем длину строки
        if len(str_date) < 10:
            raise ValueError("Ошибка: недостаточно символов")

        # Получаем дату, месяц, год
        day_from_date = str_date[8:10]
        month_from_date = str_date[5:7]
        year_from_date = str_date[:4]

        # Если хотя бы одно из значений не число, возвращаем ошибку
        if not day_from_date.isdigit() or not month_from_date.isdigit() or not year_from_date.isdigit():
            raise ValueError("Ошибка: некорректная дата")

    except ValueError as e:
        # Возврат ошибки
        return str(e)

    else:
        # Формируем дату в нужном формате
        result = f"{day_from_date}.{month_from_date}.{year_from_date}"

        return result
