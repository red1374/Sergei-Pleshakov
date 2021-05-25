from random import randint


class DeadCellWithNegativeCores(Exception):
    def __init__(self):
        self.message = 'The second cell is too BIG!!!'
        super().__init__(self.message)


class Cell:
    def __init__(self, cores:int):
        self.cores = cores

    def __add__(self, other):
        return Cell(self.cores + other.cores)

    def __sub__(self, other):
        if self.cores - other.cores > 0:
            return Cell(self.cores - other.cores)
        else:
            raise DeadCellWithNegativeCores

    def __mul__(self, other):
        return Cell(self.cores * other.cores)

    def __floordiv__(self, other):
        return Cell(self.cores // other.cores)

    def __truediv__(self, other):
        return Cell(self.cores // other.cores)

    def __str__(self):
        return f'Cell with {self.cores} cores'

    @staticmethod
    def make_order(cell, cores_in_row: int):
        result = ''
        for row_index in range(cell.cores // cores_in_row):
            result += '*' * cores_in_row + '\n'
        if cell.cores % cores_in_row:
            result += '*' * (cell.cores % cores_in_row)

        return result


cell1 = Cell(12)
print(cell1)
cell2 = Cell(7)
print(cell2)

print('Summ: ', cell1 + cell2)
print('Subtraction: ', cell1 - cell2)
print('Multiplication: ', cell1 * cell2)
print('Division: ', cell1 / cell2, cell1 // cell2)

print('-' * 20 + '\n' * 2)
for rend_cells in (randint(3, 10) for item in range(2, 7)):
    print('Cells in row:', rend_cells)
    print('with', cell1.cores, 'cores')
    print(Cell.make_order(cell1, rend_cells))
    print('with', cell2.cores, 'cores')
    print(Cell.make_order(cell2, rend_cells))
    print()
