from json import dump, load

# Prepare data from files
with open('files/users.csv', 'r', encoding='UTF-8') as f_users:
    users = f_users.readlines()
users = [user.strip().replace(',', ' ') for user in users]
with open('files/hobby.csv', 'r', encoding='UTF-8') as f_hobbies:
    hobbies = f_hobbies.readlines()
hobbies = [hobby.strip().split(',') for hobby in hobbies]

if len(hobbies) > len(users):
    print(1)
else:
    # Add empty values to a list
    hobbies.extend([None] * (len(users) - len(hobbies)))
    # Create a dictionary from two lists
    users_hobbies = {key: val for key, val in zip(users, hobbies)}
    with open('files/user_hobbies.csv', 'w', encoding='UTF-8') as f:
        dump(users_hobbies, f)

    # Check saved data from a file
    with open('files/user_hobbies.csv', 'r', encoding='UTF-8') as f:
        print(load(f))
