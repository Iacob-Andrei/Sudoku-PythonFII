import numpy
from dokusan import generators


def generate_instance(rank: int) -> str:
    """
    generates an instance of the game using dokusan.Generators
    :param rank: difficulty of the instance
    :return: string representing initial matrix
    """
    sudoku = generators.random_sudoku(avg_rank=rank)
    return str(sudoku)


def verify_final_instance(matrix: numpy.array) -> bool:
    """
    checks if given matrix is a valid solution
    :param matrix: to be verified
    :return: True if final solution, False if not
    """
    if '' in matrix:
        return False
    return verify_on_line(matrix) and verify_on_column(matrix) and verify_small_matrix(matrix)


def verify_on_line(matrix: numpy.array) -> bool:
    """
    check if there are duplicate numbers on lines
    :param matrix: to be verified
    :return: True if ok, False if not
    """
    for index in range(matrix.shape[0]):
        line = matrix[index, :]
        if len(line) != len(set(line)):
            return False
    return True


def verify_on_column(matrix: numpy.array) -> bool:
    """
    check if there are duplicate numbers on rows
    :param matrix: to be verified
    :return: True if ok, False if not
    """
    for index in range(matrix.shape[1]):
        column = matrix[:, index]
        if len(column) != len(set(column)):
            return False
    return True


def verify_small_matrix(matrix: numpy.array) -> bool:
    """
    checks if there are duplicate numbers on small matrices
    :param matrix: to be verified
    :return: True if ok, False if not
    """
    for line in range(0, 9, 3):
        for column in range(0, 9, 3):
            mat = list()
            for i in range(line, line+3):
                for j in range(column, column+3):
                    if matrix[i][j] in mat:
                        return False
                    mat.append(matrix[i][j])
    return True
