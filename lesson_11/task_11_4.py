from classes.classes_def import Warehouse, Xerox, Scanner, Printer

warehouse1 = Warehouse('warehouse 1')
print(warehouse1.name)

xerox1 = Xerox('Samsung', 'XR-458', 5600, 'white', False, (200, 400, 680), 'big_xerox')
print(xerox1)

printer1 = Printer('Canon', 'Pixma-5200', 2300, 'silver', True, (200, 400, 40), 'inkjet')
print(printer1)

scanner1 = Scanner('Epson', 'Perfection V19', 8000, 'black', False, (248.5, 38.8, 364), 'CIS')
print(scanner1)
