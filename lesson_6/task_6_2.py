# Get list of tuples from nginx_logs.txt file with format (<remote_addr>, <request_type>, <requested_resource>)

users = {}
with open('files/nginx_logs.txt', encoding='UTF-8') as f:
    for line in f:
        row_list = line.split(' ')
        if users.get(row_list[0]) is not None:
            users[row_list[0]] += 1
        else:
            users[row_list[0]] = 1

sorted_dict = dict(sorted(users.items(), key=lambda item: item[1]))
spammer = sorted_dict.popitem()
print('Spammer is:', spammer[0], 'with', spammer[1], 'requests', sep=' ')
