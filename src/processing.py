from src.widget import get_date

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

# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
#         ],
#         "CANCELED"
#     )
# )


def sort_by_date(list_dicts: list[dict], reverse=True ):
    """
    Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате.
    :return:
    """

    return sorted( list_dicts, key=lambda d: d.get("date")[:10] )

list_sorted = sort_by_date(
    [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
)
for d in list_sorted:
    print(d, end="\n")

# unsorted = [
#     '2019-07-03T18:35:29.512364',
#     '2018-06-30T02:08:58.425572',
#     '2018-09-12T21:27:25.241689',
#     '2018-10-14T08:21:33.419441'
# ]

# sorted_list = sorted( unsorted, key=lambda x: x, reverse=False )
# for s in sorted_list:
#     print(s[:10], end="\n")
