# Проверка есть ли цифры в строке

while True:
    digits = []
    string = input("Введите строку для анализа. Для выхода введите exit\n")
    if string == 'exit':
        break

    for symbol in list(string):
        if symbol.isdigit():
            digits.append(symbol)

    if not digits:
        print("В указанной строке нет цифр")
    else:
        print("В указанной строке есть цифры", digits)
