import datetime
from abc import ABC, abstractmethod


class NotEnoughEquipmentError(Exception):
    def __init__(self, type_name, qty):
        self.txt = f'Not enough equipment of type "\033[33m{type_name}\033[0m". Current value is {qty}'


class NotAnIntegerValueError(Exception):
    def __init__(self):
        self.txt = f'"Quantity" attribute must have an integer type'


class NoEquipmentOfGivenTypeError(Exception):
    def __init__(self, type_name):
        self.txt = f'There\'s no equipment of type "\033[33m{type_name}\033[0m"!'


class Transfer(ABC):
    def __init__(self):
        self._equipment = {}

    def set_equipment(self, equipment: object, quantity: int):
        if not Transfer.check_quantity_value(quantity):
            return None

        if not self._equipment.get(equipment.__class__.__name__):
            self._equipment[equipment.__class__.__name__] = {'items': [], 'qty': 0}

        self._equipment[equipment.__class__.__name__]['items'].append({
            'item': equipment,
            'qty': quantity,
            'date': datetime.datetime.now()})

        self._equipment[equipment.__class__.__name__]['qty'] += quantity

    def get_equipment(self, equipment_type=''):
        if not equipment_type:
            # Get all equipment from a warehouse
            return self._equipment
        else:
            # Get equipment from a warehouse of given type
            return self._equipment.get(equipment_type)

    @abstractmethod
    def transfer_equipment(self, where_to_transfer: object, equipment: object, quantity: int):
        pass

    def _delete_empty_items(self, equipment_type: object):
        """
        Delete empty dictionary and list items
        :param equipment_type:
        :return:
        """
        equipment_list = self._equipment.get(equipment_type)
        if equipment_list['qty'] == 0:
            del self._equipment[equipment_type]
        else:
            idx1 = 0
            while len(equipment_list['items']) > idx1:
                if equipment_list['items'][idx1]['qty'] == 0:
                    del equipment_list['items'][idx1]
                else:
                    idx1 += 1

    @staticmethod
    def check_quantity_value(qty):
        try:
            if not isinstance(qty, int):
                raise NotAnIntegerValueError
        except NotAnIntegerValueError as e:
            print(e.txt)
            return False
        else:
            return True


class Warehouse(Transfer):
    def __init__(self, name):
        super(Warehouse, self).__init__()
        self.name = name

    def transfer_equipment(self, department: object, equipment_type='', qty=0):
        """
            Transfer equipment of given type from a warehouse to a current department
            :param department:
            :param equipment_type:
            :param qty:
            :return:
        """

        if not Transfer.check_quantity_value(qty):
            return None

        try:
            if not isinstance(qty, int):
                raise NotAnIntegerValueError

            if not self._equipment.get(equipment_type):
                raise NoEquipmentOfGivenTypeError(equipment_type)

            if self._equipment.get(equipment_type)['qty'] < qty:
                raise NotEnoughEquipmentError(equipment_type, self._equipment.get(equipment_type)['qty'])

            equipment_list = self._equipment.get(equipment_type)
        except NotEnoughEquipmentError as e:
            print(e.txt)
        except NoEquipmentOfGivenTypeError as e:
            print(e.txt)
        except NotAnIntegerValueError as e:
            print(e.txt)
        else:
            for idx, equipment in enumerate(equipment_list['items']):
                if equipment['qty'] <= qty:
                    department.set_equipment(equipment['item'], equipment['qty'])
                    qty -= equipment['qty']
                    equipment_list['qty'] -= equipment['qty']
                    equipment['qty'] = 0
                else:
                    department.set_equipment(equipment['item'], qty)
                    equipment['qty'] -= qty
                    equipment_list['qty'] -= qty
                    break

            self._delete_empty_items(equipment_type)


class OfficeEquipment:
    def __init__(self, brand='', model='', price=0, color='', is_colored=False, sizes=()):
        self._brand = brand
        self._model = model
        self.__price = price
        self._color = color
        self._is_colored = is_colored
        self._sizes = sizes

    def __str__(self):
        return str(list(f'{key} => {value}' for key, value in self.__dict__.items()))

    @classmethod
    def get_count(cls):
        return cls.count


class Printer(OfficeEquipment):
    count = 0

    def __init__(self, brand='', model='', price=0, color='', is_colored=False, sizes=(), printer_type=''):
        super().__init__(brand, model, price, color, is_colored, sizes)
        self.type = printer_type
        Printer.count += 1


class Scanner(OfficeEquipment):
    count = 0

    def __init__(self, brand='', model='', price=0, color='', is_colored=False, sizes=(), scanner_type=''):
        super().__init__(brand, model, price, color, is_colored, sizes)
        self.type = scanner_type
        Scanner.count += 1


class Xerox(OfficeEquipment):
    count = 0

    def __init__(self, _brand='', _model='', _price=0, _color='', _is_colored=False, _sizes=(), xerox_type=''):
        super().__init__(brand=_brand, model=_model, price=_price, color=_color, is_colored=_is_colored, sizes=_sizes)
        self.type = xerox_type
        Xerox.count += 1


class Department(Transfer):
    def __init__(self, name):
        super(Department, self).__init__()
        self.name = name

    def transfer_equipment(self, warehouse: object, equipment_type='', qty=0):
        if not Transfer.check_quantity_value(qty):
            return None

        if self._equipment.get(equipment_type):
            print(f'Send an email to {warehouse.name}. They should take {qty} our broken {equipment_type} in two days')
        else:
            print(f'\033[33mWe don\'t have any {equipment_type} at our department.\033[0m')
