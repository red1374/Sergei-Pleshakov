src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]


def get_bigger_num(_src):
    for idx in range(len(_src)):
        if idx != 0:
            if _src[idx] > _src[idx - 1]:
                yield _src[idx]


result = get_bigger_num(src)
print(*result)
