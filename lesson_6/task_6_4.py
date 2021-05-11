users_f = open('files/users.csv', 'r', encoding='UTF-8')
hobbies_f = open('files/hobby.csv', 'r', encoding='UTF-8')
users_hobbies_f = open('files/user_hobbies.txt', 'w', encoding='UTF-8')

for user_line in users_f:
    hobbies_line = hobbies_f.readline()
    if hobbies_line == '':
        hobbies_line = 'None'
        user_line = '\n' + user_line.strip()
    else:
        user_line = user_line.strip()

    users_hobbies_f.write(user_line + ': ' + hobbies_line)

if hobbies_f.readline():
    print(1)

users_f.close()
hobbies_f.close()
users_hobbies_f.close()

# Check file result
with open('files/user_hobbies.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line)
