def num_translate_adv(_number: str = ""):
    if _number == '' or not isinstance(_number, str):
        return None

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
    if _number[0].isupper():
        return str(dictionary.get(_number.lower())).title()
    else:
        return dictionary.get(_number)


print(num_translate_adv('One'))
print(num_translate_adv('Eight'))
print(num_translate_adv('ten'))
print(num_translate_adv(5))
print(num_translate_adv())
