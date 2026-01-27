def filter_by_state(list_dicts: list[dict], state: str="EXECUTED") -> list[dict]:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и параметр
    state, возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение.
    :param list_dicts: list[dict]
    :param state='EXECUTED'
    :return: list[dict]
    """
    return [ d for d in list_dicts if isinstance(d, dict) and d.get("state") == state ]


def sort_by_date(list_dicts: list[dict], is_reverse: bool=True ) -> list:
    """
    Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате.
    :return:
    """
    result = []
    try:
        result = sorted( list_dicts, key=lambda d: d["date"][:10], reverse=is_reverse )
    except KeyError as e:
        print( f"Ошибка: {e}" )
    return result

