def num_translate(_number: str = ""):
    dictionary = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    return dictionary.get(_number)


print(num_translate('one'))
print(num_translate('eight'))
print(num_translate('ten'))
print(num_translate(5))
print(num_translate())
