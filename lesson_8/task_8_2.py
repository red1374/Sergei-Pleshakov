import re

RE_ROW = re.compile(r'((?:\d{1,3}\.){3}\d{1,3})\s-\s-\s\[(.+)]\s"(\w{3,7})\s(.+)\sHTTP/\d[.\d]*"\s(\d{3})\s(\d+)')


def get_row_info(row):
    result = RE_ROW.findall(row)
    return result


with open('files/nginx_logs.txt', 'r', encoding="UTF") as f:
    for indx, line in enumerate(f):
        print(line, get_row_info(line))
        if indx == 10:
            break
