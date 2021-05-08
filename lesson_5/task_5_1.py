def odd_nums(max_len):
    for i in range(1, max_len + 1, 2):
        yield i


num = int(input('Укажите число элементов\n'))
odd_to_15 = odd_nums(num)
for num in range(1, num + 1, 2):
    print(next(odd_to_15))
