# Get list of tuples from nginx_logs.txt file with format (<remote_addr>, <request_type>, <requested_resource>)
# from time import perf_counter

result = []
# start = perf_counter()
with open('files/nginx_logs.txt', encoding='UTF-8') as f:
    for line in f:
        row_list = line.split(' ')  # .replace('"', '')
        result.append((row_list[0], row_list[5].replace('"', ''), row_list[6]))
# print(perf_counter() - start)
print(result[15200:15207])
