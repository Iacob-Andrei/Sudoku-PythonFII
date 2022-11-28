import numpy
from dokusan import generators


def generate_instance(rank: int) -> str:
    sudoku = generators.random_sudoku(avg_rank=rank)
    return str(sudoku)


def verify_final_instance(matrix: numpy.array) -> bool:
    if '' in matrix:
        return False
    return verify_on_line(matrix) and verify_on_column(matrix) and verify_small_matrix(matrix)


def verify_on_line(matrix: numpy.array) -> bool:
    for index in range(matrix.shape[0]):
        line = matrix[index, :]
        if len(line) != len(set(line)):
            return False
    return True


def verify_on_column(matrix: numpy.array) -> bool:
    for index in range(matrix.shape[1]):
        column = matrix[:, index]
        if len(column) != len(set(column)):
            return False
    return True


def verify_small_matrix(matrix: numpy.array) -> bool:
    matrices = list()

    for line in range(0, 9, 3):
        for column in range(0, 9, 3):
            mat = list()
            for i in range(line, line+3):
                for j in range(column, column+3):
                    mat.append(matrix[i][j])
            matrices.append(mat)

    for mat in matrices:
        if len(mat) != len(set(mat)):
            return False
    return True
