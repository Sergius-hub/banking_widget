from typing import Any, Dict, List


def filter_by_state(list_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и параметр
    state, возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение.
    :param list_dicts: list[dict]
    :param state = 'EXECUTED'
    :return: list[dict]
    """
    # Формируем список при условии что, внутри списка словари
    # и в словаре есть ключ "state" равный state опциональному параметру
    return [d for d in list_dicts if isinstance(d, dict) and d.get("state") == state]


def sort_by_date(list_dicts: List[Dict[str, Any]], is_reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате.
    :param list_dicts: list[dict]
    :param is_reverse: bool = True
    :return:
    """
    # Создаем переменную где будем хранить результат или пустой список
    result = list(dict())

    # Внутрення key функция с проверками для lamda функции, необходима для sorted()
    def get_date_by_ggggmmdd(str_date: str) -> str:
        try:
            # Ищщем ошибки неправильного типа и размера строки
            if not isinstance(str_date, str):
                raise TypeError("в функцию передана не строка")
            if len(str_date) < 10:
                raise Exception("недостаточно символов для даты")
            # Получаем срезы для года, месяца и дня
            gggg = str_date[:4]
            mm = str_date[5:7]
            dd = str_date[8:10]
            # Проверяем год, месяц и дату на то что они являются числами
            if not gggg.isdigit() or not mm.isdigit() or not dd.isdigit():
                raise ValueError("неправильные значения gggg, mm, dd")
        # Ловим все стандартные ошибки
        except Exception as e:
            print(f"Ошибка: {e}")
        # Выводим f строку c результатами
        # key lambda функция в sorted выводит ошибки, но не прерывает вычисление
        return f"{gggg}{mm}{dd}"

    try:
        # Формируем сортированный список
        result = sorted(list_dicts, key=lambda d: get_date_by_ggggmmdd(d["date"]), reverse=is_reverse)

        # Ловим ошибки
    except Exception as e:
        print(f"Ошибка: {e}")

    # Результат сортированный список либо пустой
    return result
