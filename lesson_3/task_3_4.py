def thesaurus_adv(*args):
    result = {}
    for item in args:
        if item == '' or not isinstance(item, str):
            continue

        fio = item.split()
        if not result.get(fio[1][0]) is None:
            if not result[fio[1][0]].get(fio[0][0]) is None:
                if item not in result[fio[1][0]][fio[0][0]]:
                    result[fio[1][0]][fio[0][0]].append(item)
            else:
                result[fio[1][0]][fio[0][0]] = [item]
        else:
            result[fio[1][0]] = {}
            result[fio[1][0]][fio[0][0]] = [item]

    return result


def sort_by_key(dict_input: dict, is_revers=False):
    if not isinstance(dict_input, dict):
        return None

    return dict(sorted(dict_input.items(), reverse=is_revers))


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

print(sort_by_key(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"), False))
