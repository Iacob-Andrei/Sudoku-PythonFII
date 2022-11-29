import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import table


def cancel_popup():
    sys.exit()


class UiSudokuClass(object):
    to_place = None
    instance = table.generate_instance(10)
    matrix = []

    def __init__(self, SudokuClass):
        SudokuClass.setObjectName("SudokuClass")
        SudokuClass.setFixedSize(550, 650)
        SudokuClass.setLayoutDirection(QtCore.Qt.RightToLeft)
        SudokuClass.setWindowTitle("Sudoku")
        SudokuClass.setWindowIcon(QtGui.QIcon('resources/logo.png'))
        self.centralWidget = QtWidgets.QWidget(SudokuClass)
        self.centralWidget.setObjectName("centralWidget")

        self.Table = QtWidgets.QTableWidget(self.centralWidget)
        self.Table.setGeometry(QtCore.QRect(50, 30, 450, 450))

        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Table.setFont(font)
        self.Table.setMouseTracking(False)
        self.Table.setAcceptDrops(False)
        self.Table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Table.setAutoScrollMargin(16)
        self.Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Table.setTextElideMode(QtCore.Qt.ElideNone)
        self.Table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.Table.setGridStyle(QtCore.Qt.DashDotLine)
        self.Table.setWordWrap(True)
        self.Table.setRowCount(9)
        self.Table.setColumnCount(9)
        self.Table.setObjectName("Table")

        for line in range(0, 9):
            for column in range(0, 9):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Table.setItem(line, column, item)

        self.Table.horizontalHeader().setVisible(False)
        self.Table.horizontalHeader().setDefaultSectionSize(50)
        self.Table.horizontalHeader().setHighlightSections(False)
        self.Table.horizontalHeader().setMinimumSectionSize(10)
        self.Table.verticalHeader().setVisible(False)
        self.Table.verticalHeader().setDefaultSectionSize(50)
        self.Table.verticalHeader().setHighlightSections(False)
        self.Table.verticalHeader().setMinimumSectionSize(10)
        self.Table.selectionModel().selectionChanged.connect(self.handle_select_matrix)

        lines_coordonates = [(50, 170, 451, 21), (50, 320, 451, 21), (180, 30, 41, 451), (330, 30, 41, 451)]
        for index in range(0, 4):
            self.line = QtWidgets.QFrame(self.centralWidget)
            self.line.setGeometry(QtCore.QRect(lines_coordonates[index][0], lines_coordonates[index][1],
                                               lines_coordonates[index][2], lines_coordonates[index][3]))
            self.line.setFrameShadow(QtWidgets.QFrame.Plain)
            self.line.setLineWidth(3)
            if index > 1:
                self.line.setFrameShape(QtWidgets.QFrame.VLine)
            else:
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setObjectName(f"line_{index}")

        self.Table_2 = QtWidgets.QTableWidget(self.centralWidget)
        self.Table_2.setGeometry(QtCore.QRect(20, 510, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Table_2.setFont(font)
        self.Table_2.setMouseTracking(False)
        self.Table_2.setAcceptDrops(False)
        self.Table_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Table_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Table_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Table_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Table_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.Table_2.setGridStyle(QtCore.Qt.DashDotLine)
        self.Table_2.setWordWrap(True)
        self.Table_2.setRowCount(1)
        self.Table_2.setColumnCount(10)
        self.Table_2.setObjectName("Table_2")

        for index in range(0, 10):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.Table_2.setItem(0, index, item)

        self.Table_2.horizontalHeader().setVisible(False)
        self.Table_2.horizontalHeader().setDefaultSectionSize(50)
        self.Table_2.horizontalHeader().setHighlightSections(False)
        self.Table_2.horizontalHeader().setMinimumSectionSize(10)
        self.Table_2.verticalHeader().setVisible(False)
        self.Table_2.verticalHeader().setDefaultSectionSize(50)
        self.Table_2.verticalHeader().setHighlightSections(False)
        self.Table_2.verticalHeader().setMinimumSectionSize(10)
        SudokuClass.setCentralWidget(self.centralWidget)
        self.Table_2.selectionModel().selectionChanged.connect(self.handle_select_numbers)

        self.predefined_options()
        self.default_instance()
        QtCore.QMetaObject.connectSlotsByName(SudokuClass)

    def default_instance(self):
        for line in range(0, 9):
            for column in range(0, 9):
                nr = self.instance[line*9 + column]
                if nr != '0':
                    item = self.Table.item(line, column)
                    item.setText(nr)
                    brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    item.setBackground(brush)

    def predefined_options(self):
        for column in range(0, 9):
            item = self.Table_2.item(0, column)
            item.setText(f"{column+1}")

        item = self.Table_2.item(0, 9)
        item.setText('-')

    def handle_select_matrix(self, selected):
        if self.to_place is None:
            return

        row = column = 0
        for ix in selected.indexes():
            row = ix.row()
            column = ix.column()

        if self.instance[row*9 + column] != '0':
            return

        item = self.Table.item(row, column)
        item.setText(self.to_place)

        self.get_matrix_state()
        if table.verify_final_instance(self.matrix):
            self.show_popup("Congrats")
        self.Table.clearSelection()

    def handle_select_numbers(self, selected):
        index = 0
        for ix in selected.indexes():
            index = ix.column()

        if index == 9:
            self.to_place = ''
        else:
            item = self.Table_2.item(0, index)
            self.to_place = item.text()

    def get_matrix_state(self):
        self.matrix = []
        for line in range(0, 9):
            for column in range(0, 9):
                item = self.Table.item(line, column)
                self.matrix.append(item.text())
        self.matrix = np.array(self.matrix).reshape((9, 9))

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setWindowTitle(text)
        msg.setWindowIcon(QtGui.QIcon('resources/logo.png'))
        if text == "Congrats":
            msg.setText("Congrats, you finished the game!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Cancel)
        else:
            msg.setText("Unfortunately, the time is up!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Cancel)

        msg.buttonClicked.connect(cancel_popup)
        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sudoku_ui = QtWidgets.QMainWindow()

    ui = UiSudokuClass(sudoku_ui)
    sudoku_ui.show()

    sys.exit(app.exec_())
