import re


class ValueError(ValueError):
    def __init__(self, email):
        self.message = f'wrong email: "{email}"!'
        super().__init__(self.message)


RE_EMAIL = re.compile(r'(?P<username>[\w\d_-]+)@(?P<domain>[\w\d-]+\.[^\d]{2,3})')
email_list = ['someone@geekbrains.ru', 'test@unocore.org', 'менеджер@госуслуги.рф', 'manager@store',
              'info85_78@games.dev', 'ultrageek1987.net', '568mess_in_my-head@stuff.com', 'just@another@string']


def email_parse(email_string=''):
    result = RE_EMAIL.match(email_string)

    if isinstance(result, re.Match):
        return result.groupdict()
    else:
        raise ValueError(email_string)


for email in email_list:
    print(email, email_parse(email))
