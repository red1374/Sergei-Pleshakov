import re
RE = re.compile(r'(\d{2})-(\d{2})-(\d{4})')


class WrongDateFormatError(Exception):
    def __init__(self, date_value):
        self.txt = f'Wrong date format: {date_value}'


class WrongDateValueError(Exception):
    def __init__(self, value):
        self.txt = f'Wrong date value: {value}'


class Date:
    date = ''
    day = 0
    month = 0
    year = 0

    def __init__(self, date_str: str):
        Date.date = date_str

    @classmethod
    def get_int_date(cls):
        if RE.match(cls.date):
            Date.day, Date.month, Date.year = map(int, RE.findall(cls.date)[0])
        else:
            raise WrongDateFormatError(cls.date)

    @staticmethod
    def validate(date):
        if date.month < 1 or 12 < date.month:
            raise WrongDateValueError(f'Month must be between 1 and 12. Current value is \'{date.month}\'')

        if date.year < 1961 or 2021 < date.year:
            raise WrongDateValueError(f'Year must be between 1961 and 2021. Current value is \'{date.year}\'')

        print('Date is valid!')


date1 = Date('12-01-2009')
date1.get_int_date()
Date.validate(date1)

# date2 = Date('12.01.2009')
# date2.get_int_date()
# Date.validate(date2)

# date3 = Date('12-01-0000')
# date3.get_int_date()
# Date.validate(date3)

# date4 = Date('02-15-2009')
# date4.get_int_date()
# Date.validate(date4)

# date6 = Date('12-01-2025')
# date6.get_int_date()
# Date.validate(date6)
