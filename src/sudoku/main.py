import ui
import PyQt5
import sys

TIME = 1000
DIFFICULTY = 10

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    sudoku_ui = PyQt5.QtWidgets.QMainWindow()

    ui = ui.UiSudokuClass(sudoku_ui, TIME, DIFFICULTY)
    sudoku_ui.show()

    sys.exit(app.exec_())
