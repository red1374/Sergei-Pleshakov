from random import choice


def get_next_word(words_list, remove_item=False):
    """
    Get next word from the given list
    :param words_list:
    :param remove_item: flag to remove an item from a given list
    :return: random chosen item
    """

    next_word = choice(words_list)
    if not remove_item:
        words_list.remove(next_word)

    return next_word


def get_jokes(jokes_count: int, can_be_repeated=True):
    """
    Get random generated jokes list
    :param jokes_count: number of jokes to be generated
    :param can_be_repeated: flag to check if a words in jokes can be repeated
    :return: a list with random generated jokes
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []

    for idj in range(jokes_count):
        if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
            break
        jokes.append(' '.join([get_next_word(nouns, can_be_repeated), get_next_word(adverbs, can_be_repeated), get_next_word(adjectives, can_be_repeated)]))

    return jokes


print(get_jokes(50, can_be_repeated=False))

print(get_jokes(6))