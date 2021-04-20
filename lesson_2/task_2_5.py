# Get price formatted string for given _number parameter
def get_price_formatted(_number):
    if _number is False:
        return ''

    _template = '__RUB__ руб __KOP__ коп'
    price_list = str(_number).split('.')
    if len(price_list) == 1:
        price_list.append('00')
    else:
        price_list[1] = f'{int(price_list[1]):02d}'

    return _template.replace('__RUB__', price_list[0]).replace('__KOP__', price_list[1])


goods_prices = [
    45, 12.56, 89.70, 1001, 89, 54, 63.14, 79.8, 10.90, 45.30, 89.99, 70.80, 55, 45.69, 963.74, 75.63, 877, 1, 3.95, 6
]
goods_prices_formatted = []

# Subtask A. Print formatted price list
print('Subtask A')
for idx in range(len(goods_prices)):
    goods_prices_formatted.append(get_price_formatted(goods_prices[idx]))
print(', '.join(goods_prices_formatted))

# Subtask B. Check if sorted list hasn't changed his id
print('\nSubtask B')
print('List id before sorting: ', id(goods_prices), sep='')
goods_prices.sort()
print(goods_prices)
print('List id after sorting: ', id(goods_prices), sep='')

# Subtask C. Create new price list sorted descending
print('\nSubtask C')
print('List id before sorting: ', id(goods_prices), sep='')
goods_prices_desc = sorted(goods_prices, reverse=True)
print(goods_prices_desc)
print('List id after sorting: ', id(goods_prices_desc), sep='')

# Subtask D. Print out 5 most expansive goods
print('\nSubtask D')
print(sorted(goods_prices, reverse=True)[:5])
