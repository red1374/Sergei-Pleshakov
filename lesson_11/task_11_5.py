from classes.classes_def import Warehouse, Xerox, Scanner, Printer, Department
# Create warehouses
warehouse1 = Warehouse('warehouse 1')
warehouse2 = Warehouse('warehouse 2')

# Create equipments
xerox1 = Xerox('Samsung', 'XR-458', 5600, 'white', False, (200, 400, 680), 'big_xerox')
printer1 = Printer('Canon', 'Pixma-5200', 2300, 'silver', True, (200, 400, 40), 'inkjet')
printer2 = Printer('BenQ', 'Terra-50', 9200, 'black', True, (200, 400, 400), 'laser')
scanner1 = Scanner('Epson', 'Perfection V19', 8000, 'black', False, (248.5, 38.8, 364), 'CIS')

# Add equipment to the warehouses
warehouse1.set_equipment(xerox1, 1)
warehouse1.set_equipment(scanner1, 2)
warehouse1.set_equipment(printer2, 5)
warehouse1.set_equipment(printer1, 9)

warehouse2.set_equipment(printer1, 10)

print(warehouse1.get_equipment())
print(warehouse2.get_equipment())
print(f'Total Xerox models count: {Xerox.get_count()}')
print(f'Total Printer models count: {Printer.get_count()}')

# Check warehouse for equipment of given type
# print(warehouse1.get_equipment('Xerox'))
# print(warehouse1.get_equipment('Scanner'))
print(warehouse1.get_equipment('Printer'))

# Transfer equipment between warehouse and department
department1 = Department('Marketing')
warehouse1.transfer_equipment(department1, 'Printer', 14)
print(department1.get_equipment())
print(warehouse1.get_equipment('Printer'))
department1.transfer_equipment(warehouse1, 'Xerox', 10)

department1.transfer_equipment(warehouse1, 'Printer', 2)

