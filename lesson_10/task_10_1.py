class MatrixDimensionError(Exception):
    def __init__(self):
        self.message = 'Matrices dimensions mismatch'
        super().__init__(self.message)


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = []
        if self._check_dimensions(other.matrix):
            for idx, row in enumerate(self.matrix):
                new_row = (item + other.matrix[idx][idx1] for idx1, item in enumerate(row))
                result.append(new_row)

        return Matrix(result)

    def _check_dimensions(self, matrix):
        if len(self.matrix) != len(matrix):
            raise MatrixDimensionError

        for idx, row in enumerate(self.matrix):
            if len(row) != len(matrix[idx]):
                raise MatrixDimensionError

        return True

    def __str__(self):
        if not self.matrix:
            return str(None)

        # matrix_str = (' '.join(map(str, el)) for el in self.matrix)
        matrix_str = (' '.join(map(lambda x: '{:<3}'.format(x), el)) for el in self.matrix)

        return '\n'.join(matrix_str) + '\n'


matrix1 = [
    [1, 1, 1, 15],
    [0, 3, 1, 6],
    [-3, 9, 8, 15]
]
matrix2 = [
    [0, 1, 8, -7],
    [6, 10, 5, 2],
    [6, 9, 12, -8]
]
# matrix2 = [
#     [0, 1, 8],
#     [6, 10, 5],
#     [6, 9, 12]
# ]
m1 = Matrix(matrix1)
m2 = Matrix(matrix2)
print(m1)
print(m2)
print(m1 + m2)
