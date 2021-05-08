num = int(input('Укажите число элементов\n'))

odd_to_15 = (i for i in range(1, num + 1, 2))
for num in range(1, num + 1, 2):
    print(next(odd_to_15))
