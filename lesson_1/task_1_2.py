# Вывести разбитое на разряды число
def number_formated(_number):
    if not str(_number).isdigit():
        return 0

    numbers_string = ''
    while(_number > 0):
        numbers_string = str(_number % 1000) + ' ' + numbers_string
        _number //= 1000

    return numbers_string


# Делится ли сумма цифр на заданное число
def is_sum_divided_by(_number, _digit):
    if not str(_number).isdigit() or (not str(_digit).isdigit() or _digit == 0):
        return 0

    summ = 0
    while(_number > 0):
        summ += _number % 10
        _number //= 10

    return summ % _digit == 0


# Вычисление суммы чисел, сумма цифр которых делится нацело на divider
def digits_summ(_digits, divider):
    if not _digits or (not str(divider).isdigit() or divider == 0):
        return 0

    summ = 0
    for idx in range(len(_digits)):
        if is_sum_divided_by(_digits[idx], 7):
            summ += _digits[idx]

    return summ


digits = []
# Создаем Список кубов нечетных цифр
for digit in list(range(1, 1000, 2)):
    digits.append(digit ** 3)

print('Сумма чисел, сумма цифр которых делится нацело на 7:', digits_summ(digits, 7))

for idx in range(len(digits)):
    # Добавляем к каждому числу списка 17
    digits[idx] += 17

print('После добавления 17 к каждому элементу списка сумма чисел стала равна:', digits_summ(digits, 7))
