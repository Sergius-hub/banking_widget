from .masks import get_mask_account, get_mask_card_number


def mask_account_card(value_str: str) -> str:
    """
    Функция mask_account_card(account_or_card), принимает строку с номером карты или номером счёта,
    возвращает такую же строку только с замаскированной строкой номера карты или счёта.
    :param account_or_card: Visa Platinum 7000792289606361
    :return masked string: Visa Platinum 7000 79** **** 6361
    """
    result = ""
    # Проверка типа
    if not isinstance(value_str, str):
        raise TypeError("Ошибка: аргумент не строка")
    # Проверка размерности
    value_size = len(value_str)
    if value_size < 16:
        raise ValueError("Ошибка: недостаточно символов")

    # Выбор между счетом и картой
    if value_size == 16 or value_size == 20:
        number_str = value_str
    elif 16 < value_size < 20:
        # Проверка пробела
        if value_str[-17] != " ":
            raise ValueError("Ошибка: отсутствует пробел отделяющий номер карты")
        number_str = value_str[-16:]
    elif value_size > 20:
        # Если в -17 позиции пробел, то номером считаем [-16:]
        if value_str[-17] == " ":
            number_str = value_str[-16:]
        else:
            # Проверка пробела
            if value_str[-21] != " ":
                raise ValueError("Ошибка: отсутствует пробел отделяющий номер счёта")
            number_str = value_str[-20:]

    # Проверка на число
    if not number_str.isdigit():
        raise ValueError("Ошибка: номер карты или счета не является числом")

    # Определяем размер строки номера
    number_str_size = len(number_str)

    # Пройдены все проверки формируем результирующую строку
    if number_str_size == 16:
        result = value_str[:-16] + get_mask_card_number(int(number_str))
    elif number_str_size == 20:
        result = value_str[:-20] + get_mask_account(int(number_str))

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
