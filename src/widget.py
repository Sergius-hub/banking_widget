def mask_account_card(account_or_card):
    result = ""
    size_str = len(account_or_card)
    # Проверяем длину строки
    if size_str < 16:
        return "Ошибка: недостаточно символов"

    # Определяем позицию среза с конца строки
    offset_reverse = -16

    # Полагаем что это номер карты
    card_number = account_or_card[offset_reverse:]

    # Проверяем номер карты число?
    if not card_number.isdigit():
        return "Ошибка: Неправильный номер карты или счёта"

    # Проверяем строку на 20 и более символов
    if size_str >= 20:
        # Если строка более 20 можем взять срез, и полагаем что это префикс для номера счета
        account_number_prefix = account_or_card[offset_reverse-4:offset_reverse]
        # Если префикс число, это номер счета
        if account_number_prefix.isdigit():
            result = account_number_prefix + card_number

    # Проверяем результат если он = "" значит это номер карты
    if result == "":
        result = card_number

    return result



print(mask_account_card("Maestro 7000792289606361"))