stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices_yesterday):

    # убедимся, что количество цен в массиве превышает 2
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Получение прибыли требует как минимум двух цен в массиве')

    # инициализируем min_price и max_profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # пропустим 0-ой элемент массива, так как min_price инициализирован.
        # Также продавать в 0-й позиции нельзя
        if index == 0:
            continue

        # вычисляем потенциальную прибыль
        potential_profit = current_price - min_price

        # обновляем максимальную прибыль
        max_profit = max(max_profit, potential_profit)

        # обновляем минимальную цену
        min_price  = min(min_price, current_price)

    return max_profit

print(get_max_profit(stock_prices_yesterday))
#вернет 6 (купили за 5, продали за 11)

