from dokusan import generators


def generate_instance(rank):
    sudoku = generators.random_sudoku(avg_rank=rank)
    return str(sudoku)
