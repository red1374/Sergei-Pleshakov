"""
Работаем в МФЦ.
Поддержка различных форм документов:
* свидетельство о рождении
* свидетельство о смене работы
* свидетельство о браке
Помним, что все должно быть масштабируемо!
"""


"""
маленькое повторение: написать свое исключение на нехватку данных
"""
class ClassArgumentError(Exception):
    def __init__(self, needed):
        self.message = f'We need more data! [{needed}]'
        super().__init__(self.message)


class PFR:
    def send_data(self):
        print('Form was sent')

    def update_data(self):
        print('updated')


class BaseForm:
    minimum_info = frozenset({'name', 'surname'})

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        res = [f"{key} : {value}" for key, value in self.__dict__.items()]
        return ', '.join(res)

    """
        Вынести в класс базовая форма метод проверки аргументов
    """
    def check_data(self, minimum_info):
        if not minimum_info:
            minimum_info = BaseForm.minimum_info

        if minimum_info.issubset(set(self.__dict__.keys())):
            return True
        else:
            more_data = [*minimum_info.difference(set(self.__dict__.keys()))]
            raise ClassArgumentError(' ,'.join(more_data))


class Passport(BaseForm):
    minimum_info = frozenset({'name', 'surname',
                              'birth_date', 'mothers_name',
                              'fathers_name'})

    def check_data(self):
        return super(Passport, self).check_data(Passport.minimum_info)


class BirthForm(BaseForm, PFR):
    pass


class MarriageForm(BaseForm):
    passport_info = frozenset({"name", "surname", "age"})

    def check_data(self):
        return super(MarriageForm, self).check_data(MarriageForm.passport_info)

    def get_passport_data(self, passport1, passport2):
        """
        Нужно вынуть passport_info из каждого из паспортов и добавить атрибуты к
        объекту данного класса, такие как
        self.name_1, self.name_2 так далее

        """
        self.__dict__.update({f'{key}_1': value for key, value in passport1.__dict__.items()
                              if key in MarriageForm.passport_info})
        self.__dict__.update({f'{key}_2': value for key, value in passport2.__dict__.items()
                              if key in MarriageForm.passport_info})

    def update_passport_data(self, passport1, passport2):
        if isinstance(passport1, Passport) and isinstance(passport2, Passport):
            passport1.__dict__['marriage_1'] = True
            passport2.__dict__['marriage_2'] = True
        else:
            print('Wrong passports!')


test_user = Passport(name="Basil", surname='Ivanov',
                     birth_date='19/05/1980',
                     fathers_name='Kirill', mothers_name='Natalia')

test_user1 = Passport(name="Katya", fathers_name='Anatoly', age='42',
                     birth_date='19/05/1978', mothers_name='Natalia')

print(test_user)

marrige_form1 = MarriageForm()
marrige_form1.update_passport_data(test_user, test_user1)
marrige_form1.get_passport_data(test_user, test_user1)
print(marrige_form1)


print(test_user.check_data())
# print(test_user1.check_data())
x = str(test_user)
