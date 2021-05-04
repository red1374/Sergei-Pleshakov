from requests import get, utils
from decimal import Decimal, ROUND_HALF_EVEN

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

    return content


def currency_rates(code=''):
    """
    Get currency rate by given currency code
    :param code: currency code
    :return: currency rate value
    """
    if code is None or not isinstance(code, str) or code.strip() == '':
        return None

    code = code.strip().upper()

    rate_rows = get_data(CURRENCIES_URL)
    if rate_rows is None:
        return None

    currency_rate = 0.0
    for rate_row in rate_rows.split('<NumCode>'):
        if rate_row.find('<CharCode>' + code + '</CharCode>') > 0:
            currency_rate = rate_row[rate_row.find('<Value>') + 7:rate_row.find('</Value>')].replace(',', '.')
            break

    if currency_rate == 0:
        return None
    else:
        currency_rate = Decimal(currency_rate)
        return currency_rate.quantize(Decimal('1.00'), ROUND_HALF_EVEN)


print('USD:', currency_rates('uSd'), sep=' ')
print('EUR:', currency_rates('eur'), sep=' ')
