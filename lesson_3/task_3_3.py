def thesaurus(*args):
    result = {}
    for item in args:
        if item == '' or not isinstance(item, str):
            continue

        if not result.get(item[0]) is None:
            if item not in result[item[0]]:
                result[item[0]].append(item)
        else:
            result[item[0]] = [item]

    return result


def sort_by_key(dict_input: dict, is_revers=False):
    if not isinstance(dict_input, dict):
        return None

    return dict(sorted(dict_input.items(), reverse=is_revers))


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
#print(thesaurus("Иван", 5, "Петр", "Илья"))
#print(thesaurus())

print(sort_by_key(thesaurus("Мария", "Юлия", "Иван",  "Петр", "Илья"), True))
