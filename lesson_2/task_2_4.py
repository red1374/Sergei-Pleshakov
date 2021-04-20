# Print messages from the list _messages and replace __NAME__ tag with a given _name parameter
def print_message(_messages, _name):
    if _messages is False or _name is False:
        return 'Empty message'

    for idm in range(len(_messages)):
        print(_messages[idm].replace('__NAME__', _name))


messages = [
    'Привет, __NAME__!',
    'У нас для тебя отличная новость. __NAME__, с понедельника мы повышаем тебе зарплату в ДВА раза! ',
    '__NAME__, с тобой все хорошо?',
    '__NAME__? Ты себя хорошо чувствуешь? Принесите кто-нибудь воды! ...',
    'Так __NAME__. Что-то ты неважно выглядишь.',
    'Иди-ка ты в отпуск, подлечись, а через две недели приступай к своей новой должности'
]
employes = [
    'инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита'
]

# Get names from a list
for idx in range(len(employes)):
    employes[idx] = employes[idx][::-1][0:employes[idx][::-1].index(' ')][::-1].capitalize()

print_message(messages, employes[2])
