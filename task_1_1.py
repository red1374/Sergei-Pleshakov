test_durations = [53, 153, 4153, 400153]


def date_from_time(_duration):
    result = ''
    days = houers = minutes = 0

    days = _duration // (3600 * 24)
    if days > 0:
        result += str(days) + ' дн '

    houers = (_duration // 3600) % 24
    if houers > 0 or result:
        result += str(houers) + ' час '

    minutes = (_duration // 60) % 60
    if minutes > 0 or result:
        result += str(minutes) + ' мин '

    result += str(_duration % 60) + ' сек'
    print(_duration, 'сек :', result)


print('Вывод информации о промежутке времени')

while True:
    duration = input('Укажите число секунд или нажмите t для проверки тестовых значений\n')
    if duration.isdigit():
        date_from_time(int(duration))
        break
    elif duration == 't':
        for idx in range(len(test_durations)):
            date_from_time(test_durations[idx])
        break
