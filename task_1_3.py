# Вывод словоформы слова процент
def get_percent_word(_number):
    if not str(_number).isdigit():
        return 0

    word = 'процент'

    if (5 <= _number <= 20 or _number % 10 == 0) or 5 <= _number % 10 <= 9:
        word += 'ов'
    elif 2 <= _number % 10 <= 4:
        word += 'a'

    print(_number, word)


for digit in range(21):
    get_percent_word(digit)
