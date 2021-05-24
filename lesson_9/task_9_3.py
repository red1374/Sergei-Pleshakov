class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income[0], 'bonus': income[1]}


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.surname, self.name])

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position1 = Position('Иван', 'Петров', 'менеджер', [5000, 3000])
print(dir(position1))
print(position1.name, position1.surname, position1.position, position1._income)
print(position1.get_full_name())
print(position1.get_total_income())
