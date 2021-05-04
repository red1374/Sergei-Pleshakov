from requests import get, utils
from decimal import Decimal, ROUND_HALF_EVEN
from datetime import date, datetime

CURRENCIES_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def get_data(url):
    """
    Get data by given url
    :param url:
    :return: document content
    """
    if url is None or url == '':
        return None

    response = get(url)
    if response.status_code != 200:
        return None

    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    file_datetime = datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S GMT')

    return dict(
        date=date(file_datetime.year, file_datetime.month, file_datetime.day),
        text=content
    )


def currency_rates(code=''):
    """
    Get currency rate by given currency code
    :param code: currency code
    :return: currency rate value and actual course date
    """
    if code is None or not isinstance(code, str) or code.strip() == '':
        return None

    code = code.strip().upper()

    rates = get_data(CURRENCIES_URL)
    if rates is None:
        return None

    currency_rate = 0.0
    for rate_row in rates['text'].split('<NumCode>'):
        if rate_row.find('<CharCode>' + code + '</CharCode>') > 0:
            currency_rate = rate_row[rate_row.find('<Value>') + 7:rate_row.find('</Value>')].replace(',', '.')
            currency_name = rate_row[rate_row.find('<Name>') + 6:rate_row.find('</Name>')]
            currency_nominal = int(rate_row[rate_row.find('<Nominal>') + 9:rate_row.find('</Nominal>')])
            break

    if currency_rate == 0:
        return None
    else:
        currency_rate = Decimal(currency_rate)
        return dict(
            course_rate=currency_rate.quantize(Decimal('1.00'), ROUND_HALF_EVEN),
            course_name=currency_name,
            course_date=rates['date'],
            course_nominal=currency_nominal
        )


def print_course(code=''):
    course = currency_rates(code)

    if course is None or not isinstance(course, dict) or course['course_rate'] is None:
        return None

    print(f'Курс валюты "{course["course_name"]}" на {course["course_date"]}:\n'
          f' {course["course_rate"]} руб. за {course["course_nominal"]} {code.upper()}')
